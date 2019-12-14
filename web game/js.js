window.currentlocation = 25;
window.bulletlocation = 26;
window.facing = -20;
document.addEventListener('keydown', function(event) {
    const charList = 'abcdefghijklmnopqrstuvwxyz0123456789';
    const key = event.key.toLowerCase();
    if (charList.indexOf(key) === -1) return;
    if (key == "e") {
        shooting();
    }
    if ((key == "w") && (window.currentlocation - 20) > 0) {
        document.getElementById('id'.concat(window.currentlocation)).style.backgroundColor = "initial";
        window.currentlocation -= 20;
        document.getElementById('id'.concat(window.currentlocation)).style.backgroundColor = "red";
        console.log(window.currentlocation);
        window.facing = -20;
    }
    if ((key == "a") && (window.currentlocation != 1) && (window.currentlocation != 21) && (window.currentlocation != 41) && (window.currentlocation != 61) && (window.currentlocation != 81)
    && (window.currentlocation != 101) && (window.currentlocation != 121) && (window.currentlocation != 141) && (window.currentlocation != 161) && (window.currentlocation != 181)) {
        document.getElementById('id'.concat(window.currentlocation)).style.backgroundColor = "initial";
        window.currentlocation -= 1;
        document.getElementById('id'.concat(window.currentlocation)).style.backgroundColor = "red";
        console.log(window.currentlocation);
        window.facing = -1;
    }
    if ((key == "s") && (window.currentlocation + 20) < 201) {
        document.getElementById('id'.concat(window.currentlocation)).style.backgroundColor = "initial";
        window.currentlocation += 20;
        document.getElementById('id'.concat(window.currentlocation)).style.backgroundColor = "red";
        console.log(window.currentlocation);
        window.facing = +20;
    }
    if ((key == "d") && (window.currentlocation != 20) && (window.currentlocation != 40) && (window.currentlocation != 60) && (window.currentlocation != 80) && (window.currentlocation != 100)
    && (window.currentlocation != 120) && (window.currentlocation != 140) && (window.currentlocation != 160) && (window.currentlocation != 180) && (window.currentlocation != 200)) {
        document.getElementById('id'.concat(window.currentlocation)).style.backgroundColor = "initial";
        window.currentlocation += 1;
        document.getElementById('id'.concat(window.currentlocation)).style.backgroundColor = "red";
        console.log(window.currentlocation);
        window.facing = +1;
    }
});
w = new Worker("worker.js");
function shooting() {
    window.bulletlocation = window.currentlocation + window.facing;
    w.addEventListener("message", function() {
        if (window.bulletlocation == window.currentlocation) {
            document.getElementById('id'.concat(window.bulletlocation)).style.backgroundColor = "initial";
            document.getElementById('id'.concat(window.currentlocation)).style.backgroundColor = "green";
        } else {
            document.getElementById('id'.concat(window.bulletlocation)).style.backgroundColor = "initial";
            window.bulletlocation += window.facing;
            document.getElementById('id'.concat(window.bulletlocation)).style.backgroundColor = "black";
        }
    })
}
