Django Jinja2 template engine integration.

Features
========

* Template loaders
* makemessages_jinja command
* test runner

Installation
============

``Djinja2`` requires ``Django 1.3`` and ``chouwa``.

::

    pip install chouwa

Install from here using ``pip``::

    pip install -e git+git://github.com/comoga/django-djinja2#egg=django-djinja2


Configuration
=============

Modify your ``settings.py``.
Add ``djinja2`` app to your ``INSTALLED_APPS``.

Configure template loaders.
``Djinja2`` loader must come before ``django`` original loaders.

::

    TEMPLATE_LOADERS = (
        'djinja2.loaders.filesystem.Loader',
        'djinja2.loaders.app_directories.Loader',
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

Exclude non-jinja (admin site ...) templates with ``KEEP_DJANGO_TEMPLATES`` option in your settings.
``Djinja2`` loaders skip any template which path begins with specified prefixes.
For example to skip admin site templates use::

    KEEP_DJANGO_TEMPLATES = (
        'admin/',
    )

Optionally run tests with ``Jinja2TestSuiteRunner`` to have correctly instrumented template render.

Usage
=====

You can use all `Jinja2 <http://jinja.pocoo.org/>`_ and
`chouwa <http://bitbucket.org/trevor/chouwa/>`_ features (chouwa decorators, jinja_globals.py in each app ...)

To create or update a localization message file use ``makemessagesjinja`` command instead.

