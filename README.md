# Crear Usuarios con FastAPI y conectar a Mongo DB

![phyton](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![mongo](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
![fastapi](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white)
![jwt](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white)
![postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white)

![html](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![css](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![js](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![vsc](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![git](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)



Este proyecto es una aplicación web desarrollada utilizando [FastAPI](https://fastapi.tiangolo.com/), un moderno marco web de Python para crear API rápidas. El objetivo de esta aplicación es gestionar usuarios, permitiendo la creación, lectura, actualización y eliminación de usuarios.

## Características

- **Creación de Usuarios:** Permite crear nuevos usuarios proporcionando un nombre de usuario y una dirección de correo electrónico.
- **Obtención de Usuarios:** Permite obtener una lista de todos los usuarios almacenados en la base de datos.
- **Actualización de Usuarios:** Permite actualizar la información de un usuario existente.
- **Eliminación de Usuarios:** Permite eliminar un usuario de la base de datos.

## Estructura del Proyecto

El proyecto sigue una estructura de carpetas y archivos que se organiza de la siguiente manera:

- **main.py:** Contiene el código principal de la aplicación FastAPI, donde se definen las rutas y la lógica de la aplicación.
- **routers/:** Carpeta que contiene los enrutadores (routers) de la aplicación, cada uno con sus propias rutas y operaciones relacionadas con usuarios.
- **db/:** Carpeta que contiene los modelos de datos y la configuración de la base de datos MongoDB.
- **frontend/:** Carpeta que contiene los archivos estáticos (HTML, CSS, JavaScript) para el frontend de la aplicación.
- **README.md:** Este archivo que estás leyendo, que proporciona información sobre el proyecto.

## Requisitos

Para ejecutar este proyecto localmente, necesitarás tener instalado lo siguiente:

- Python 3.7 o superior
- MongoDB

## Instalación y Ejecución

1. Clona este repositorio en tu máquina local:
```bash
git clone https://github.com/tu_usuario/fastapi-user-management.git
```


2. Instala las dependencias del proyecto:
```sh
pip install -r AyudaIniciarProyecto.txt
```

3. Inicia el servidor FastAPI:
```sh
uvicorn main:app --reload
```

4. Accede a la aplicación en tu navegador web:

a traves de  http://127.0.0.1:8000 y al front http://127.0.0.1:8000/static/index.html

## Contacto
### Para dudas y consultas..
![LINKEDIN](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)

- [Elias Javier Riquelme](https://www.linkedin.com/in/elias-javier-riquelme-b62655297/)




