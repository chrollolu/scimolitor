from django.core.management.base import BaseCommand, CommandError
from django.apps import apps

from . import seeders

class Command(BaseCommand):

    help = 'Help fix migrations problems & seeding the database.'

    def handle(self, *args, **options):
        seeders.pyClean()
        seeders.backupDB()
        seeders.vacuumDB()
        seeders.migradteDB()
        seeders.seedSuperUser()
        seeders.seedBien()
        seeders.seedEmploye()
        seeders.seedPost()
        seeders.seedGallery()
        seeders.seedClient()