

function showVideo(id){

	// Array of all media-elements
	var mediaAll = document.querySelectorAll(".audiotags");

	for (var i = 0; i < mediaAll.length; i++) {
		// Hiding all media-elements
		mediaAll[i].style.display = "none";
	}

	// Modify the id-String
	var playId = id.replace('play', "");
	var btnId = playId.replace('Btn', "");
	var myId = 'audio' + btnId

	// Show the media-element corresponding to the id
	document.getElementById(myId).style.display = "block";
}
