function tolt() {
  setInterval(ido_lekerdezes, 1000);
}
function ido_lekerdezes() {
  var datumido = new Date();
  var nap = datumido.getDate();
  var honap = datumido.getMonth();
  var ev = datumido.getFullYear();
  var ora = datumido.getHours();
  var perc = datumido.getMinutes();
  var mp = datumido.getSeconds();
  document.getElementsByClassName('pontosido').innerHTML = ev + "." + honap + "." + nap + "." + ora + "." + perc + "." + mp;
}
function bekuldes() {
  var nev = document.getElementsByClassName('nev_mezo').value;
  var uzenet = document.getElementsByClassName('uzenet_mezo').value;
  var datumido = new Date();
  var ora = datumido.getHours();
  var perc = datumido.getMinutes();
  var mp = datumido.getSeconds();
  document.getElementsByClassName('cseveges_mezo').value += nev + "[" + ora + ":" + perc + ":" + mp + "]" + ": " + uzenet + "\n";
  alert('Üzenet elküldve!');
}
