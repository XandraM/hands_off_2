const client = new Paho.Client("openlab.kpi.fei.tuke.sk", 443, "player" + Date.now());
client.onMessageArrived = onMessageArrived;
client.connect({onSuccess: onConnect, reconnect: true, useSSL: true, keepAliveInterval: 10, timeout: 10});

function onMessageArrived(messaage) {
    client.subscribe("openlab/voice/recognition");

    document.getElementById("")
}