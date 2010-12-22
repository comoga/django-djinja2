Django Jinja2 template engine integration.

Features
========

* Template loaders
* makemessages_jinja command
* Test runner

Installation
============

Requires chouwa and Django 1.3::

    pip install chouwa

Install from here using ``pip``::

    pip install -e git+git://github.com/comoga/django-djinja2#egg=django-djinja2


Configuration
=============

Modify your ``settings.py``.
Add ``djinja2`` app to your ``INSTALLED_APPS``.

Configure template loaders. ``Djinja2`` loader must be before ``django`` original loaders.::

    TEMPLATE_LOADERS = (
        'djinja2.loaders.filesystem.Loader',
        'djinja2.loaders.app_directories.Loader',
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

Exclude non-jinja (admin site ...) templates with ``KEEP_DJANGO_TEMPLATES`` option in your settings. Eg.::

    KEEP_DJANGO_TEMPLATES = (
        'admin/',
    )

Usage
=====

You can use all ``chouwa`` features (chouwa decorators, jinja_globals.py in each app ...)

