from exercises.models import Textbook


def get_all_subjects():
    subjects = []
    for textbook in Textbook.objects.all():
        subjects.append(textbook.subject.name)
    return subjects
