from exercises.models import Professor


def update_professor_ages():
    for professor in Professor.objects.all():
        professor.age += 1
        professor.save()
