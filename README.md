# dj_admin_bootstrapped

This project gives a new UI for django projects!

Here are some examples:
![Login](https://cdn.rawgit.com/carlosmart626/dj_admin_bootstrapped/master/media/dj_admin_bootstrapped-1.png)
![IndexAdmin](https://cdn.rawgit.com/carlosmart626/dj_admin_bootstrapped/master/media/dj_admin_bootstrapped-2.png)
![ModelIndex](https://cdn.rawgit.com/carlosmart626/dj_admin_bootstrapped/master/media/dj_admin_bootstrapped-3.png)
![ModelIndexNoInstances](https://cdn.rawgit.com/carlosmart626/dj_admin_bootstrapped/master/media/dj_admin_bootstrapped-4.png)

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