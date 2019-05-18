from django.apps import AppConfig


class ChildproductConfig(AppConfig):
    name = 'childproduct'

    def ready(self):
        import childproduct.signals
