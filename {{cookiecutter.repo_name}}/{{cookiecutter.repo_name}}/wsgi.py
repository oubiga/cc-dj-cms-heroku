"""
WSGI config for {{ cookiecutter.project_name }} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from dj_static import Cling


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ cookiecutter.repo_name }}.settings")
application = Cling(get_wsgi_application())
