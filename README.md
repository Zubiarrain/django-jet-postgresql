# NZ Home Project

## Descripción

Breve descripción del proyecto, su propósito y funcionalidades principales.

## Requisitos Previos

- Python 3.8+
- pip
- virtualenv

## Estructura del Proyecto

```
nz-home/
│
├── .vscode/              # Configuraciones de Visual Studio Code
├── locale/               # Archivos de localización
├── logs/                 # Directorio de logs
├── nzhome/               # Directorio principal del proyecto
│   ├── .env              # Variables de entorno
│   ├── .env.example      # Ejemplo de configuración
│   └── ...
├── public/               # Archivos estáticos públicos
├── templates/            # Plantillas HTML
├── typings/              # Definiciones de tipos
├── utils/                # Utilidades y funciones auxiliares
├── venv/                 # Entorno virtual
├── .gitignore
├── db.sqlite3
├── manage.py
├── README.md             # Este archivo
└── requirements.txt      # Dependencias del proyecto
```

## Configuración del Entorno de Desarrollo

### 1. Clonar el Repositorio

```bash
mkdir nombre-de-tu-proyecto
git clone git@github.com:Zubiarrain/django-jet-postgresql.git .
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

### 5. Configuración Inicial

1. Crear directorio de logs

```bash
mkdir logs
```

2. Navegar a la carpeta `nzhome`
3. Copiar `.env.example` a `.env`

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

### 7. Configurar Base de Datos

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### 8. Crear Superusuario

```bash
python3 manage.py createsuperuser
```

Sigue las instrucciones para:

- Ingresar nombre de usuario
- Ingresar dirección de correo electrónico (opcional)
- Crear contraseña
- Confirmar contraseña

### 9. Crear Nueva Aplicación Django

```bash
python3 manage.py startapp nombre_de_tu_app
```

Pasos adicionales después de crear la app:

1. Añadir la app al `INSTALLED_APPS` en `settings.py`

```python
INSTALLED_APPS = [
    ...
    'nombre_de_tu_app',
]
```

2. Crear modelos en `models.py`
3. Crear migraciones

```bash
python3 manage.py makemigrations nombre_de_tu_app
python3 manage.py migrate
```

### 10. Ejecución del Proyecto

```bash
python3 manage.py runserver
```

## Buenas Prácticas

- Mantén el `.env` fuera del control de versiones
- Usa un nombre descriptivo para tu nueva app
- Crea migraciones cada vez que modifiques modelos
- Mantén la documentación actualizada

## Troubleshooting

- Si encuentras problemas con migraciones:
  ```bash
  python3 manage.py migrate --run-syncdb
  ```
- Para reinstalar dependencias:
  ```bash
  pip install -r requirements.txt --upgrade
  ```

## Comandos Útiles

- Listar todas las migraciones:
  ```bash
  python3 manage.py showmigrations
  ```
- Crear migraciones para una app específica:
  ```bash
  python3 manage.py makemigrations nombre_de_tu_app
  ```

## Contacto

zubiarrainnahuel@gmail.com
