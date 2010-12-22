from django.template.loaders.filesystem import Loader as DjangoLoader
from djinja2.loaders import Jinja2Loader

class Loader(Jinja2Loader, DjangoLoader):
    pass
