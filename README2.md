# FastPdf2Docx

API para convertir un pdf a docx

## Requisitos
- Python 3.10 o superior
- venv (**solo si se va a ejecutar en un entorno virtual**)

## Instalación

1. Clona el repositorio
```bash
git clone https://github.com/klamx/convert2docx.git
```

### Dockerizacion
1. Docker
```bash
cd convert2docx
docker compose build
docker compose up -d
```

2. Visualiza en tu navegador [http://localhost:3000/docs](http://localhost:3000/docs).

### Entorno virtual
1. Crea el entorno de desarrollo
```bash
cd convert2docx
python -m venv venv
# or
python3 -m venv venv

source ./venv/bin/activate
```

2. Verificar que se este ejecutando el entorno de desarrollo
```bash
# Este comando no debe devolver nada
pip3 freeze
# or
pip3 freeze
```

3. Instala las dependencias
```bash
pip install -r requirements.txt
# or
pip3 install -r requirements.txt
```

4. Ejecuta la aplicación
```bash
uvicorn src.main:app --host 0.0.0.0 --port 3000
```

5. Visualiza en tu navegador [http://localhost:3000/docs](http://localhost:3000/docs).

## Stack usado
- FastAPI