import environ
import os

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()

...

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
			...
		'app',
]
DATABASES = {
    # read os.environ['DATABASE_URL'] and raises
    # ImproperlyConfigured exception if not found
    'default': env.db(),

}




