# FastPdf2Docx

API para convertir un pdf a docx

## Requisitos
- Python 3.10 o superior

## Instalación

1. Clona el repositorio
```bash
git clone https://github.com/klamx/convert2docx.git
```

2. Crea el entorno de desarrollo
```bash
cd convert2docx
pip install pipenv
pipenv shell
```

3. Instala las dependencias
```bash
pipenv install -r requirements.txt
```

4. Ejecuta la aplicación
```bash
uvicorn main:app main:app --host 0.0.0.0 --port 3000
```

5. Visualiza en tu navegador [http://localhost:3000/](http://localhost:3000/).
