# NZ Home Project

## Descripción

Breve descripción del proyecto, su propósito y funcionalidades principales.

## Requisitos Previos

- Python 3.8+
- pip
- virtualenv

## Configuración del Entorno de Desarrollo

### 1. Clonar el Repositorio

```bash
git clone https://github.tu-usuario/django-jet-postgresql.git
cd django-jet-postgresql
```

### 2. Crear Entorno Virtual

```bash
python3 -m venv venv
```

### 3. Activar Entorno Virtual

- En Unix/macOS:

```bash
source venv/bin/activate
```

- En Windows:

```bash
.\venv\Scripts\activate
```

### 4. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 5. Configuración de Variables de Entorno

1. Navegar a la carpeta `nzhome`
2. Copiar `.env.example` a `.env`

```bash
cp .env.example .env
```

### 6. Generar SECRET_KEY

```bash
python3 manage.py shell
>>> from django.core.management.utils import get_random_secret_key
>>> print(get_random_secret_key())
```

Copiar la clave generada y reemplazar el valor en `.env`

### 7. Crear Directorio de Logs

```bash
mkdir logs
```

### 8. Configurar Base de Datos

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### 9. Crear Superusuario

```bash
python3 manage.py createsuperuser
```

## Ejecución del Proyecto

```bash
python3 manage.py runserver
```

## Estructura del Proyecto

```
nz-home/
│
├── .vscode/
├── locale/
├── logs/                 # Directorio de logs
├── nzhome/               # Directorio principal del proyecto
│   ├── .env              # Variables de entorno
│   ├── .env.example      # Ejemplo de configuración
│   └── ...
├── public/
├── templates/
├── typings/
├── utils/
├── venv/                 # Entorno virtual
├── .gitignore
├── db.sqlite3
├── manage.py
├── README.md             # Este archivo
└── requirements.txt      # Dependencias del proyecto
```

## Buenas Prácticas

- Mantén el `.env` fuera del control de versiones
- Actualiza regularmente las dependencias
- Usa `pip freeze > requirements.txt` para actualizar dependencias

## Troubleshooting

- Si encuentras problemas con migraciones:
  ```bash
  python3 manage.py migrate --run-syncdb
  ```
- Para reinstalar dependencias:
  ```bash
  pip install -r requirements.txt --upgrade
  ```

## Contacto

zubiarrainnahuel@gmail.com
