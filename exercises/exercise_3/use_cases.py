from exercises.models import Professor


def remove_pii():
    """
    Remove all personally identifiable information from the DB by redacting all
    the professor information
    :return:
    """
    for professor in Professor.objects.all():
        professor.first_name = "REDACTED"
        professor.last_name = "REDACTED"
        professor.save()
