# django-bootstrap-base-template

A common base template for Django web apps using Bootstrap

## Why?

I created this package because every time I start a new Django
web application it requires me to set up a very similar directory
structure for templates and static files. This Bootstrap base
template lets me quickly start a new Django project with all of
the assets I need already included.

Additionally, this package simplifies the process of updating the
static files used by multiple projects.

## Installation

```
pip install django-bootstrap-base-template
```

## Django settings.py

```
INSTALLED_APPS = [
    # ...
    'django_bootstrap_base_template',
    # ...
]
```

## my_template.html

```
{% extends 'bootstrap_base.html' %}

{% block body %}
    <!-- html content -->
{% endblock %}
```