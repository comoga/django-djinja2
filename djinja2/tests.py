from django.test.simple import DjangoTestSuiteRunner
from django.test import signals
from djinja2.models import Jinja2Template


__all__ = ('Jinja2TestSuiteRunner', )

def instrumented_render(self, context):
    signals.template_rendered.send(sender=self, template=self, context=context)
    return self._render(context)

class Jinja2TestSuiteRunner(DjangoTestSuiteRunner):
    """Allows use test assertTemplateUsed in test"""

    def setup_test_environment(self):
        super(Jinja2TestSuiteRunner, self).setup_test_environment()
        Jinja2Template._render = Jinja2Template.render
        Jinja2Template.render = instrumented_render

