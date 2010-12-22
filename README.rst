Jinja2 integration with Django

Features
========

* Template loaders
* makemessages_jinja command

Installation
============

Install from here using ``pip``::



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



