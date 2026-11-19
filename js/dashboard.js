/* Retail Sales dashboard — dependency-free (data + SVG charts).
   The dataset is synthetic and deterministic (fixed seed), so it always shows the same numbers. */
(function () {
  'use strict';

  var C = { teal: '#0d9488', indigo: '#4f46e5', amber: '#d97706', rose: '#e11d48', blue: '#2563eb', violet: '#7c3aed' };
  var PALETTE = [C.teal, C.indigo, C.amber, C.rose, C.blue, C.violet];
  var MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

  /* ======================================================================
     1) SYNTHETIC DATA
     ====================================================================== */
  var REGIONS = [['Cairo', .32], ['Giza', .18], ['Alexandria', .16], ['Delta', .14], ['Upper Egypt', .12], ['Canal', .08]];
  var CHANNELS = [['Website', .45], ['Mobile App', .38], ['Marketplace', .17]];
  var CATS = [
    { name: 'Electronics',    p: .28, price: 4500, cost: .78, products: ['Smart Watch', 'Wireless Earbuds', '4K Monitor', 'Bluetooth Speaker'] },
    { name: 'Home & Kitchen', p: .22, price: 1800, cost: .66, products: ['Air Fryer', 'Coffee Maker', 'Vacuum Cleaner', 'Blender Set'] },
    { name: 'Fashion',        p: .20, price: 750,  cost: .52, products: ['Running Shoes', 'Denim Jacket', 'Leather Wallet', 'Cotton Hoodie'] },
    { name: 'Beauty',         p: .12, price: 420,  cost: .48, products: ['Skincare Set', 'Perfume 100ml', 'Hair Dryer', 'Makeup Kit'] },
    { name: 'Grocery',        p: .10, price: 350,  cost: .84, products: ['Olive Oil Pack', 'Coffee Beans 1kg', 'Snack Box', 'Protein Bars'] },
    { name: 'Sports',         p: .08, price: 900,  cost: .64, products: ['Yoga Mat', 'Dumbbell Set', 'Fitness Tracker', 'Water Bottle'] }
  ];
  var MONTH_F = [.92, .90, 1.02, .98, 1.00, .97, .95, .99, 1.05, 1.08, 1.45, 1.18];
  var DISC = [0, .05, .10, .15, .20];
  var DAY_MS = 864e5;
  var START = Date.UTC(2025, 0, 1);
  var END = Date.UTC(2026, 8, 30);
  var NDAYS = Math.round((END - START) / DAY_MS) + 1;

  function mulberry32(a) {
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      var t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  function buildData() {
    var rnd = mulberry32(2026);
    function gauss() {
      var u = 0, v = 0;
      while (!u) u = rnd();
      while (!v) v = rnd();
      return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
    }
    function cumOf(w) { var s = 0; return w.map(function (x) { return (s += x); }); }
    function pick(cum) { var x = rnd(); for (var i = 0; i < cum.length; i++) if (x < cum[i]) return i; return cum.length - 1; }

    var cCat = cumOf(CATS.map(function (c) { return c.p; }));
    var cReg = cumOf(REGIONS.map(function (r) { return r[1]; }));
    var cCh = cumOf(CHANNELS.map(function (c) { return c[1]; }));
    var cQty = cumOf([.70, .22, .08]);
    var cDisc = cumOf([.50, .20, .15, .10, .05]);

    var counts = new Uint16Array(NDAYS), total = 0;
    var blackFriday = Math.round((Date.UTC(2025, 10, 28) - START) / DAY_MS);
    for (var d = 0; d < NDAYS; d++) {
      var dt = new Date(START + d * DAY_MS), dow = dt.getUTCDay();
      var lam = 140 * (1 + .0011 * d) * MONTH_F[dt.getUTCMonth()] * ((dow === 5 || dow === 6) ? 1.25 : 1);
      if (d === blackFriday) lam *= 2.2;
      var c = Math.max(0, Math.round(lam + Math.sqrt(lam) * gauss()));
      counts[d] = c; total += c;
    }

    var o = {
      n: total,
      day: new Uint16Array(total), reg: new Uint8Array(total), ch: new Uint8Array(total),
      cat: new Uint8Array(total), prod: new Uint8Array(total), qty: new Uint8Array(total),
      rev: new Float32Array(total), profit: new Float32Array(total),
      dayStart: new Uint32Array(NDAYS + 1)
    };
    var k = 0;
    for (var day = 0; day < NDAYS; day++) {
      o.dayStart[day] = k;
      for (var j = 0; j < counts[day]; j++) {
        var ci = pick(cCat), m = CATS[ci];
        var price = Math.max(50, Math.round(m.price * Math.exp(.35 * gauss()) / 10) * 10);
        var q = pick(cQty) + 1, gross = price * q;
        var revenue = gross * (1 - DISC[pick(cDisc)]);
        o.day[k] = day; o.reg[k] = pick(cReg); o.ch[k] = pick(cCh);
        o.cat[k] = ci; o.prod[k] = Math.floor(rnd() * 4); o.qty[k] = q;
        o.rev[k] = revenue; o.profit[k] = revenue - gross * m.cost;
        k++;
      }
    }
    o.dayStart[NDAYS] = k;
    return o;
  }

  var DATA = buildData();

  /* ======================================================================
     2) AGGREGATION
     ====================================================================== */
  var state = { start: 0, end: NDAYS - 1, reg: all(REGIONS.length), ch: all(CHANNELS.length), cat: all(CATS.length) };
  function all(n) { var a = []; for (var i = 0; i < n; i++) a.push(1); return a; }

  function aggregate(s, e) {
    var D = DATA;
    var r = {
      rev: 0, profit: 0, orders: 0,
      dayRev: new Float64Array(NDAYS), dayProfit: new Float64Array(NDAYS),
      cat: new Float64Array(CATS.length), ch: new Float64Array(CHANNELS.length), reg: new Float64Array(REGIONS.length),
      pRev: new Float64Array(CATS.length * 4), pProfit: new Float64Array(CATS.length * 4), pQty: new Float64Array(CATS.length * 4)
    };
    if (s < 0) s = 0;
    if (e > NDAYS - 1) e = NDAYS - 1;
    if (e < s) return r;
    var from = D.dayStart[s], to = D.dayStart[e + 1];
    for (var i = from; i < to; i++) {
      if (!state.reg[D.reg[i]] || !state.ch[D.ch[i]] || !state.cat[D.cat[i]]) continue;
      var v = D.rev[i], p = D.profit[i], d = D.day[i], pi = D.cat[i] * 4 + D.prod[i];
      r.rev += v; r.profit += p; r.orders++;
      r.dayRev[d] += v; r.dayProfit[d] += p;
      r.cat[D.cat[i]] += v; r.ch[D.ch[i]] += v; r.reg[D.reg[i]] += v;
      r.pRev[pi] += v; r.pProfit[pi] += p; r.pQty[pi] += D.qty[i];
    }
    return r;
  }

  /* ======================================================================
     3) FORMATTING + TOOLTIP
     ====================================================================== */
  function fmtInt(n) { return Math.round(n).toLocaleString('en-US'); }
  function egp(x) {
    var a = Math.abs(x);
    if (a >= 1e6) return 'EGP ' + (x / 1e6).toFixed(2) + 'M';
    if (a >= 1e3) return 'EGP ' + (x / 1e3).toFixed(1) + 'K';
    return 'EGP ' + fmtInt(x);
  }
  function short(x) {
    var a = Math.abs(x);
    if (a >= 1e9) return (x / 1e9).toFixed(1).replace(/\.0$/, '') + 'B';
    if (a >= 1e6) return (x / 1e6).toFixed(1).replace(/\.0$/, '') + 'M';
    if (a >= 1e3) return (x / 1e3).toFixed(1).replace(/\.0$/, '') + 'K';
    return String(Math.round(x));
  }
  function dayDate(d) { return new Date(START + d * DAY_MS); }
  function lbl(d, year) {
    var dt = dayDate(d);
    return dt.getUTCDate() + ' ' + MON[dt.getUTCMonth()] + (year ? ' ' + dt.getUTCFullYear() : '');
  }
  function iso(d) { return dayDate(d).toISOString().slice(0, 10); }
  function parseIso(v) { return Math.round((Date.parse(v + 'T00:00:00Z') - START) / DAY_MS); }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;'); }

  var tipEl = document.getElementById('tip');
  var Tip = {
    show: function (html, x, y) {
      tipEl.innerHTML = html; tipEl.classList.add('on');
      var w = tipEl.offsetWidth, h = tipEl.offsetHeight;
      var px = x + 14, py = y + 14;
      if (px + w > window.innerWidth - 8) px = x - w - 14;
      if (py + h > window.innerHeight - 8) py = y - h - 14;
      tipEl.style.left = Math.max(8, px) + 'px'; tipEl.style.top = Math.max(8, py) + 'px';
    },
    hide: function () { tipEl.classList.remove('on'); }
  };
  document.addEventListener('mousemove', function (e) {
    var t = e.target.closest ? e.target.closest('[data-tip]') : null;
    if (t) Tip.show(t.getAttribute('data-tip'), e.clientX, e.clientY);
    else if (!e.target.closest || !e.target.closest('.ov')) Tip.hide();
  });

  /* ======================================================================
     4) SVG CHARTS
     ====================================================================== */
  var uid = 0;
  function niceScale(max, ticks) {
    var raw = max / ticks, p = Math.pow(10, Math.floor(Math.log10(raw))), f = raw / p;
    var step = (f <= 1 ? 1 : f <= 2 ? 2 : f <= 2.5 ? 2.5 : f <= 5 ? 5 : 10) * p;
    return { step: step, max: Math.ceil(max / step) * step };
  }
  function width(el) { return Math.max(280, Math.floor(el.clientWidth)); }

  function lineChart(el, o) {
    var W = width(el), H = o.height || 360, m = { l: 58, r: 16, t: 12, b: 30 };
    var pw = W - m.l - m.r, ph = H - m.t - m.b, n = o.labels.length;
    var maxV = 1; o.series.forEach(function (s) { s.values.forEach(function (v) { if (v > maxV) maxV = v; }); });
    var sc = niceScale(maxV, 4), gid = 'g' + (++uid);
    function x(i) { return m.l + (n <= 1 ? pw / 2 : i * pw / (n - 1)); }
    function y(v) { return m.t + ph - (v / sc.max) * ph; }

    var svg = '<svg width="' + W + '" height="' + H + '" viewBox="0 0 ' + W + ' ' + H + '">';
    svg += '<defs><linearGradient id="' + gid + '" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="' + o.series[0].color + '" stop-opacity=".35"/><stop offset="1" stop-color="' + o.series[0].color + '" stop-opacity="0"/></linearGradient></defs>';
    for (var v = 0; v <= sc.max + 1e-9; v += sc.step) {
      svg += '<line x1="' + m.l + '" x2="' + (W - m.r) + '" y1="' + y(v) + '" y2="' + y(v) + '" stroke="rgba(255,255,255,.08)"/>';
      svg += '<text x="' + (m.l - 8) + '" y="' + (y(v) + 4) + '" text-anchor="end" font-size="11" fill="rgba(230,237,247,.6)">' + short(v) + '</text>';
    }
    var cnt = Math.max(2, Math.min(n, Math.floor(pw / 95)));
    for (var t = 0; t < cnt; t++) {
      var idx = Math.round(t * (n - 1) / (cnt - 1));
      svg += '<text x="' + x(idx) + '" y="' + (H - 8) + '" text-anchor="middle" font-size="11" fill="rgba(230,237,247,.6)">' + o.labels[idx] + '</text>';
    }
    o.series.forEach(function (s, si) {
      var pts = s.values.map(function (val, i) { return x(i).toFixed(1) + ',' + y(val).toFixed(1); });
      if (si === 0) svg += '<path d="M' + pts.join('L') + 'L' + x(n - 1) + ',' + y(0) + 'L' + x(0) + ',' + y(0) + 'Z" fill="url(#' + gid + ')"/>';
      svg += '<path d="M' + pts.join('L') + '" fill="none" stroke="' + s.color + '" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>';
    });
    svg += '<line class="guide" y1="' + m.t + '" y2="' + (m.t + ph) + '" stroke="rgba(255,255,255,.35)" stroke-dasharray="4 3" style="display:none"/>';
    o.series.forEach(function (s, si) { svg += '<circle class="dot' + si + '" r="4.5" fill="' + s.color + '" stroke="#0a0f1a" stroke-width="2" style="display:none"/>'; });
    svg += '<rect class="ov" x="' + m.l + '" y="' + m.t + '" width="' + pw + '" height="' + ph + '" fill="transparent"/></svg>';

    var legend = '<div class="legend">' + o.series.map(function (s) { return '<span><i style="background:' + s.color + '"></i>' + s.name + '</span>'; }).join('') + '</div>';
    el.innerHTML = legend + svg;

    var root = el.querySelector('svg'), ov = el.querySelector('.ov'), guide = el.querySelector('.guide');
    var dots = o.series.map(function (s, si) { return el.querySelector('.dot' + si); });
    ov.addEventListener('mousemove', function (e) {
      var rect = root.getBoundingClientRect();
      var i = Math.round(((e.clientX - rect.left) - m.l) / pw * (n - 1));
      i = Math.max(0, Math.min(n - 1, i));
      guide.setAttribute('x1', x(i)); guide.setAttribute('x2', x(i)); guide.style.display = '';
      var html = '<b>' + o.tipLabels[i] + '</b>';
      o.series.forEach(function (s, si) {
        dots[si].setAttribute('cx', x(i)); dots[si].setAttribute('cy', y(s.values[i])); dots[si].style.display = '';
        html += '<br><i style="background:' + s.color + '"></i>' + s.name + ': <b>' + egp(s.values[i]) + '</b>';
      });
      Tip.show(html, e.clientX, e.clientY);
    });
    ov.addEventListener('mouseleave', function () {
      guide.style.display = 'none'; dots.forEach(function (d) { d.style.display = 'none'; }); Tip.hide();
    });
  }

  function barH(el, items, color) {
    var W = width(el), rowH = 52, labelW = Math.min(130, W * .34), valW = 58, H = items.length * rowH + 6;
    var max = 1; items.forEach(function (it) { if (it.value > max) max = it.value; });
    var mw = Math.max(40, W - labelW - valW);
    var svg = '<svg width="' + W + '" height="' + H + '" viewBox="0 0 ' + W + ' ' + H + '">';
    items.forEach(function (it, i) {
      var yy = i * rowH + 4, bw = Math.max(3, it.value / max * mw);
      var tip = esc('<b>' + it.label + '</b><br>Revenue: <b>' + egp(it.value) + '</b><br>' + it.pct + '% of total');
      svg += '<g data-tip="' + tip + '">';
      svg += '<rect x="0" y="' + yy + '" width="' + W + '" height="' + (rowH - 4) + '" fill="transparent"/>';
      svg += '<text x="0" y="' + (yy + 21) + '" font-size="13" fill="#cbd5e1">' + esc(it.label) + '</text>';
      svg += '<rect x="' + labelW + '" y="' + (yy + 6) + '" width="' + bw + '" height="22" rx="5" fill="' + color + '"/>';
      svg += '<text x="' + (labelW + bw + 8) + '" y="' + (yy + 22) + '" font-size="12" fill="rgba(230,237,247,.85)">' + short(it.value) + '</text></g>';
    });
    el.innerHTML = svg + '</svg>';
  }

  function barV(el, items, color) {
    var W = width(el), H = 340, m = { l: 48, r: 8, t: 26, b: 52 };
    var pw = W - m.l - m.r, ph = H - m.t - m.b, n = items.length;
    var max = 1; items.forEach(function (it) { if (it.value > max) max = it.value; });
    var sc = niceScale(max, 4), slot = pw / n, bw = Math.min(64, slot * .62);
    function y(v) { return m.t + ph - (v / sc.max) * ph; }
    var svg = '<svg width="' + W + '" height="' + H + '" viewBox="0 0 ' + W + ' ' + H + '">';
    for (var v = 0; v <= sc.max + 1e-9; v += sc.step) {
      svg += '<line x1="' + m.l + '" x2="' + (W - m.r) + '" y1="' + y(v) + '" y2="' + y(v) + '" stroke="rgba(255,255,255,.08)"/>';
      svg += '<text x="' + (m.l - 8) + '" y="' + (y(v) + 4) + '" text-anchor="end" font-size="11" fill="rgba(230,237,247,.6)">' + short(v) + '</text>';
    }
    items.forEach(function (it, i) {
      var cx = m.l + slot * i + slot / 2, top = y(it.value);
      var tip = esc('<b>' + it.label + '</b><br>Revenue: <b>' + egp(it.value) + '</b><br>' + it.pct + '% of total');
      svg += '<g data-tip="' + tip + '"><rect x="' + (cx - slot / 2) + '" y="' + m.t + '" width="' + slot + '" height="' + (ph + m.b) + '" fill="transparent"/>';
      svg += '<rect x="' + (cx - bw / 2) + '" y="' + top + '" width="' + bw + '" height="' + Math.max(0, m.t + ph - top) + '" rx="5" fill="' + color + '"/>';
      svg += '<text x="' + cx + '" y="' + (top - 7) + '" text-anchor="middle" font-size="12" fill="rgba(230,237,247,.85)">' + short(it.value) + '</text>';
      var words = it.label.split(' ');
      svg += '<text text-anchor="middle" font-size="12" fill="#cbd5e1"><tspan x="' + cx + '" y="' + (H - 30) + '">' + esc(words[0]) + '</tspan>' +
             (words[1] ? '<tspan x="' + cx + '" y="' + (H - 15) + '">' + esc(words.slice(1).join(' ')) + '</tspan>' : '') + '</text></g>';
    });
    el.innerHTML = svg + '</svg>';
  }

  function donut(el, items) {
    var S = 210, cx = S / 2, cy = S / 2, r = 76, sw = 32, circ = 2 * Math.PI * r;
    var total = items.reduce(function (a, b) { return a + b.value; }, 0) || 1, off = 0;
    var svg = '<svg width="' + S + '" height="' + S + '" viewBox="0 0 ' + S + ' ' + S + '">';
    items.forEach(function (it, i) {
      var len = it.value / total * circ, col = PALETTE[i % PALETTE.length];
      var tip = esc('<b>' + it.label + '</b><br>Revenue: <b>' + egp(it.value) + '</b><br>' + (it.value / total * 100).toFixed(1) + '% of total');
      svg += '<circle data-tip="' + tip + '" cx="' + cx + '" cy="' + cy + '" r="' + r + '" fill="none" stroke="' + col + '" stroke-width="' + sw +
             '" stroke-dasharray="' + Math.max(0, len - 2) + ' ' + (circ - Math.max(0, len - 2)) + '" stroke-dashoffset="' + (-off) + '" transform="rotate(-90 ' + cx + ' ' + cy + ')"/>';
      off += len;
    });
    svg += '<text x="' + cx + '" y="' + (cy + 2) + '" text-anchor="middle" font-size="24" font-weight="800" fill="#fff">' + short(total) + '</text>';
    svg += '<text x="' + cx + '" y="' + (cy + 22) + '" text-anchor="middle" font-size="12" fill="rgba(230,237,247,.6)">EGP revenue</text></svg>';
    var legend = '<div class="donut-legend">' + items.map(function (it, i) {
      return '<div><i style="background:' + PALETTE[i % PALETTE.length] + '"></i>' + esc(it.label) + '<b>' + (it.value / total * 100).toFixed(1) + '%</b></div>';
    }).join('') + '</div>';
    el.innerHTML = '<div class="donut-wrap">' + svg + legend + '</div>';
  }

  /* ======================================================================
     5) RENDER
     ====================================================================== */
  var $ = function (id) { return document.getElementById(id); };
  var last = null;

  function setDelta(id, cur, prev, ok, isPp) {
    var el = $(id);
    if (!ok) { el.textContent = 'vs previous period: n/a'; el.className = 'delta flat'; return; }
    var diff = isPp ? (cur - prev) * 100 : (prev ? (cur - prev) / prev * 100 : 0);
    var up = diff > 0.05, down = diff < -0.05;
    el.className = 'delta ' + (up ? 'up' : down ? 'down' : 'flat');
    el.textContent = (up ? '▲ ' : down ? '▼ ' : '● ') + (diff >= 0 ? '+' : '') + diff.toFixed(1) + (isPp ? ' pp' : '%');
  }

  function render() {
    var s = state.start, e = state.end, len = e - s + 1;
    var cur = aggregate(s, e);
    var ps = s - len, pe = s - 1;
    var prevOk = ps >= 0;
    var prev = prevOk ? aggregate(ps, pe) : null;

    $('range').textContent = lbl(s, true) + ' – ' + lbl(e, true) + (prevOk ? ' · compared with the previous ' + len + ' days' : ' · previous period is outside the data range');
    $('empty').hidden = cur.orders > 0;
    $('content').hidden = cur.orders === 0;
    if (cur.orders === 0) return;

    var aov = cur.rev / cur.orders, mar = cur.profit / cur.rev;
    $('k-rev').textContent = egp(cur.rev);
    $('k-ord').textContent = fmtInt(cur.orders);
    $('k-aov').textContent = 'EGP ' + fmtInt(aov);
    $('k-mar').textContent = (mar * 100).toFixed(1) + '%';
    var okP = prevOk && prev.orders > 0;
    setDelta('d-rev', cur.rev, okP && prev.rev, okP);
    setDelta('d-ord', cur.orders, okP && prev.orders, okP);
    setDelta('d-aov', aov, okP && prev.rev / prev.orders, okP);
    setDelta('d-mar', mar, okP && prev.profit / prev.rev, okP, true);

    // Trend: daily up to 90 days, otherwise full 7-day buckets.
    var labels = [], tipLabels = [], rv = [], pf = [];
    if (len <= 90) {
      for (var d = s; d <= e; d++) { labels.push(lbl(d)); tipLabels.push(lbl(d, true)); rv.push(cur.dayRev[d]); pf.push(cur.dayProfit[d]); }
    } else {
      for (var b = s; b + 6 <= e; b += 7) {
        var a = 0, p = 0;
        for (var k = b; k < b + 7; k++) { a += cur.dayRev[k]; p += cur.dayProfit[k]; }
        labels.push(lbl(b)); tipLabels.push('Week of ' + lbl(b, true)); rv.push(a); pf.push(p);
      }
    }
    var series = [{ name: 'Revenue', color: C.teal, values: rv }, { name: 'Profit', color: C.amber, values: pf }];
    last = { cur: cur, trend: { labels: labels, tipLabels: tipLabels, series: series } };
    drawCharts();

    // Top products table
    var rows = [];
    for (var i = 0; i < CATS.length * 4; i++) {
      if (cur.pRev[i] > 0) rows.push({ product: CATS[Math.floor(i / 4)].products[i % 4], cat: CATS[Math.floor(i / 4)].name, units: cur.pQty[i], rev: cur.pRev[i], margin: cur.pProfit[i] / cur.pRev[i] * 100 });
    }
    rows.sort(function (x, y) { return y.rev - x.rev; });
    rows = rows.slice(0, 8);
    var mx = rows.length ? rows[0].rev : 1;
    $('tbl').innerHTML = '<table class="tbl"><thead><tr><th>Product</th><th>Category</th><th class="num">Units</th><th>Revenue (EGP)</th><th class="num">Margin</th></tr></thead><tbody>' +
      rows.map(function (r) {
        return '<tr><td>' + esc(r.product) + '</td><td class="muted">' + esc(r.cat) + '</td><td class="num">' + fmtInt(r.units) + '</td>' +
          '<td class="bar-cell"><div class="fill" style="width:' + (r.rev / mx * 100).toFixed(1) + '%"></div><span>' + fmtInt(r.rev) + '</span></td>' +
          '<td class="num">' + r.margin.toFixed(1) + '%</td></tr>';
      }).join('') + '</tbody></table>';
  }

  function drawCharts() {
    if (!last) return;
    var cur = last.cur;
    lineChart($('ch-trend'), { labels: last.trend.labels, tipLabels: last.trend.tipLabels, series: last.trend.series, height: 360 });

    function items(names, vals) {
      var tot = 0; for (var i = 0; i < vals.length; i++) tot += vals[i];
      return names.map(function (n, i) { return { label: n, value: vals[i], pct: tot ? (vals[i] / tot * 100).toFixed(1) : '0.0' }; })
        .filter(function (x) { return x.value > 0; })
        .sort(function (a, b) { return b.value - a.value; });
    }
    barH($('ch-cat'), items(CATS.map(function (c) { return c.name; }), cur.cat), C.indigo);
    donut($('ch-chan'), items(CHANNELS.map(function (c) { return c[0]; }), cur.ch));
    barV($('ch-reg'), items(REGIONS.map(function (r) { return r[0]; }), cur.reg), C.teal);
  }

  var rt; window.addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(drawCharts, 120); });

  /* ======================================================================
     6) FILTERS
     ====================================================================== */
  var startEl = $('f-start'), endEl = $('f-end');
  startEl.min = endEl.min = iso(0); startEl.max = endEl.max = iso(NDAYS - 1);

  function syncDates() { startEl.value = iso(state.start); endEl.value = iso(state.end); }
  function markPresets() {
    var len = state.end - state.start + 1, atEnd = state.end === NDAYS - 1;
    document.querySelectorAll('#presets .pill').forEach(function (b) {
      var d = +b.getAttribute('data-days');
      var on = d === 0 ? (state.start === 0 && atEnd) : (atEnd && len === d);
      b.classList.toggle('on', on);
    });
  }
  function setRange(s, e) {
    state.start = Math.max(0, Math.min(NDAYS - 1, s));
    state.end = Math.max(state.start, Math.min(NDAYS - 1, e));
    syncDates(); markPresets(); render();
  }

  document.querySelectorAll('#presets .pill').forEach(function (b) {
    b.addEventListener('click', function () {
      var d = +b.getAttribute('data-days');
      setRange(d === 0 ? 0 : NDAYS - d, NDAYS - 1);
    });
  });
  startEl.addEventListener('change', function () { if (startEl.value) setRange(parseIso(startEl.value), Math.max(state.end, parseIso(startEl.value))); });
  endEl.addEventListener('change', function () { if (endEl.value) setRange(Math.min(state.start, parseIso(endEl.value)), parseIso(endEl.value)); });

  function chipGroup(id, names, key) {
    var box = $(id);
    box.innerHTML = '';
    names.forEach(function (n, i) {
      var b = document.createElement('button');
      b.className = 'pill on'; b.type = 'button'; b.textContent = n;
      b.addEventListener('click', function () {
        state[key][i] = state[key][i] ? 0 : 1;
        b.classList.toggle('on', !!state[key][i]);
        render();
      });
      box.appendChild(b);
    });
  }
  chipGroup('f-region', REGIONS.map(function (r) { return r[0]; }), 'reg');
  chipGroup('f-cat', CATS.map(function (c) { return c.name; }), 'cat');
  chipGroup('f-chan', CHANNELS.map(function (c) { return c[0]; }), 'ch');

  $('reset').addEventListener('click', function () {
    state.reg = all(REGIONS.length); state.cat = all(CATS.length); state.ch = all(CHANNELS.length);
    document.querySelectorAll('#f-region .pill, #f-cat .pill, #f-chan .pill').forEach(function (b) { b.classList.add('on'); });
    setRange(NDAYS - 180, NDAYS - 1);
  });

  /* ---------- CSV export (filtered rows for the selected range) ---------- */
  $('csv').addEventListener('click', function () {
    var D = DATA, out = ['order_id,date,region,channel,category,product,qty,revenue,profit'];
    for (var i = D.dayStart[state.start]; i < D.dayStart[state.end + 1]; i++) {
      if (!state.reg[D.reg[i]] || !state.ch[D.ch[i]] || !state.cat[D.cat[i]]) continue;
      var c = CATS[D.cat[i]];
      out.push([100000 + i, iso(D.day[i]), REGIONS[D.reg[i]][0], CHANNELS[D.ch[i]][0], '"' + c.name + '"', c.products[D.prod[i]], D.qty[i], D.rev[i].toFixed(2), D.profit[i].toFixed(2)].join(','));
    }
    var blob = new Blob([out.join('\n')], { type: 'text/csv' });
    var a = document.createElement('a');
    a.href = URL.createObjectURL(blob); a.download = 'filtered_orders.csv';
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(function () { URL.revokeObjectURL(a.href); }, 1000);
  });

  // Default view: the last 180 days.
  setRange(NDAYS - 180, NDAYS - 1);

  // Exposed for quick checks in the browser console.
  window.__dash = { rows: DATA.n, aggregate: aggregate };
})();
