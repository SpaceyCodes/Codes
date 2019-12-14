const electron = require('electron');
const url = require('url');
const path = require('path');
const {app, BrowserWindow, Menu, globalShortcut, shell, ipcMain, dialog} = require('electron');

let mainWindow;
ipcMain.on('open-error', function(event) {
    shell.openItem("D:\\WOODLANDS\\Documents\\GitHub\\Codes\\discord bot\\bot.py");
})
app.on('ready', function(){
    mainWindow = new BrowserWindow({ minWidth: 150 ,minHeight: 10,webPreferences: {nodeIntegration: true}});
    mainWindow.setSize(370,500);
    mainWindow.webContents.openDevTools();
    globalShortcut.register('Alt+A', () => {
        shell.openItem("D:\\WOODLANDS\\Documents\\GitHub\\Codes\\discord bot\\bot.py");
    });
    mainWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'index.html'),
        protcol:'file',
        slashes: true
    }));
    Menu.setApplicationMenu(null);
    
});
