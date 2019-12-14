const { ipcRenderer } = require("electron");
    // Let's define our first command. First the text we expect, and then the function it should call
var commands = {
    'hello': function() {console.log('dwa');}};
  
// Add our commands to annyang
annyang.addCommands(commands);
annyang.start();

