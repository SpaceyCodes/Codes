const formval = document.getElementById("form");
function firestarter() {
    formval.addEventListener("click", function() {
        formclear();
    })
    formval.addEventListener("keydown", function(e) {
        if (e.keyCode ==13) {
            if (formval.value=="code init") {
                const electron = require("electron");
                const ipc = electron.ipcRenderer;
                ipc.send("code init");
                formclear();
                formval.blur();
            }
            else if (formval.value=="game init") {
                const electron = require("electron");
                const ipc = electron.ipcRenderer;
                ipc.send("game init");
                formclear();
                formval.blur();
            }
            else {
                formval.value = "| Wrong Command |"
                formval.blur();
            }
        }
    }) 
}
function formclear() {
    formval.value = "";
}
firestarter();