/* Shared behaviour: mobile menu, optional images (profile + dashboard screenshots), lightbox. */
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

  // ---- Optional images ----------------------------------------------------
  // <img data-img="profile"> looks for assets/profile.(png|jpg|jpeg|webp), then the same names in the
  // site root. If nothing is found the element is hidden (or its card removed when data-card is set).
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
    // Remove the whole gallery section (and its menu link) when no screenshot was found.
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
