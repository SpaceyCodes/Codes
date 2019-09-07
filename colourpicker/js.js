var x = 0;
var robotchoice = 0;
var score = 0;
const startingbutton = document.getElementById("action-message");
const lime = document.getElementById("lime");
const purple = document.getElementById("purple");
const orange = document.getElementById("orange");
const yellow = document.getElementById("yellow");
const red = document.getElementById("red");
const aquablue = document.getElementById("aquablue");
const lightgreen = document.getElementById("lightgreen");
const brightpurple = document.getElementById("brightpurple");
const brown = document.getElementById("brown");
const result = document.querySelector(".result > p");

function workerstarter() {
    w.addEventListener("message", function() {
        if (x == 0) {
            result.innerHTML = 3;
        } else if (x == 1000) {
            result.innerHTML = 2;
        } else if (x == 2000) {
            result.innerHTML = 1;
        } else if (x == 3000) {
            result.innerHTML = "GO";
        } else if (x == 3100) {
            starterbutton();
            robot();
        } else if (x == 20000) {
            result.innerHTML = `${score}/10 score | ${x}ms`;
        }
        if (score == 10) {
            w.terminate();
            result.innerHTML = `${score}/10 score | ${x}ms`;
        }
        x = x + 5;
    })
}
function robot() {
    robotchoice = Math.floor(Math.random() * 10);
    if (robotchoice == 0) {
        result.style.background = "#ddf796";
        robotchoice = "lime";
    } else if (robotchoice == 1) {
        result.style.background = "#b18ea6";
        robotchoice = "purple";
    } else if (robotchoice == 2) {
        result.style.background = "#b6ffea";
        robotchoice = "aquablue";
    } else if (robotchoice == 3) {
        result.style.background = "#f1f0cf";
        robotchoice = "yellow";
    } else if (robotchoice == 4) {
        result.style.background = "#ffc5a1";
        robotchoice = "orange";
    } else if (robotchoice == 5) {
        result.style.background = "#eb7070";
        robotchoice = "red";
    } else if (robotchoice == 6) {
        result.style.background = "#d1eecc";
        robotchoice = "lightgreen";
    } else if (robotchoice == 7) {
        result.style.background = "#caa5f1";
        robotchoice = "lightpurple";
    } else {
        result.style.background = "#eadca6";
        robotchoice = "brown";
    }
}
function playerchoice(x) {
    if (robotchoice == x) {
        console.log("correct");
        score = score + 1
        robot();
    } else {
        console.log("wrong");
        robot();
    }
}


function starter() {
    startingbutton.addEventListener("click", function(){
        if (x > 0) {
            location.reload(false);
        } else {
            w = new Worker("worker.js");
            workerstarter();
        }
    })
}
function starterbutton() {
    lime.addEventListener("click", function() {
        playerchoice("lime");
    })
    purple.addEventListener("click", function() {
        playerchoice("purple");
    })
    orange.addEventListener("click", function() {
        playerchoice("orange");
    })
    aquablue.addEventListener("click", function() {
        playerchoice("aquablue");
    })
    red.addEventListener("click", function() {
        playerchoice("red");
    })
    brightpurple.addEventListener("click", function() {
        playerchoice("brightpurple");
    })
    brown.addEventListener("click", function() {
        playerchoice("brown");
    })
    lightgreen.addEventListener("click", function() {
        playerchoice("lightgreen");
    })
    yellow.addEventListener("click", function() {
        playerchoice("yellow");
    })
}

starter()

