from datetime import timedelta
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2me%54_m481*_e033+eb91j5fi0k10^@^2^1^-uqtcz9_*f84i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['simul-api.onrender.com', 'localhost', '127.0.0.1','jumia-clone-api-11vb.onrender.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',

    'users',
    'news',
    'jobs',
    'user_message',
    'client_tracking',
    'bookings',
  
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'client_tracking.middleware.ClientIPTrackingMiddleware',
]

ROOT_URLCONF = 'core.urls'

AUTH_USER_MODEL = 'users.CustomUser'

# # Configure CORS
# CORS_ALLOWED_ORIGINS = [
#     "https://simul-website.vercel.app", 
#      "http://localhost:3000" # Add your frontend's origin here
#     # Add any other origins you want to allow
# ]

# Optional: Allow all origins (for development only)
CORS_ALLOW_ALL_ORIGINS = True


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,  # 10 messages per page

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Your SMTP server address
EMAIL_PORT = 587  # Your SMTP server port (587 is the default for SMTP with TLS)
EMAIL_USE_TLS = True  # Whether to use TLS (True by default)
EMAIL_HOST_USER = 'artstraining.co.uk@gmail.com'
EMAIL_HOST_PASSWORD = 'teoa fgdi draf suok'  #teoa fgdi draf suok
DEFAULT_FROM_EMAIL = 'artstraining.co.uk@gmail.com'  # The default email address to use for sending emails
EMAIL_DEBUG = True


# Email configuration
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'  # Your SMTP server address
# EMAIL_PORT = 587  # Your SMTP server port (587 is the default for SMTP with TLS)
# EMAIL_USE_TLS = True  # Whether to use TLS (True by default)
# EMAIL_HOST_USER = 'ekenehanson@gmail.com'
# EMAIL_HOST_PASSWORD = 'pduw cpmw dgoq adrp'
# DEFAULT_FROM_EMAIL = 'ekenehanson@gmail.com'
# EMAIL_DEBUG = True


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=15),

    "SIGNING_KEY": SECRET_KEY,

    "AUTH_HEADER_TYPES": ("Bearer",),

}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
] 

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'simupwsv_simulDB',         # Name of your mysql database
#         'USER': 'simupwsv_ekenehanson',        
#         'PASSWORD': '1234567890Qwerty1234567890',
#         'HOST': 'localhost',        
#         'PORT': '3306',   
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



