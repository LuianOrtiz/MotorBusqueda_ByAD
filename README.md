# Motor de busqueda de startups en venture capital
- Busqueda y Almacenamiento de Datos
- Luis Angel Ortiz Salinas

## **Instrucciones**
1. Clonar el repositorio
    ```cmd
    git clone https://github.com/LuianOrtiz/MotorBusqueda_ByAD
    ```
2. Crear un entorno virtual de python
    ```cmd
        python -m venv env
    ```
3. Activar el entorno virtual
    ```cmd
    Windows: env\Scripts\activate
    Linux y Mac: source\bin\activate
    ```
4. Instalar las dependencias del proyecto que se encuentran en **requirements.txt**
    ```cmd
    pip install requirements.txt
    ```
5. Crear un superusuario 
    ```cmd
    python manage.py createsuperuser
    ```
6. Inicializar el servidor. 
    ```cmd
    python manage.py runserver
    ```

En este caso no es necesario hacer una migracion a la base de datos, ya que se encuentra el archivo db.sqlite3. Se recomienda eliminar los registros que se encuentran en dicha base de datos (esto puede ser desde el administrador de Django)

