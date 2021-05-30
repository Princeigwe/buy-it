"""
Django settings for buy_it project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import dj_database_url
#from decouple import config
#from braintree import Configuration, Environment

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

#SECRET_KEY = 'c-(er+$vt@2wo0xp_e(%qc_skl1$5ca+2wf&2&l907sn-ly(5x'
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'c-(er+$vt@2wo0xp_e(%qc_skl1$5ca+2wf&2&l907sn-ly(5x')


# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

#ALLOWED_HOSTS = ['buy-it-ecommerce.herokuapp.com']
ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    
    #local apps
    'corsheaders',
    'account.apps.AccountConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    'payments.apps.PaymentsConfig',
    'shop.apps.ShopConfig',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    
    #'stripe_payments.apps.StripePaymentsConfig'
    
    
    
]

AUTHENTICATION_BACKENDS = [
'django.contrib.auth.backends.ModelBackend',
'account.authentication.EmailAuthBackend',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'buy_it.urls'

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
                'cart.context_processors.cart',
            ],
        },
    },
]

#WSGI_APPLICATION = 'buy_it.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'buy_it_db',
    #     'USER': 'root',
    #     'PASSWORD': '',
    #     'HOST': '127.0.0.1',
    #     'PORT': '',
    #     'OPTIONS': {
    #         'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
    #     }
    # },
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'buy_it_db',
    #     'USER': 'skydata',
    #     'PASSWORD': '12345678',
    #     'HOST': '127.0.0.1',
    #     'PORT': '',
    # }
    

}

# Heroku: Update database configuration from $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
#DATABASES['default'] = dj_database_url.config(conn_max_age=600, default='postgres://wtgszukuxasdid:922ebd0c792295274fde5e073e964b756387e1000386551abbe4c3de27a95f57@ec2-54-158-232-223.compute-1.amazonaws.com:5432/dafv9sfmubqagb')



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#STATIC_URL = '/static/'


STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# The URL to use when referring to static files (where they will be served from)
STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


#cart key to store cart in the user session
CART_SESSION_ID = 'cart'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'buyitecommerce@gmail.com'
EMAIL_HOST_PASSWORD = '12abyz90'
EMAIL_USE_TLS = True
EMAIL_PORT = 587


##before running celery worker, open rabbitmq cmd and run rabbitmq-server
## when running celery worker, run it as:
## celery -A buy_it worker --pool=eventlet or..
## celery -A buy_it worker -l info -P eventlet
## Also run celery -A buy_it flower together with the former 

#########################################################################
## for linux:
## you can run the rabbitmq on the project terminal
## you can run it using " systemctl start rabbitmq-server.service "
## checking server details using " systemctl status rabbitmq-server.service "

# for linux:
# run celery as : "celery -A buy_it worker -l info"

## for linux:
## running xampp, run " cd /opt/lampp " press enter
##  then run "sudo ./manager-linux-x64.run"

# or just run "sudo /opt/lampp/manager-linux-x64.run"
## if apache server fails to start, run "sudo apachectl stop", and run the server again

## for monitoring celery operation, run " celery -A buy_it flower ", 
## then open "localhost:5555" on chrome

## activating virtual environment, run "source myenv/bin/activate"

RAVE_PUBLIC_KEY = "FLWPUBK_TEST-9a0419763aaa4cb0470adc8e8195629c-X"
RAVE_SECRET_KEY = "FLWSECK_TEST-05fd286ec89df9093b7e87afff9d7ae0-X"


LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'shop:product-list'


## run 'stripe listen --forward-to localhost:8000/stripe_webhook/' on terminal with internet, after creating the views and url

CELERY_BROKER_URL = "amqp://localhost"


# reducing staticfiles size
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#django_heroku.settings(locals())