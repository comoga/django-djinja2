from django.template.loaders.app_directories import Loader as DjangoLoader
from djinja2.loaders import Jinja2Loader

class Loader(Jinja2Loader, DjangoLoader):
    pass


