
function open_image_viewer(image){
	document.getElementById("imagenGrande").src = image;
	document.getElementById("visorImagen").style.display = "flex";
}

function close_image_viewer(){
	document.getElementById("visorImagen").style.display = "none";
}

