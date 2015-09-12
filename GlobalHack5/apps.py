from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "GlobalHack5"

    def ready(self):
        import_module("GlobalHack5.receivers")
