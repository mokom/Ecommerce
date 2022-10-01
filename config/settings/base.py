import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-@%3t50gww1wudf$edzmmuc=q34pv28u(72&l!8neq&0e_56t23"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "yourdomain.com"]


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "store.apps.StoreConfig",
    "cart.apps.CartConfig",
    "account.apps.AccountConfig",
    "payment.apps.PaymentConfig",
    "orders.apps.OrdersConfig",
    "mptt",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "store.context_processors.categories",
                "cart.context_processors.cart",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

CART_SESSION_ID = "cart"


# Custom user model
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
AUTH_USER_MODEL = "account.Customer"
LOGIN_REDIRECT_URL = "/account/dashboard"
LOGIN_URL = "/account/login/"


# Email setting
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# Stripe Payment
os.environ.setdefault(
    "STRIPE_PUBLISHABLE_KEY",
    "pk_test_51JCUg3KvELx4Sm5hsZduoTWMBghBv5URhepTSx55zH7Bu2Cccnc6dO8r56xzy7TtcYsFyVpbH564ozEihRAWpyLT00pTGCmmv7",
)
STRIPE_SECRET_KEY = (
    "sk_test_51JCUg3KvELx4Sm5hfSomtogvUhgSZTH0bTL8AIO3tA3os8jQYXVxiDlJSD7ao07xiuwCLcZI2rIb4oCxaDTLI2DZ00KEgxP5bQ"
)

# PUBLSIHABLE_KEY = 'pk_test_51JCUg3KvELx4Sm5hsZduoTWMBghBv5URhepTSx55zH7Bu2Cccnc6dO8r56xzy7TtcYsFyVpbH564ozEihRAWpyLT00pTGCmmv7'
# SECRET_KEY = 'sk_test_51JCUg3KvELx4Sm5hfSomtogvUhgSZTH0bTL8AIO3tA3os8jQYXVxiDlJSD7ao07xiuwCLcZI2rIb4oCxaDTLI2DZ00KEgxP5bQ'

# Stripe Payment
STRIPE_ENDPOINT_SECRET = "whsec_d8e248991fd52176e35bba93738124cfc675805c858c8fd85557a411b65ceefd"
# Stripe listen --forward-to localhost:8000/payment/webhook/
