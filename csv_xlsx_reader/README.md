# csv_xlsx_reader

# Pasos para correr el proyecto

```
    - git clone git@gitlab.com:Jota.alvarez/csv_xlsx_reader.git
    - virtualenv nombre_de_tu_entorno -p python3
    - source nombre_de_tu_entorno/bin/activate
    - cd csv_xlsx_reader
    - pip install -r requirements.txt
    - python manage.py migrate
    - python manage.py runserver
```

# Una vez creado el proyecto

```
    - ir a 127.0.0.1:8000
    - crear un usuario
    - loguearse
    - subir el archivo excel
```

# Para ver el admin

### Cuando el proyecto esté corriendo sin problemas

```
    - source nombre_de_tu_entorno/bin/activate (Solo si no está activado el entorno virtual)
    - python manage.py createsuperuser
    - ir a 127.0.0.1:8000/admin/
    - entrar con el super usuario creado
```
