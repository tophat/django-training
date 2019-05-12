from exercises.models import Professor


def add_new_professors(names):
    for first_name, last_name in names:
        Professor.objects.create(
            first_name=first_name,
            last_name=last_name,
        )
