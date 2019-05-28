from exercises.models import Professor


def update_professor_ages():
    """
    Increments all the professor's ages by one
    """
    for professor in Professor.objects.all():
        professor.age += 1
        professor.save()
