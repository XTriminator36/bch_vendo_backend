from django.apps import AppConfig


class BuyproductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Main'

    def ready(self):
        pass