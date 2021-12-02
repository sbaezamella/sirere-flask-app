# Sistema de registro Renal - Flask App

La aplicación completa está contenida dentro de la carpeta `sirere`.

El archivo `manage.py` es el ejecutable para iniciar la aplicación de Flask.

## Requerimientos

Tener Python 3 e instalar el entorno virtal. En este caso se ocupó `virtualenv`

- Python3
- virtualenv package

```bash
pip install virtualenv
```

## Variables de entorno

Se necesista crear un archivo `.env` en la carpeta raiz que contenga:

- La conexión URL a MySQL `MYSQL_URI="tuconexión"`
- Entorno de desarrollo de Flask, sólo uno de los tres: `SIRERE_CONFIG=development|production|testing`

## Instalación

Primero se debe crear el entorno virtual.

```bash
virtualenv env
```

Luego se activa.

```bash
source env/bin/activate
```

Por último, se instalan los paquetess en el entorno virtual desde el `requirementes.txt`.

```bash
pip install -r requirements.txt
```

## Iniciar la aplicación de Flask

```bash
python manager.py runserver
```

La aplicación se encontrará corriendo en `localhost:5000`
