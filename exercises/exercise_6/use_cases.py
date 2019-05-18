from exercises.models import Professor


def get_professor(first_name):
    return Professor.objects.filter(first_name=first_name)
