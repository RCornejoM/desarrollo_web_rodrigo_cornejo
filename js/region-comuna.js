const regionSelect = document.getElementById("region");
const comunaSelect = document.getElementById("comuna");
  
// Crea todas las opciones de región
for( const region_data of comunasPorRegion.regiones ){
    regionSelect.innerHTML += "<option value='" + region_data.id + "'>" + region_data.region + "</option>";
}

// Cuando se seleccione una región
regionSelect.addEventListener("change", () => {
  const selectedRegion = regionSelect.value;
  const comunas = comunasPorRegion.regiones[selectedRegion].comunas;
    
  comunaSelect.innerHTML = "<option value=''>Seleccione una comuna</option>";
  for( const comuna_index in comunas ){
    comunaSelect.innerHTML += "<option value='" + comuna_index + "'>" + comunas[comuna_index] + "</option>";
  }
  
  comunaSelect.disabled = comunas.length === 0;
});
