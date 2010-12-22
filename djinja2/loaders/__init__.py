from django.template.loader import make_origin
from django.template import TemplateDoesNotExist
from django.conf import settings

from djinja2.models import Jinja2Template

class Jinja2Loader(object):

    skip_dirs = getattr(settings, 'KEEP_DJANGO_TEMPLATES', ())

    def load_template(self, template_name, template_dirs=None):
        source, display_name = self.load_template_source(template_name, template_dirs)
        origin = make_origin(display_name, self.load_template_source, template_name, template_dirs)
        try:
            template = self.get_template_from_string(source, origin, template_name)
            return template, None
        except TemplateDoesNotExist:
            # If compiling the template we found raises TemplateDoesNotExist, back off to
            # returning the source and display name for the template we were asked to load.
            # This allows for correct identification (later) of the actual template that does
            # not exist.
            return source, display_name

    def is_keep_django_template(self, template_name):
        for prefix in self.skip_dirs:
            if template_name.startswith(prefix):
                return True
        return False

    def get_template_from_string(self, source, origin=None, name=None):
        if name and self.is_keep_django_template(name):
            raise TemplateDoesNotExist
        return Jinja2Template(source, name)
