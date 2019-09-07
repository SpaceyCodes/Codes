var total = 100;
var profit = 0;
var costforplus1 = 5;
var costforplus5 = 25;
var costforplus10 = 50;
var costforplus50 = 250;
var costforplus100 = 500;
var costforplus500 = 2500;
var costforplus1000 = 5000;
var costforplus2500 = 17500;
var costforplus5000 = 25000;
const r = document.getElementById("r");
const plus1 = document.getElementById("plus1")
const plus5 = document.getElementById("plus5")
const plus10 = document.getElementById("plus10")
const plus50 = document.getElementById("plus50")
const plus100 = document.getElementById("plus100")
const plus500 = document.getElementById("plus500")
const plus1000 = document.getElementById("plus1000")
const plus2500 = document.getElementById("plus2500")
const plus5000 = document.getElementById("plus5000")
const showprofit = document.querySelector("#showprofit");
const showtotal = document.querySelector("#showtotal");
const showcostfor1 = document.querySelector("#showcostfor1");
const showcostfor5 = document.querySelector("#showcostfor5");
const showcostfor10 = document.querySelector("#showcostfor10");
const showcostfor50 = document.querySelector("#showcostfor50");
const showcostfor100 = document.querySelector("#showcostfor100");
const showcostfor500 = document.querySelector("#showcostfor500");
const showcostfor1000 = document.querySelector("#showcostfor1000");
const showcostfor2500 = document.querySelector("#showcostfor2500");
const showcostfor5000 = document.querySelector("#showcostfor5000");
function starter() {
    w = new Worker("worker.js");
    w.addEventListener("message", function() {
        game()
    })
    plus1.addEventListener("click", function() {
        if (0 <= total - costforplus1) {
            cost (costforplus1, showcostfor1);
        } 
    })
    plus5.addEventListener("click", function() {
        if (0 <= total - costforplus5) {
            cost (costforplus5, showcostfor5);
        }
    })
    plus10.addEventListener("click", function() {
        if (0 <= total - costforplus10) {
            cost (costforplus10, showcostfor10);
        }
    })
    plus50.addEventListener("click", function() {
        if (0 <= total - costforplus50) {
            cost (costforplus50, showcostfor50);
        }
    })
    plus100.addEventListener("click", function() {
        if (0 <= total - costforplus100) {
            cost (costforplus100, showcostfor100);
        }
    })
    plus500.addEventListener("click", function() {
        if (0 <= total - costforplus500) {
            cost (costforplus500, showcostfor500);
        }
    })
    plus1000.addEventListener("click", function() {
        if (0 <= total - costforplus1000) {
            cost (costforplus1000, showcostfor1000);
        }
    })
    plus2500.addEventListener("click", function() {
        if (0 <= total - costforplus2500) {
            cost (costforplus2500, showcostfor2500);
        }
    })
    plus5000.addEventListener("click", function() {
        if (0 <= total - costforplus5000) {
            cost (costforplus5000, showcostfor5000);
        }
    })
}
starter();
function game() {
    total = total + profit;
    showtotal.innerHTML = `Total: ${total}units`;
}
function adding(x) {
    profit = profit + x;
    showprofit.innerHTML = `${profit} units/s`;
}
function cost(x, y) {
    total = total - x;
    if (x == costforplus1){
        adding(1);
        costforplus1 = Math.floor(costforplus1*1.2);
        x = Math.floor(x*1.2);
    } else if (x == costforplus5){
        adding(5);
        costforplus5 = Math.floor(costforplus5*1.25);
        x = Math.floor(x*1.25);
    } else if (x == costforplus10) {
        adding(10);
        costforplus10 = Math.floor(costforplus10*1.30);
        x = Math.floor(x*1.30);
    } else if (x == costforplus50) {
        adding(50);
        costforplus50 = Math.floor(costforplus50*1.30);
        x = Math.floor(x*1.30);
    } else if (x == costforplus100) {
        adding(100);
        costforplus100 = Math.floor(costforplus100*1.30);
        x = Math.floor(x*1.30);
    } else if (x == costforplus500) {
        adding(500);
        costforplus500 = Math.floor(costforplus500*1.30);
        x = Math.floor(x*1.30);
    }else if (x == costforplus1000) {
        adding(1000);
        costforplus1000 = Math.floor(costforplus1000*1.30);
        x = Math.floor(x*1.30);
    } else if (x == costforplus2500) {
        adding(2500);
        costforplus2500 = Math.floor(costforplus2500*1.30);
        x = Math.floor(x*1.30);
    } else if (x == costforplus5000) {
        adding(5000);
        costforplus5000 = Math.floor(costforplus5000*1.30);
        x = Math.floor(x*1.30);
    }
    showtotal.innerHTML = `Total: ${total}units`;
    y.innerHTML = `Cost:${x}`;
}