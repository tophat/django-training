from exercises.models import Professor


def remove_pii():
    for professor in Professor.objects.all():
        professor.first_name = "REDACTED"
        professor.last_name = "REDACTED"
