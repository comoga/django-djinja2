from chouwa.environment import env

def context_to_dict(ctxt):
    """Translates context for jinja2.
    In case ctxt is dictionary, it returns it with no change.
    """
    if isinstance(ctxt, dict):
        return ctxt
    res = {}
    for d in reversed(ctxt.dicts):
        res.update(d)
    return res


class Jinja2Template(object):
    "Jinja2 template object to Django template object adapter"

    def __init__(self, source, name=None):
        self.template = env.from_string(source)
        self.template.name = name
        self.name = name

    def render(self, context):
        context = context_to_dict(context)
        return self.template.render(context)