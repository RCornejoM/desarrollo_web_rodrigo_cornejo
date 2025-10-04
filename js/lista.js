
function open_image_viewer(image){
	document.getElementById("imagenGrande").src = image;
	document.getElementById("visorImagen").style.display = "flex";
}

function close_image_viewer(){
	document.getElementById("visorImagen").style.display = "none";
}




document.addEventListener("DOMContentLoaded", () => {
  const tablaAvisos = document.getElementById("tablaAvisos");
  const detalleAviso = document.getElementById("detalleAviso");
  const contenidoDetalle = document.getElementById("contenidoDetalle");
  const visor = document.getElementById("visorImagen");
  const imagenGrande = document.getElementById("imagenGrande");

  if (tablaAvisos) {
    const datosEjemplo = {
      1: {
        fechaPub: "2025-08-18",
        fechaEntrega: "2025-08-21",
        comuna: "Santiago",
        sector: "Beauchef 851",
        cantidad: 1,
        tipo: "Gato",
        edad: "2 meses",
        contacto: "Juan Pérez",
        email: "juanp@example.com",
        fotos: ["assets/imgs/gato1.jpg", "assets/imgs/gato2.jpg"],
        descripcion: "Gatito cariñoso y juguetón, listo para adopción."
      },
      2: {
        fechaPub: "2025-08-17",
        fechaEntrega: "2025-08-22",
        comuna: "Ñuñoa",
        sector: "Irarrázaval 3010",
        cantidad: 1,
        tipo: "Perro",
        edad: "1 año",
        contacto: "María López",
        email: "mlopez@example.com",
        fotos: ["assets/imgs/perro1.jpg"],
        descripcion: "Perro amistoso, vacunado y esterilizado."
      },
      3: {
        fechaPub: "2025-08-16",
        fechaEntrega: "2025-08-25",
        comuna: "Valparaíso",
        sector: "Calle Francia 900",
        cantidad: 2,
        tipo: "Gato",
        edad: "3 meses",
        contacto: "José Díaz",
        email: "jdiaz@example.com",
        fotos: ["assets/imgs/gato2.jpg", "assets/imgs/gato3.jpg", "assets/imgs/gato1.jpg"],
        descripcion: "Dos hermanitos muy sociables, buscan adopción conjunta."
      },
      4: {
        fechaPub: "2025-08-15",
        fechaEntrega: "2025-08-23",
        comuna: "La Florida",
        sector: "Walker Martínez 400",
        cantidad: 1,
        tipo: "Perro",
        edad: "6 meses",
        contacto: "Camila Soto",
        email: "csoto@example.com",
        fotos: ["assets/imgs/perro2.jpg"],
        descripcion: "Cachorro obediente y muy cariñoso."
      },
      5: {
        fechaPub: "2025-08-14",
        fechaEntrega: "2025-08-20",
        comuna: "Puente Alto",
        sector: "Av. Concha y Toro 2300",
        cantidad: 1,
        tipo: "Gato",
        edad: "4 meses",
        contacto: "Pedro García",
        email: "pgarcia@example.com",
        fotos: ["assets/imgs/gato3.jpg", "assets/imgs/gato2.jpg"],
        descripcion: "Gatito juguetón que busca familia."
      }
    };

    // Click on a row → show detail
    tablaAvisos.querySelectorAll("tr[data-aviso]").forEach(row => {
      row.addEventListener("click", () => {
        const id = row.getAttribute("data-aviso");
        const a = datosEjemplo[id];

        // Build detail content
        contenidoDetalle.innerHTML = `
          <h2>Detalle del aviso</h2>
          <p><strong>Fecha publicación:</strong> ${a.fechaPub}</p>
          <p><strong>Fecha entrega:</strong> ${a.fechaEntrega}</p>
          <p><strong>Comuna:</strong> ${a.comuna}</p>
          <p><strong>Sector:</strong> ${a.sector}</p>
          <p><strong>Mascota:</strong> ${a.cantidad} ${a.tipo}, ${a.edad}</p>
          <p><strong>Descripción:</strong> ${a.descripcion}</p>
          <p><strong>Contacto:</strong> ${a.contacto} (${a.email})</p>
          <div class="fotosDetalle">
            ${a.fotos.map(f => `<img src="${f}" class="fotoDetalle" alt="foto" width="320" height="240">`).join("")}
          </div>
        `;

        // Toggle visibility
        tablaAvisos.classList.add("oculto");
        detalleAviso.classList.remove("oculto");

        // Add event listeners to each image
        document.querySelectorAll(".fotoDetalle").forEach(img => {
          img.addEventListener("click", () => {
            imagenGrande.src = img.src;
            visor.classList.remove("oculto");
          });
        });
      });
    });

    // Close full image
    const cerrarVisor = document.getElementById("cerrarVisor");
    if (cerrarVisor) {
      cerrarVisor.addEventListener("click", () => {
        visor.classList.add("oculto");
      });
    }

    // Back to list
    const volverListado = document.getElementById("volverListado");
    if (volverListado) {
      volverListado.addEventListener("click", () => {
        detalleAviso.classList.add("oculto");
        tablaAvisos.classList.remove("oculto");
      });
    }
  }
});



