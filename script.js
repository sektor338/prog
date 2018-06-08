function cserel(){
	document.getElementById("egy").style.background = "rgb(150, 150, 150)";
	next();
setInterval("next()", 15000);



}
function next(){
	setTimeout("ketto()", 5000);
setTimeout("harom()", 10000);
setTimeout("egy()", 15000);
}
function egy(){
	document.getElementById("harmadik").style.opacity = "0";
	document.getElementById("masodik").style.opacity = "0";
	document.getElementById("elso").style.opacity = "1";
	document.getElementById("egy").style.background = "rgb(150, 150, 150)";
	document.getElementById("ketto").style.background = "rgb(255, 255, 255)";
	document.getElementById("harom").style.background = "rgb(255, 255, 255)";
}
function ketto(){
	document.getElementById("harmadik").style.opacity = "0";
	document.getElementById("masodik").style.opacity = "1";
	document.getElementById("elso").style.opacity = "0";
	document.getElementById("egy").style.background = "rgb(255, 255, 255)";
	document.getElementById("ketto").style.background = "rgb(150, 150, 150)";
	document.getElementById("harom").style.background = "rgb(255, 255, 255)";
}

function harom(){
	document.getElementById("harmadik").style.opacity = "1";
	document.getElementById("masodik").style.opacity = "0";
	document.getElementById("elso").style.opacity = "0";
	document.getElementById("egy").style.background = "rgb(255, 255, 255)";
	document.getElementById("ketto").style.background = "rgb(255, 255, 255)";
	document.getElementById("harom").style.background = "rgb(150, 150, 150)";
}
