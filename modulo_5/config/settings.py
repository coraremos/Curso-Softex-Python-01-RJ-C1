import os 
import environ
from pathlib import Path
from datetime import timedelta
import sys
import dj_database_url
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# Inicializar django-environ
env = environ.Env( 
    DEBUG=(bool, False)  # Valor padrão caso não esteja no .env 
)

# Ler o arquivo .env
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Lê do ambiente. Se não achar, usa uma chave insegura (fallback)
SECRET_KEY = os.getenv("SECRET_KEY", "chave-insegura-fallback")

# Lê do ambiente. Retorna 'True' se o valor for "True", senão False.
DEBUG = os.getenv("DEBUG", "False") == "True"

# Hosts permitidos
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

# O Render define a variável RENDER_EXTERNAL_HOSTNAME automaticamente
render_host = os.getenv("RENDER_EXTERNAL_HOSTNAME")
if render_host:
    ALLOWED_HOSTS.append(render_host)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party 
    'rest_framework', 
    'rest_framework_simplejwt', 
    'rest_framework_simplejwt.token_blacklist',
     
    # Local apps 
    'core',
]

# Configuração do Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_ATUTHENTICATION_CLASSES': (
        # Define JWT como método de autenticação PADRÃO
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_THROTTLE_CLASSES': [         
        'rest_framework.throttling.AnonRateThrottle',         
        'rest_framework.throttling.UserRateThrottle'     
    ],     
    
    'DEFAULT_THROTTLE_RATES': {         
        'anon': '100/day',  # 100 requisições por dia para anônimos (ex: /token/)
        'user': '3000/day'  # 3000 requisições por dia para autenticados (ex: /tarefas/)     
    }
}

SIMPLE_JWT = {
    'ACESS_TOKEN_LIFETIME': timedelta(minutes=15), #tempo de vida do token Access
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7), #tempo de vida do token Refresh

    'ROTATE_REFRESH_TOKENS': True,      
    'BLACKLIST_AFTER_ROTATION': True,

    'AUTH_HEADER_TYPES': ('Bearer',), #será o esquema de autenticação no header HTTP
    'ALGORITHM':'HS256', #algoritmo de criptografia
    'USER_ID_CLAIM':'user_id', #nome do campo de usuário no PayLoad
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True, # Importante para Render
    )
}

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "staticfiles"

# Compactação e cacheamento otimizado
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

if 'test' in sys.argv:     
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',         
        'NAME': ':memory:',  # Banco reside apenas na RAM     
    }