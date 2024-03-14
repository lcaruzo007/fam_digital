import os
from pathlib import Path
from decouple import config


# Variáveis de ambiente sensíveis -> .env
HOSTS_LIBERADOS = config('HOSTS_LIBERADOS')
ORIGENS_CONFIAVEIS = config('ORIGENS_CONFIAVEIS')
SECRET_KEY = config('SECRET_KEY')
NAME_BANCO = config('NAME_BANCO')
USER_BANCO = config('USER_BANCO')
PASSWORD_BANCO = config('PASSWORD_BANCO')
HOST_BANCO = config('HOST_BANCO')
PORT_BANCO = config('PORT_BANCO')


DEBUG = True  # Alterar para False em produção

ALLOWED_HOSTS = [HOSTS_LIBERADOS]  

CSRF_TRUSTED_ORIGINS = [ORIGENS_CONFIAVEIS] 

# Configuração do banco de dados
DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql',
        "NAME": NAME_BANCO,
        "USER": USER_BANCO,
        "PASSWORD": PASSWORD_BANCO,
        "HOST": HOST_BANCO,
        "PORT": PORT_BANCO,
    }
}

BASE_DIR = Path(__file__).resolve().parent.parent

# Aplicativos instalados no projeto
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "app",
    "crispy_forms",
    "crispy_bootstrap5",
]

# Configuração do Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Configuração do Django
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Configuração de rotas -> começa pelas urls de config
ROOT_URLCONF = "config.urls"

# Configuração de templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            # Templates das demais aplicações
            os.path.join(BASE_DIR, "app/templates/"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Validação de senha
AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
]

# Padronização de URL -> adiciona barra no final quando True
APPEND_SLASH = False

# Configuração de região e fuso horário
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"

# Configuração de localização
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Configuração de formato de data e hora
DATE_INPUT_FORMATS = ["%d-%m-%Y"]  # Data no formato 'dd-mm-yy'
DATETIME_INPUT_FORMATS = [
    "%d-%m-%Y %H:%M:%S"
]  # Data e hora no formato 'dd-mm-yy hh:mm:ss'

# Configuração de arquivos estáticos
# URL para arquivos estáticos
STATIC_URL = "static/"
# Caminho absoluto para a pasta 'static'
STATIC_ROOT = os.path.join(STATIC_URL, "static")
# Locais adicionais para arquivos estáticos
STATICFILES_DIRS = [
    # Diretório 'static' das demais aplicações
    os.path.join(BASE_DIR, "apps/static/"),
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"