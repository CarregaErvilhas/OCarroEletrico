// Liga o painel "Aparência e acessibilidade" às preferências.
(function () {
  var KEY = 'oce-prefs';
  var h = document.documentElement;
  var form = document.querySelector('#prefs form');
  if (!form) return;

  function read() {
    try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { return {}; }
  }
  function write(p) {
    try { localStorage.setItem(KEY, JSON.stringify(p)); } catch (e) {}
  }
  function apply(p) {
    var t = p.theme === 'light' || p.theme === 'dark' ? p.theme : 'auto';
    h.setAttribute('data-theme', t);
    ['cvd', 'contrast', 'large'].forEach(function (k) {
      if (p[k] === true) h.setAttribute('data-' + k, ''); else h.removeAttribute('data-' + k);
    });
  }
  function sync(p) {
    var t = p.theme === 'light' || p.theme === 'dark' ? p.theme : 'auto';
    form.elements.theme.value = t;
    ['cvd', 'contrast', 'large'].forEach(function (k) { form.elements[k].checked = p[k] === true; });
  }

  sync(read());
  form.addEventListener('change', function () {
    var p = {
      theme: form.elements.theme.value,
      cvd: form.elements.cvd.checked,
      contrast: form.elements.contrast.checked,
      large: form.elements.large.checked
    };
    write(p);
    apply(p);
  });
  form.addEventListener('submit', function (e) { e.preventDefault(); });
  document.getElementById('prefs-reset').addEventListener('click', function () {
    try { localStorage.removeItem(KEY); } catch (e) {}
    apply({}); sync({});
  });
  document.addEventListener('keydown', function (e) {
    var d = document.getElementById('prefs');
    if (e.key === 'Escape' && d.open) { d.open = false; d.querySelector('summary').focus(); }
  });
})();
