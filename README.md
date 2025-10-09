#  Sistema de Gestión de Adopciones de Mascotas

Este proyecto es un prototipo de aplicación web que permite gestionar el proceso de adopción de perros y gatos.  
Fue desarrollado utilizando **HTML5**, **CSS3** y **JavaScript**, ahora incluye integración base de datos. 
Su propósito es demostrar la estructura, navegación y validaciones de un sistema de adopciones.

No se implementó el manejo de archivos. Se implementaron cinco templates (una Portada, un formulario, una lista, una para fichas y una futura pagina para estadisticas), las validaciones se hacen tanto de lado del servidor como del cliente. La informacion de las regiones se trata en el cliente como JSON/Objeto de javascript, ya que es la que se habia implementado ya para la tarea 1. 

---

## Cómo Ejecutar

1. Descargue o clone este repositorio.  
2. Cree un entorno virtual
```bash
python -m venv venv
source venv/bin/activate
venv/Scripts/activate
```

3. Si no existe la base de datos "adopciones", creela con:
```mysql
CREATE DATABASE adopciones;
```

y luego

```bash
mysql -u <user> -p adopciones < region-comuna.sql
mysql -u <user> -p adopciones < tarea2.sql;
```
---

4. Finalmente ejecute
```bash
flask --app app.py run
```
La página se mostrará en localhost:5000.


---

No licence.
