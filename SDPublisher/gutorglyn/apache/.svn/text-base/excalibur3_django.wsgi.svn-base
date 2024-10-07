import os, sys

sys.path.append('C:/Users/lsrobert/Documents/shared work/external work/gutorGlyn/SDPublisher')
sys.path.append('C:/Users/lsrobert/Documents/shared work/external work/gutorGlyn/SDPublisher/gutorglyn')

import settings

import django.core.management
django.core.management.setup_environ(settings)
utility = django.core.management.ManagementUtility()
command = utility.fetch_command('runserver')

command.validate()

import django.conf
import django.utils

django.utils.translation.activate(django.conf.settings.LANGUAGE_CODE)

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
