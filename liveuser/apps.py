from django.apps import AppConfig


class ExampleConfig(AppConfig):
    name = 'liveuser'

    def ready(self):
        import liveuser.signals