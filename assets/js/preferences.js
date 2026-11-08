// Aplica as preferências guardadas ao <html> antes da primeira pintura.
// Guardadas em localStorage (chave "oce-prefs"), nunca enviadas a ninguém:
// o site não tem cookies, análise nem servidor próprio.
(function () {
  var prefs = {};
  try { prefs = JSON.parse(localStorage.getItem('oce-prefs')) || {}; } catch (e) {}
  var h = document.documentElement;
  var theme = prefs.theme === 'light' || prefs.theme === 'dark' ? prefs.theme : 'auto';
  h.setAttribute('data-theme', theme);
  if (prefs.cvd === true) h.setAttribute('data-cvd', '');
  if (prefs.contrast === true) h.setAttribute('data-contrast', '');
  if (prefs.large === true) h.setAttribute('data-large', '');
})();
