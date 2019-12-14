var Peer = require('simple-peer');
var peer = new Peer({
    initiator: location.hash === '#init',
    trickle: false
});

peer.on('signal', function(data) {
    document.getElementById('yourid').value = JSON.stringify(data)
})
document.getElementById('connect').addEventListener('click', function(){
    var otherid = JSON.parse(document.getElementById('otherid').value)
    peer.signal(otherid)
})

document.getElementById('send').addEventListener('click', function() {
    var yourmessage = document.getElementById('yourmessage').value
    document.getElementById('messages').textContent += yourmessage + '\n'
    peer.send(yourmessage)
})

peer.on('data',function(data) {
    document.getElementById('messages').textContent += data + '\n'
})