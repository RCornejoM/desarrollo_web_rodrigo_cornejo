var form = document.getElementById("avisoForm");
var fotosContainer = document.getElementById("fotosContainer");
var btnAgregarFoto = document.getElementById("agregarFoto");

btnAgregarFoto.onclick = function() {
  var totalFotos = fotosContainer.getElementsByTagName("input").length;
  if (totalFotos < 5) {
    var nuevoDiv = document.createElement("div");
    nuevoDiv.innerHTML = '<label>Foto: <input type="file" name="foto" accept="image/*"></label>';
    fotosContainer.appendChild(nuevoDiv);
  } else {
    alert("Máximo 5 fotos permitidas");
  }
};

form.onsubmit = function(e) {
  e.preventDefault();
  var errores = "";

  var region = form.elements["region"].value;
  var comuna = form.elements["comuna"].value;
  var sector = form.elements["sector"].value.trim();
  var nombre = form.elements["nombre"].value.trim();
  var email = form.elements["email"].value.trim();
  var celular = form.elements["celular"].value.trim();
  var descripcion = form.elements["descripcion"].value.trim();
  var tipo = form.elements["tipo"].value;
  var cantidad = parseInt(form.elements["cantidad"].value);
  var edad = parseInt(form.elements["edad"].value);
  var unidadEdad = form.elements["unidad_medida"].value;
  var fechaEntrega = form.elements["fecha_entrega"].value;
  var fotos = form.elements["foto"]; // puede ser lista si hay varias

  if (region === "") errores += "- Debe seleccionar una región.\n";
  if (comuna === "") errores += "- Debe seleccionar una comuna.\n";
  if (sector.length < 3) errores += "- El sector debe tener al menos 3 caracteres.\n";
  if (nombre.length < 3) errores += "- El nombre debe tener al menos 3 caracteres.\n";

  // Validación de email simple
  if (email === "") {
    errores += "- El email es obligatorio.\n";
  } else if (email.indexOf("@") === -1 || email.indexOf(".") === -1) {
    errores += "- El email debe tener un formato válido.\n";
  }

  // Validación de celular simple: mínimo 8 dígitos y solo números
  if (celular === "") {
    errores += "- El celular es obligatorio.\n";
  } else if (!/^\d{8,15}$/.test(celular)) {
    errores += "- El celular debe tener entre 8 y 15 números.\n";
  }

  if (tipo === "") errores += "- Debe seleccionar el tipo de mascota.\n";
  if (isNaN(cantidad) || cantidad < 1) errores += "- Cantidad inválida.\n";
  if (isNaN(edad) || edad < 1) errores += "- Edad inválida.\n";
  if (unidadEdad === "") errores += "- Debe indicar unidad de edad (si es en meses o años).\n";
  if (fechaEntrega === "") errores += "- Debe indicar una fecha de entrega.\n";
  if (descripcion === "") errores += "- Debe indicar una descripcion.\n";
  var fotosCount = fotos.length ? fotos.length : (fotos.value ? 1 : 0);
  if (fotosCount === 0) errores += "- Debe subir al menos una foto.\n";
  if (fotosCount > 5) errores += "- Debe subir a lo más cinco fotos.\n";

  if (errores !== "") {
    alert("Errores:\n" + errores);
    return;
  }

  form.submit();
};

