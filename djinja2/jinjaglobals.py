import jinja2
from jinja2.utils import Markup, escape

from django.core.urlresolvers import reverse
from django.conf import settings

from chouwa.decorators import jinjaglobal, jinjafilter

@jinjaglobal
@jinja2.contextfunction
def csrf_token_tag(context):
    csrf_token = context.get('csrf_token', None)
    code = ''
    if csrf_token:
        if csrf_token != 'NOTPROVIDED':
            code = '<input type="hidden" name="csrfmiddlewaretoken" value="%s" />' % csrf_token
    return Markup(code)


@jinjaglobal
def url(viewname, *args, **kwargs):
    '''
    Lookup a url via `django.core.urlresolvers.reverse`.

    :Parameters:
      viewname : str
        The label associated with a url or the dotted path module name
        of a view.
    '''
    return reverse(viewname, settings.ROOT_URLCONF, args, kwargs)


@jinjafilter
def linebreaksbr(value):
    escaped_lines = []
    for line in value.split('\n'):
        escaped_lines.append(escape(line))
    escaped = "<br/>".join(escaped_lines)
    return Markup(escaped)


