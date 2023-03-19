import json
import os
import yaml
# from decouple import config
from datetime import datetime

from faker import Faker

from django.contrib.auth import get_user_model
from django.apps import apps
from django.core import management
from tqdm import tqdm
from django.utils.text import slugify
from django.core.files import File

# import Models for seeding
from scimolitor.settings import BASE_DIR

# import Others variables
from . import vars


# Yaml config file
centre_sante_config_data = BASE_DIR.joinpath('config.yaml')



def jsonFileToData(file):
    out = None
    with open(file, 'r') as f:
        out = json.load(f)
    return out

def yamlFileToData(file):
    out = None
    with open(file, 'r') as f:
        out = yaml.safe_load(f)
    return out

def uploadFile(f):
    from django.core.files import File
    file_obj = File(open(f))

def pyClean():
    import os
    os.system('find . -type f -name "*.py[co]" -delete')
    os.system('find . -type d -name "__pycache__" -delete')
    os.system('find . -type f -name "db.sqlite3" -delete')

def backupDB():
    # Prevent failure if not database initialized yet!!! sqlite or first start
    try:
        management.call_command('makemigrations')
    except:
        pass

    try:
        management.call_command('migrate')
    except:
        pass

    try:
        management.call_command('migrate', '--run-syncdb')
    except:
        pass

    print('Backing up database...')

    apps_excluded = [
        'jazzmin' ,
        'admin' ,
        'contenttypes' ,
        'auth' ,
        'sessions' ,
        'messages' ,
        'staticfiles' ,
        'sites' ,
        'rest_framework' ,
        'token_blacklist' ,
        'corsheaders' ,
        'rest_framework_simplejwt' ,
        'django_filters' ,
        'django_rest_passwordreset' ,
        'users' ,
        'drf_yasg' ,
        'django_db_logger' ,
        'debug_toolbar' ,
        'inspectdb_refactor' ,
        'import_export' ,
    ]

    all_apps = [ x for x in apps.all_models]

    apps_to_backup = []

    # Filter app to backup
    for app in all_apps:
        if app not in apps_excluded:
            apps_to_backup.append(app)
    # Generate output filename
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    heure = now.hour
    minute = now.minute
    second = now.second
    outputfile = f'./fixtures/fixture_backup_{year}-{month}-{day}-{heure}-{minute}-{second}.json'

    # Building Argv
    argv = ['manage.py', 'dumpdata', '--indent=2', f'--output={outputfile}']
    for app in apps_to_backup:
        app_models = apps.get_app_config(app).models
        for x in app_models:
            model_string = f'{app}.{x}'
            argv.append(model_string)
    management.execute_from_command_line(argv=
        argv
    )

def vacuumDB():
    print('Flushing the current database :')
    management.call_command('flush', '--noinput')

    print('Flushing the current database... OK')

def migradteDB():
    print('Migrating database...')
    try:
        management.call_command('makemigrations')
        management.call_command('migrate', '--run-syncdb')
    except:
        print('*************** Error Applying Migrations ****************')
    # management.call_command('migrate', '--fake-initial')

    print('Migrating database... OK')

def seedSuperUser():
    print('Creating admin user...')
    UserModel = get_user_model()
    UserModel.objects.create_superuser( vars.super_user['username'], vars.super_user['email'], vars.super_user['password'])
    print('Creating admin user... OK')


# -------------------------- Seed Bien ---------------------------------------#
from web.models import Bien
def seedBien():
    data = vars.bien
    for x in tqdm(data, desc='Seeding Bien...'):
        tmp_bien = Bien()
        tmp_bien.title = x['titre']
        tmp_bien.location = x['location']
        tmp_bien.body = x['body']
        tmp_bien.image.save('file.jpg', File(open(x['image'], 'rb')))
        
    print('Seeding Bien... OK')
# -------------------------- Seed Bien ---------------------------------------#


# -------------------------- Seed Employe ---------------------------------------#

from web.models import Employe
def seedEmploye():
    data = vars.employe
    for x in tqdm(data, desc='Seeding Employe...'):
        tmp_employe = Employe()
        tmp_employe.titre = x['titre']
        tmp_employe.nom = x['nom']
        tmp_employe.fonction = x['fonction']
        tmp_employe.mobile = x['mobile']
        tmp_employe.email = x['email']
        tmp_employe.image.save('file.jpg', File(open(x['image'], 'rb')))
        tmp_employe.save()
        
    print('Seeding Employe... OK')
# -------------------------- Seed Employe ---------------------------------------#

# -------------------------- Seed Post ---------------------------------------#

from web.models import Post
def seedPost():
    data = vars.post
    for x in tqdm(data, desc='Seeding Post...'):
        tmp_post = Post()
        tmp_post.title = x['title']
        tmp_post.body = x['body']
        tmp_post.status = 'PB'
        tmp_post.author = get_user_model().objects.first()
        tmp_post.image.save('file.jpg', File(open(x['image'], 'rb')))
        
    print('Seeding Post... OK')
# -------------------------- Seed Post ---------------------------------------#

# -------------------------- Seed Gallery ---------------------------------------#

from web.models import Gallery
def seedGallery():
    data = vars.gallery
    for x in tqdm(data, desc='Seeding Gallery...'):
        tmp_gallery = Gallery()
        tmp_gallery.titre = x['titre']
        tmp_gallery.image.save('file.jpg', File(open(x['image'], 'rb')))
        
    print('Seeding Gallery... OK')
# -------------------------- Seed Gallery ---------------------------------------#

# -------------------------- Seed Client ---------------------------------------#

from web.models import Client
def seedClient():
    data = vars.client
    for x in tqdm(data, desc='Seeding Client...'):
        tmp_client = Client()
        tmp_client.nom = x['nom']
        tmp_client.image.save('file.jpg', File(open(x['image'], 'rb')))
        
    print('Seeding Client... OK')
# -------------------------- Seed Client ---------------------------------------#

