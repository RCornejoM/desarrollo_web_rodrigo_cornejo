  // ------------------ CONTACTAR POR ------------------
  const contactarPor = document.getElementById("contactarPor");
  const extraContainer = document.getElementById("contactoExtraContainer");

  if (contactarPor) {
    contactarPor.addEventListener("change", () => {
      extraContainer.innerHTML = "";
      if (contactarPor.value) {
        const input = document.createElement("input");
        input.type = "text";
        input.id = "contactoExtra";
        input.placeholder = "Ingrese ID o URL (4-50 caracteres)";
        input.minLength = 4;
        input.maxLength = 50;
        extraContainer.appendChild(input);
      }
    });
  }

  // ------------------ FOTO ------------------
  const fotosContainer = document.getElementById("fotosContainer");
  const btnAgregarFoto = document.getElementById("agregarFoto");

  if (btnAgregarFoto) {
    btnAgregarFoto.addEventListener("click", () => {
      const totalFotos = fotosContainer.querySelectorAll("input[type='file']").length;
      if (totalFotos < 5) {
        const nuevo = document.createElement("div");
        nuevo.innerHTML = `<label>Foto: <input type="file" name="foto" accept="image/*"></label>`;
        fotosContainer.appendChild(nuevo);
      } else {
        alert("Máximo 5 fotos permitidas");
      }
    });
  }

  // ------------------ VALIDACIÓN ------------------
  const form = document.getElementById("avisoForm");
  const confirmacion = document.getElementById("confirmacion");
  const mensajeFinal = document.getElementById("mensajeFinal");


  form.addEventListener("submit", (e) => {
    e.preventDefault()
   
    const nombre = document.getElementById("nombre").value.trim();
    const email = document.getElementById("email").value.trim();
    const tipo = document.getElementById("tipo").value;
    const cantidad = parseInt(document.getElementById("cantidad").value);
    const edad = parseInt(document.getElementById("edad").value);
    const unidadEdad = document.getElementById("unidadEdad").value;
    const regionVal = document.getElementById("region").value;
    const comunaVal = document.getElementById("comuna").value;
    const fotos = fotosContainer.querySelectorAll("input[type='file']");

    let errores = [];

    if (!regionVal) errores.push("Debe seleccionar una región.");
    if (!comunaVal) errores.push("Debe seleccionar una comuna.");
    if (nombre.length < 3) errores.push("El nombre debe tener al menos 3 caracteres.");
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) errores.push("Email inválido.");
    if (!tipo) errores.push("Debe seleccionar el tipo de mascota.");
    if (!cantidad || cantidad < 1) errores.push("Cantidad inválida.");
    if (!edad || edad < 1) errores.push("Edad inválida.");
    if (!unidadEdad) errores.push("Debe indicar unidad de edad.");
    if (fotos.length === 0) errores.push("Debe subir al menos una foto.");
    if (fotos.length > 5) errores.push("Debe subir a lo más cinco fotos.");

    if (errores.length > 0) {
      alert("Errores:\n" + errores.join("\n"));
      return;
    }else{
       confirmacion.style.display = "none";
       form.style.display = "none"; // hide the form
       mensajeFinal.style.display = "block";
       
      const params = new URLSearchParams({
        nombre,
        email,
        tipo,
        cantidad,
        edad,
        unidadEdad,
        region: regionVal,
        comuna: comunaVal
      });

    // Redirect to another page (e.g., aviso_list.html) with the query string
    window.location.href = "aviso_list.html?" + params.toString();
    
    }
  });



function ask_for_confirmation(){
  confirmacion.style.display = "block";
}

function close_confirmation(){
  confirmacion.style.display = "none";
}


