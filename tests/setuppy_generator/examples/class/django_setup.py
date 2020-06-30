#!/usr/bin/env python
from setuppy_generator import BaseGenerator, raw

generator = BaseGenerator(
    name='name',
    version='1.0.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    include_package_data=True,
    long_description=raw("open('README.rst').read()"),
    scripts=['django/bin/django-admin.py'],
    install_requires=['pytz', 'sqlparse'],
    extras_require={
        "bcrypt": ["bcrypt"],
        "argon2": ["argon2-cffi >= 16.1.0"],
    },
    entry_points={'console_scripts': [
        'django-admin = django.core.management:execute_from_command_line',
    ]},
    project_urls={
        'Documentation': 'https://docs.djangoproject.com/',
        'Funding': 'https://www.djangoproject.com/fundraising/',
        'Source': 'https://github.com/django/django',
        'Tracker': 'https://code.djangoproject.com/',
    },
)
print(generator)
