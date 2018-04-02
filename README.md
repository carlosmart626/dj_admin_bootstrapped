# dj_admin_bootstrapped

This project gives a new UI for django projects!

Here are some examples:

## Instalation
```bash
pip install dj_admin_bootstrapped
```

## Usage
In your settings add app `dj_admin_bootstrapped` before admin
```python
INSTALLED_APPS = [
    'dj_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```