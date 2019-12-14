const minimisebut = document.getElementById("button1");
const maximisebut = document.getElementById("button2");
const closebut = document.getElementById("button3");
const electron = require("electron");
const ipc = electron.ipcRenderer;
function starter() {
    closebut.addEventListener("click", function(){
        window.close();
    });
    maximisebut.addEventListener("click", function(){
        if (window.innerHeight != screen.availHeight && window.innerWidth != screen.availWidth) {
            window.oldheight = window.innerHeight;
            window.oldwidth = window.innerWidth;
            window.resizeTo(screen.availWidth, screen.availHeight);
        } else {
            window.resizeTo(window.oldwidth,window.oldheight);
            window.moveTo(500, 100);
        }

    });
    minimisebut.addEventListener("click", function(){
        ipc.send("minimise");
    });
}

starter();