from exercises.models import Textbook


def get_all_professor_names():
    prof_names = []
    for textbook in Textbook.objects.all():
        for author in textbook.authors.all():
            prof_names.append(author.first_name)
    return prof_names
