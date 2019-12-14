const electron = require('electron');
const url = require('url');
const path = require('path');
const ipc = electron.ipcMain;
const dialog = electron.dialog;

const {app, BrowserWindow, Menu, globalShortcut, shell} = require('electron');

let mainWindow;

app.on('ready', function(){
    mainWindow = new BrowserWindow({hasShadow: false, frame: false, minWidth: 200 ,minHeight: 45, webPreferences: {nodeIntegration:true}});
    mainWindow.setPosition(1720,0);
    mainWindow.setSize(200,45);
    Menu.setApplicationMenu(null);
    mainWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'index.html'),
        protcol:'file',
        slashes: true
    }));
    globalShortcut.register('Alt+Delete', () => {
        mainWindow.setPosition(1720,0);
        mainWindow.setSize(200,45);
        mainWindow.show();
    });
    ipc.on("code init", function() {
        shell.openItem("C:\\Users\\WOODLANDS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe");
    })
    ipc.on("game init", function() {
        shell.openItem("C:\\Users\\WOODLANDS\\AppData\\Local\\Discord\\app-0.0.305\\Discord.exe");
        shell.openItem("D:\\Program Files (x86)\\Steam\\Steam.exe");
        shell.openItem("C:\\Program Files (x86)\\Garena\\Garena\\Garena.exe");
    })
    ipc.on("minimise", function(event) {0
        mainWindow.minimize();
    })
});

