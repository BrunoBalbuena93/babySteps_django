// Haciendo click
$("p").click(function(){
    $(this).text("Hiciste click sobre mi")
})

// Doble click
$('h1').on("dblclick", function(){
    $(this).toggleClass("turnBlue");
})

// Key presses
$("input").eq(0).keypress(function(event){
    $('h3').toggleClass("turnBlue")
    console.log(event)
})

// Una animación 
$('input').eq(1).on("click", function(){
    $('.container').fadeOut(3000)
})