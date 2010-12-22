from django import template
from django.template import loader, TemplateDoesNotExist
from django.template.loader import template_source_loaders
from djinja2.loaders import Jinja2Loader

register = template.Library()


class JinjaTemplateNode(template.Node):
    def __init__(self, template_name):
        self.template_name = template_name

    def find_template(self, name):
        for loader in template_source_loaders:
            if not isinstance(loader, Jinja2Loader):
                continue
            try:
                #NOT THREAD SAFE
                loader.skip_dirs_original = loader.skip_dirs
                loader.skip_dirs = []
                template = loader(name, None)[0]
                if hasattr(template, 'render'):
                    return template
            except TemplateDoesNotExist:
                pass
            finally:
                loader.skip_dirs = loader.skip_dirs_original
        raise TemplateDoesNotExist()

    def render(self, context):
        template = self.find_template(self.template_name)
        return template.render(context)

@register.tag
def include_jinja(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, template_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires a single argument" % tag_name
    if template_name[0] == template_name[-1] and template_name[0] in ('"', "'"):
        template_name = template_name[1:-1]
    return JinjaTemplateNode(template_name)
