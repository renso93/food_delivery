from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ["172.0.01", "localhost"]

INSTALLED_APPS += [
    "debug_toolbar",
]


MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]
INTERNAL_IPS = ["172.0.0.1", "localhost", ]

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Email backend for development
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
#EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025
EMAIL_USE_TLS = False
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
DEFAULT_FROM_EMAIL = "webmaster@localhost"
DEFAULT_TO_EMAIL = "admin@localhost"
SERVER_EMAIL = "server@localhost"

# Celery configuration for development
CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"
CELERY_TIMEZONE = TIME_ZONE
CELERY_ENABLE_UTC = True
CELERY_TASK_ALWAYS_EAGER = True  # Exécute les tâches de manière synchrone pour le développement
CELERY_TASK_EAGER_PROPAGATES = True  # Propage les exceptions pour le débogage


# Django Debug Toolbar settings
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,
    "DISABLE_PANELS": [
        "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    ],
}

# Logging configuration for development
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
}

# Specific loggers for development
LOGGING["loggers"] = {
    "django.db.backends": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
    "celery": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
}