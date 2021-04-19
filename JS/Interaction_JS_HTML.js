// Primero sacaremos el encabezado del documento:
var HH = document.querySelector("#one")
var CH = document.querySelector("#two")
var DCH = document.querySelector("#three")
var n = 0;
var m = 0;
// Haremos una función que genere colores aleatorios
function getRandomColor(){
    var letters = "0123456789ABCDEF";
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random()*16)];
    }
    return color
}

  // Ahora una función que cambie de color el header
function UpdateHeader(header){
    header.style.color = getRandomColor();
}

  // Haciendo que suceda cada 500 ms
//   setInterval("UpdateHeader()", 500)

// Colocando los listeners de eventos
// Evento mouseover: cuando el mouse esta encima del objeto
HH.addEventListener("mouseover", function(){
    HH.textContent = "El mouse está encima del Header";
    UpdateHeader(HH);
})
// Evento mouseout: El mouse deja de estar encima del objeto
HH.addEventListener("mouseout", function(){
    HH.textContent = "This is a Hover Header";
    HH.style.color = "black";
})

CH.addEventListener("click", function(){
    n++;
    CH.textContent = "Lo has clickeado " + n.toString() + " veces";
    UpdateHeader(CH)
})

DCH.addEventListener("dblclick", function(){
    m++;
    DCH.textContent = "Lo has dobleclickeado " + m.toString() + " veces";
    UpdateHeader(DCH)
})