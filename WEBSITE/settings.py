from pathlib import Path
import os
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY", default="mahdi")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", cast=bool, default="True")
ALLOWED_HOSTS = ["*"]

# robots
ROBOTS_USE_HOST = False
ROBOTS_USE_SITEMAP = False

# sites framwork
SITE_ID = 1

# Application definition
INSTALLED_APPS = [
    "jazzmin",  # app
    # "multi_captcha_admin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",  # app
    "webArt.apps.WebartConfig",  # app
    "Artwork.apps.ArtworkConfig",  # app
    "Artist.apps.ArtistConfig",  # app
    "Artgallery.apps.ArtgalleryConfig",  # app
    "Accounts.apps.AccountsConfig",  # app
    "django_summernote",  # app
    "taggit",  # app
    "captcha",  # app
    "robots",  # app
    "compressor",  # app
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

ROOT_URLCONF = "WEBSITE.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "WEBSITE.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE"),
        "NAME": config("DB_NAME" ),
        "USER": config("DB_USER" ),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT", cast=int ),
    }
}

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


LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Tehran"

USE_I18N = True

USE_TZ = True


# تنظیمات مربوط به ریست کردن پسوورد و ارسال ایمیل
# for development
if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# for production
else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="ghezavatimahdi7@gmail.com")
    EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="sjtyxijlffjnzpqr")


# settings for >>> Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

# settings for >>> Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# برای زمان تعمیر و تغییرات دسترسی بسته باشه
MAINTENANCE_MODE = False

# تنظیم تم سامرنوت
SUMMERNOTE_THEME = "bs4"

# captcha for admin
MULTI_CAPTCHA_ADMIN = {
    "engine": "simple-captcha",
}


# STATICFILES_FINDERS به جنگو میگوید فایل استاتیک رو از کجا بگیره
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]

# Django Compressor Settings
COMPRESS_ENABLED = True
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_OFFLINE = (
    True  # برای سرعت سایت عالیه چون غیر از زمان ریکوعست کاربر فایل هارو فشرده میکنه
)
COMPRESS_URL = "/static/"

COMPRESS_CSS_FILTERS = ["compressor.filters.cssmin.CSSMinFilter"]
COMPRESS_JS_FILTERS = ["compressor.filters.jsmin.JSMinFilter"]


# تنظیمات قالب برای بخش ادمین
JAZZMIN_SETTINGS = {
    "show_ui_builder": False,  # اپشن تغییر تم
    "site_title": "login pannel ART life",
    "welcome_sign": "Welcome",
    "site_logo": "/img/pencil.jpg",
    "icons": {  # اینجا واسه بخش اپ میشه ایکون دلخواه تنظیم کرد برای هر اپ
        "auth.user": "fas fa-user",
        "Artwork.artwork": "fas fa-paint-brush",
        "Artist.artist": "fas fa-palette",
        "Artwork.category": "fas fa-tags",
        "Artwork.comments": "fas fa-comments",
        "Django_summernote": "fas fa-file-alt",
        "django_summernote.Attachment": "fas fa-paperclip",
        "taggit.tag": "fas fa-hashtag",
        "webArt.contact": "fas fa-address-book",
        "ArtGallery.Artgallery": "fas fa-pen",
    },
}

# تنظیمات مربوط به شکل تم بخش ادمین
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-secondary",
    "accent": "accent-warning",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": True,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-warning",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "cosmo",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success",
    },
    "actions_sticky_top": False,
}
# اندازه فیلد سامرنوت
SUMMERNOTE_CONFIG = {
    "width": "135%",
    "height": "900px",
}

# تنظیمات کانفیگ برای محیط انتشار
if config("USE_SSL_SETTINGS", cast=bool, default=False):
    # Https settings
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True

    # HSTS settings
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

    # more security settings
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = "SAMEORIGIN"
    SECURE_REFERRER_POLICY = "strict-origin"
    USE_X_FORWARDED_HOST = True
    SECURE_PROXY_SSL_HEADER = ("HTTPS_X_FORWARDED_PROTO", "https")


CSRF_COOKIE_SECURE = True
