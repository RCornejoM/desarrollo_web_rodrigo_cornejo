  // CONTACTAR POR
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

  // FOTO
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

// VALIDACIÓN 
const form = document.getElementById("avisoForm");
const confirmacion = document.getElementById("confirmacion");
const mensajeFinal = document.getElementById("mensajeFinal");

form.addEventListener("submit", (e) => {
  e.preventDefault()
   
  const nombre = document.getElementById("nombre").value.trim();
  const email = document.getElementById("email").value.trim();

  let errores = [];

  if (!regionVal) errores.push("Debe seleccionar una región.");
  if (errores.length > 0) {
    alert("Errores:\n" + errores.join("\n"));
    return;
  }else{
     confirmacion.style.display = "none";
     form.style.display = "none";
     mensajeFinal.style.display = "block";
       
    
  }
});



