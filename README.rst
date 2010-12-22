Django Jinja2 template engine integration.

Features
========

* Template loaders
* makemessages_jinja command
* Test runner

Installation
============

Install from here using ``pip``::

    pip install -e git+git://github.com/comoga/django-jinja2#egg=django-jinja2


Configuration
=============

Modify your ``settings.py``.
Add ``djinja2`` app to your ``INSTALLED_APPS``.

Configure template loaders. eg.::

TEMPLATE_LOADERS = (
    'djinja2.loaders.filesystem.Loader',
    'djinja2.loaders.app_directories.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

Django-jinja2 must be first. Exclude non-jinaj templates with
KEEP_DJANGO_TEMPLATES option in settings. eg.::

KEEP_DJANGO_TEMPLATES = (
    'admin/',
)



