function osszead() {
  var elso_szam = document.getElementById("szam_1").value;
  var masodik_szam = document.getElementById("szam_2").value;
  var eredmeny = +elso_szam + +masodik_szam;
  document.getElementById("vegeredmeny").innerHTML = eredmeny;
}
