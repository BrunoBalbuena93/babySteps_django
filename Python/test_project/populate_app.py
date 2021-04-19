import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_project.settings")

import django
django.setup()

import random
from test_app.models import Users
from faker import Faker

fakegen = Faker("es_MX")

def populate(N=10):
    for entry in range(N):
        fullname = fakegen.name()
        email = fakegen.email()
        # filling up the data
        Users.objects.get_or_create(name=fullname[:fullname.index(" ")], last_name=fullname[fullname.index(" ") + 1:], email=email)

if __name__ == "__main__":
    print("Creando usuarios")
    populate()
    print("Hemos concluido")