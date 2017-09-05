# django-bootstrap-base-template

A common base template for Django web apps using Bootstrap

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