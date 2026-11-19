/* Shared behaviour: mobile menu, active menu item while scrolling, optional images, lightbox. */
(function () {
  'use strict';

  // ---- Mobile menu --------------------------------------------------------
  var btn = document.querySelector('.menu-btn');
  var overlay = document.querySelector('.overlay');
  function setNav(open) { document.body.classList.toggle('nav-open', open); }
  if (btn) btn.addEventListener('click', function () { setNav(!document.body.classList.contains('nav-open')); });
  if (overlay) overlay.addEventListener('click', function () { setNav(false); });
  document.querySelectorAll('.sidebar a').forEach(function (a) {
    a.addEventListener('click', function () { setNav(false); });
  });

  // ---- Highlight the menu item of the section being read -------------------
  var links = Array.prototype.slice.call(document.querySelectorAll('.nav a[href^="#"]'));
  function setActive(id) {
    links.forEach(function (a) { a.classList.toggle('active', a.getAttribute('href') === '#' + id); });
  }
  if ('IntersectionObserver' in window) {
    var visible = {};
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { visible[e.target.id] = e.isIntersecting; });
      var order = links.map(function (a) { return a.getAttribute('href').slice(1); });
      for (var i = 0; i < order.length; i++) {
        if (visible[order[i]]) { setActive(order[i]); return; }
      }
    }, { rootMargin: '-15% 0px -60% 0px' });
    function observeAll() {
      links.forEach(function (a) {
        var el = document.getElementById(a.getAttribute('href').slice(1));
        if (el) io.observe(el);
      });
    }
    observeAll();
  }
  if (links.length) setActive(links[0].getAttribute('href').slice(1));

  // ---- Optional images ----------------------------------------------------
  // <img data-img="profile"> looks for assets/profile.(jpg|png|jpeg|webp), then the same names in the
  // site root. If nothing is found the element is hidden (or its card removed when inside [data-card]).
  var EXT = ['jpg', 'png', 'jpeg', 'webp'];
  function candidates(stem) {
    var out = [];
    ['assets/', ''].forEach(function (dir) {
      EXT.forEach(function (e) { out.push(dir + stem + '.' + e); });
    });
    return out;
  }
  function firstThatLoads(list) {
    return new Promise(function (resolve) {
      var i = 0;
      (function next() {
        if (i >= list.length) return resolve(null);
        var im = new Image();
        im.onload = function () { resolve(list[i]); };
        im.onerror = function () { i++; next(); };
        im.src = list[i];
      })();
    });
  }

  var imgs = Array.prototype.slice.call(document.querySelectorAll('img[data-img]'));
  Promise.all(imgs.map(function (el) {
    return firstThatLoads(candidates(el.getAttribute('data-img'))).then(function (src) {
      if (src) {
        el.src = src;
        el.hidden = false;
      } else {
        var card = el.closest('[data-card]');
        if (card) card.remove();
      }
    });
  })).then(function () {
    // No screenshots found: remove the whole gallery section and its menu link.
    var gallery = document.getElementById('dashboards');
    if (gallery && !gallery.querySelector('[data-card]')) {
      gallery.remove();
      document.querySelectorAll('[data-for="dashboards"]').forEach(function (a) { a.remove(); });
    }
  });

  // ---- Lightbox for screenshots --------------------------------------------
  document.addEventListener('click', function (e) {
    var t = e.target;
    if (!(t instanceof HTMLImageElement) || !t.closest('.gcard')) return;
    var box = document.createElement('div');
    box.className = 'lightbox';
    box.innerHTML = '<img alt="">';
    box.firstChild.src = t.src;
    box.addEventListener('click', function () { box.remove(); });
    document.addEventListener('keydown', function esc(ev) {
      if (ev.key === 'Escape') { box.remove(); document.removeEventListener('keydown', esc); }
    });
    document.body.appendChild(box);
  });
})();
