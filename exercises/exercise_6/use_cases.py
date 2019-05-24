from django.db.models.query import QuerySet

from exercises.models import Professor


def get_professor(first_name: str) -> QuerySet:
    return Professor.objects.filter(first_name=first_name)
