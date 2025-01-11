
# Blog Project

## Descripción

Este es un proyecto de blog desarrollado con Django que permite a los usuarios crear, actualizar y eliminar publicaciones. Cada usuario puede ver y gestionar solo sus propias publicaciones. El proyecto incluye integración con CKEditor para edición enriquecida de texto, soporte para carga de imágenes y un sistema de autenticación de usuarios.

---

### Tecnologías Utilizadas

- **Lenguaje:** Python 3.10  
- **Framework:** Django 4.0  
- **Base de Datos:** SQLite  
- **Frontend:** HTML, CSS, Bootstrap  
- **Gestor de Dependencias:** pip  

---

### Características Principales

- Sistema de autenticación para usuarios registrados.
- Creación, edición y eliminación de publicaciones.
- Cada usuario solo puede acceder a sus propias publicaciones.
- Carga y visualización de imágenes en las publicaciones.
- Visualización del listado de publicaciones en el home.

---

## Requisitos

- Python 3.10+  
- pip para la gestión de dependencias.  
- Django 4.0+  

---

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/CristianAlbarracinCurso/Python_final_albarracin.git
   cd Python_final_albarracin
   ```

2. **Crea un entorno virtual e instálalo:**
   ```bash
   python -m venv venv
   ```

   - **En Windows:**
     ```bash
     venv\Scripts\activate
     ```

   - **En macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Realiza las migraciones:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Ejecuta el servidor:**
   ```bash
   python manage.py runserver
   ```

6. **Accede al proyecto en tu navegador en:**  
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Uso de la Aplicación

- **Inicio de sesión:** Los usuarios deben iniciar sesión o registrarse para acceder a las funcionalidades principales.
- **Creación de publicaciones:** Utiliza el formulario para agregar una nueva página con título, contenido e imagen.
- **Edición y eliminación:** Cada usuario puede editar o eliminar sus publicaciones desde el listado de páginas.
- **Visualización:** El home muestra un resumen de las publicaciones. Si el contenido es largo, aparece un enlace para ver los detalles completos.

---

## Modelo de Base de Datos

### Tabla: Page

- **author:** Relación con el usuario que crea la página.  
- **title:** Título de la publicación.  
- **content:** Contenido enriquecido del blog.  
- **image:** Imagen asociada a la publicación.  
- **created_at:** Fecha de creación.  
- **updated_at:** Fecha de última modificación.  

---

## Extras

### Capturas de pantalla

#### Página principal:

![Captura 1](https://github.com/CristianAlbarracinCurso/Python_final_albarracin/blob/main/VideoDemostracion/1.png)

---
![Captura 2](https://github.com/CristianAlbarracinCurso/Python_final_albarracin/blob/main/VideoDemostracion/2.png)

---
![Captura 3](https://github.com/CristianAlbarracinCurso/Python_final_albarracin/blob/main/VideoDemostracion/3.png)

---
![Captura 4](https://github.com/CristianAlbarracinCurso/Python_final_albarracin/blob/main/VideoDemostracion/4.png)

---
![Captura 5](https://github.com/CristianAlbarracinCurso/Python_final_albarracin/blob/main/VideoDemostracion/5.png)

---
![Captura 6](https://github.com/CristianAlbarracinCurso/Python_final_albarracin/blob/main/VideoDemostracion/6.png)

---
![Captura 7](https://github.com/CristianAlbarracinCurso/Python_final_albarracin/blob/main/VideoDemostracion/7.png)

---

![Captura video](https://github.com/CristianAlbarracinCurso/Python_final_albarracin/blob/main/VideoDemostracion/demo.mp4)

---
¡Gracias por revisar este proyecto! 😊
