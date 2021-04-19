// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []
var keepWorking = false;
// Create the functions for the tasks
while(keepWorking){
    var action = prompt("Que acción deseas? add (a), remove (r), display (d), quit (q)");
    switch(action){
        case "a":
            roster.push(prompt("Nombre a agregar: "))
            break;
        case "r":
            var temp = prompt("Nombre a quitar");
            if(roster.indexOf(temp) > -1)
            {
                roster.splice(roster.indexOf(temp), 1);
            }
            break;
        case "d":
            console.log(roster)
            break;
        default:
            keepWorking = false;
    }
}

// Mas ejercicios
////////////////////
// PROBLEM 1 //////
//////////////////

// Given the object:
var employee = {
    name: "John Smith",
    job: "Programmer",
    age: 31
  }
  
  // Add a method called nameLength that prints out the
  // length of the employees name to the console.
  employee["nameLength"] = function(){
      console.log(this.name.length)
  }
  
  ///////////////////
  // PROBLEM 2 /////
  /////////////////
  
  // Given the object:
  var employee = {
    name: "John Smith",
    job: "Programmer",
    age: 31
  }

  employee["alert"] = function(){
      for(key in this){
          if(key != "alert")
          {
              alert(key + " es " + this[key])
            }
      }
  }
  
  // Write program that will create an Alert in the browser of each of the
  // object's values for the key value pairs. For example, it should alert:
  
  // Name is John Smith, Job is Programmer, Age is 31.
  
  
  
  ///////////////////
  // PROBLEM 3 /////
  /////////////////
  
  // Given the object:
  var employee = {
    name: "John Smith",
    job: "Programmer",
    age: 31
  }
  
  // Add a method called lastName that prints
  // out the employee's last name to the console.