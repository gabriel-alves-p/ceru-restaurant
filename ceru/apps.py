from django.apps import AppConfig


class CeruConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ceru'

    def ready(self):
        import ceru.signals
