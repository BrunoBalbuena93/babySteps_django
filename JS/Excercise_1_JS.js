var fullname = prompt("¿Cual es tu nombre? ");
var name = fullname.substring(0, fullname.indexOf(" "));
var last = fullname.substring(fullname.indexOf(" ") + 1)
var age = parseInt(prompt("¿Cual es tu edad?"));
var height = parseFloat(prompt("¿Cual es tu estatura?"));
var pet = prompt("¿Y el nombre de tu mascota?");
/* Condiciones para que sea espía:
+ El nombre y apellido comienzan con la misma letra
+ La edad entre 20 y 30
+ La estaturo de al menos 1.70
+ La mascota termina con y */
if(name[0] == last[0] && age >= 20 && age <= 30 && height >= 1.7 && pet[pet.length-1] == "y")
{
    console.log("Felicidades, eres un espía");
}
