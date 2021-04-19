// Primero solicitamos los jugadores
var P1 = prompt("Nombre del jugador azul:");
var P2 = prompt("Nombre del jugador rojo: ");
// Diciendo de quien es turno
var turnP1 = true;
// Todos los puntos
var plays = $(".dot")
// Donde ha tirado el jugador 1
var turnsP1 = []
// Donde ha tirado el jugador 2
var turnsP2 = []
// Texto a mostrar
var texto;
// Index del circulo tocado
var index;
// Color, temporal también
var color;
var row = 5;
var temp = 0;
var found = false;
// finish game
var endGame = false

function FindIndex(obj){
    for(var idx=0;idx<plays.length;idx++){
        if(obj[0] === plays.eq(idx).get(0)){
            return idx
        }
    }
}

function HasWon(turns){
    if(turns.length < 4){ return false;}
    var a, step;
    // Vamos haciendo redes
    // Horizontal
    for(var cols=0;cols<4;cols++)
    {
        // corre del inicio a una antes de la ultima
        for(var rows=0; rows<6;rows++){
            a = rows * 7 + cols
            if(turns.includes(a) && turns.includes(a + 1) && turns.includes(a + 2) && turns.includes(a + 3))
            {return true}
        }
    }
    // Vertical
    for(var cols=0; cols<7;cols++)
    {
        for(var rows=0;rows<4;rows++)
        {
            a = cols + rows * 7
            if(turns.includes(a) && turns.includes(a + 7) && turns.includes(a + 14) && turns.includes(a + 21))
            { return true; }
        }
    }
    // Diagonales
    for(var cols=0;cols<4;cols++){
        for(var rows=0;rows<4;rows++){
            a = rows * 7 + cols
            if(turns.includes(a) && turns.includes(a + 8) && turns.includes(a + 16) && turns.includes(a + 24))
            {return true;}
        }
    }

    for(var cols=3;cols<7;cols++){
        for(var rows=0;rows<7;rows++){
            a = rows * 7 + cols
            if(turns.includes(a) && turns.includes(a + 6) && turns.includes(a + 12) && turns.includes(a + 18))
            {return true;}
        }
    }


    return false
}


$(".dot").click(function(){
    if(endGame){ return ;}
    // Primero definimos el color dependiendo del turno
    color = (turnP1) ? "#0e1eac": "#ac0e0e";
    // Ahora el texto
    texto = (turnP1) ? P1 + ", es tu turno":P2 + ", es tu turno";
    $("h3").text(texto);
    // Ahora definimos el index y con eso la columna
    index = FindIndex($(this))
    row = 5
    while(!found){
        // Buscamos si está ocupado abajo
        temp = 7 * row + index; 
        if(!turnsP1.includes(temp) && !turnsP2.includes(temp)){
            found = true
            plays.eq(temp).css("background-color", color)
            if(turnP1){ 
                turnsP1.push(temp)
                endGame = HasWon(turnsP1)
            }
            else{
                turnsP2.push(temp)
                endGame = HasWon(turnsP2)
            }
        }
        row--;
    }
    found = false
    if(endGame){
        texto = (turnP1) ? "Ha ganado " + P1 : "Ha ganado " + P2 
        $("h3").text(texto + ", actualiza para reiniciar")

    }
    // Por ultimo, cambiamos el turno
    turnP1 = !turnP1
    })

