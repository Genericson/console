// A test chat program
channel;
socket;

function init() {
  channel = new goog.appengine.Channel();
  socket = channel.open();
  socket = onopen = onOpened;
  socket.onmessage = onMessage;
  socket.onerror = onError;
  socket.onclose = onClose;
}
function onOpened() {
	alert("Channel opened!");
	sendMessage('/opened');
}
function onMessage(msg) {
	alert(msg.data);
}
function onError(err) {
	alert(err);
}
function onClose() {
	alert("Channel closed!");
}
function openChannel() {
	var token = '{{ token }}';
	var channel = new goog.appengine.Channel(token);
	var handler = {
		'onopen': onOpened,
		'onmessage': onMessage,
		'onerror': onError,
		'onClose': onClose,
	};
	var socket = channel.open(handler);
	socket.onmessage = onMessage;
}
function sendMessage(path) {
	path += '?g' + state.game_key;
}