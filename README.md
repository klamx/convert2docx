# PDF2DOCX

## Descripción general
La API proporciona funcionalidades para convertir archivos PDF a DOCX(word) de manera eficiente.

## Requerimientos
- Python >= 3.10
- venv
```bash
# debian
sudo apt install python3-venv
```

## Instalacion y Configuracion

- Clona el repositorio
```bash
git clone https://github.com/klamx/convert2docx.git
```

### Dockerizacion

```bash
cd convert2docx
docker compose build
docker compose up -d
```

***
[Más información sobre creacion de entornos virtuales para python](https://docs.python.org/es/3/library/venv.html)
***


### Creación entorno virtual sistemas POSIX
1. Crear el entorno virtual
```bash
python3 -m venv venv
```
2. Acceder al entorno virtual
```bash
# si se esta usando fish, csh o PowerShell cambiar activate por
# activate.fish, activate.csh, Activate.ps1 respecticavemente
source ./venv/bin/activate
```

### Creación entorno virtual Windows
1. Crear el entorno virtual
```bash
python -m venv venv
```
2. Acceder al entorno virtual
```bash
# cmd
C:\> <venv>\Scripts\activate.bat

# PowerShell
PS C:\> <venv>\Scripts\Activate.ps1
```

### Seguir con la instalación

3. Verificar que se este ejecutando el entorno de desarrollo
```bash
# Este comando no debe devolver nada
pip3 freeze
```

4. Instala las dependencias
```bash
pip3 install -r requirements.txt
```

5. Ejecuta la aplicación
```bash
uvicorn src.main:app --host 0.0.0.0 --port 3000
```

5. Visualiza en tu navegador [http://localhost:3000/docs](http://localhost:3000/docs).

## Uso Básico

### Convertir un PDF a DOCX

#### /pdf2docx/
- **POST**: Convierte un archivo PDF a DOCX.

Parámetros:
- file: Archivo PDF a DOCX.
- docxname: Nombre del archivo DOCX de salida.

Respuesta:
- Archivo DOCX convetido.