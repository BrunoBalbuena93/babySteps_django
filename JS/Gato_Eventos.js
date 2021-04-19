var restart = document.querySelector("#b")
var counter = [0, 0, 0, 0, 0, 0, 0, 0, 0]
var values = [" ", "X", "O"]
var squares = document.querySelectorAll("td");

// Clear board
function ClearBoard(){
    for( var i=0; i< squares.length; i++){
        squares[i].textContent = " ";
    }
}

restart.addEventListener("click", ClearBoard);
// Botones superiores

function ChangeMarker()
{
    if(this.textContent === ""){ this.textContent = "X"; }
    else if(this.textContent === "X"){ this.textContent = "O"; }
    else{ this.textContent = ""; }
}

for(var i=0;i<squares.length;i++){
    squares[i].addEventListener("click", ChangeMarker)
}

