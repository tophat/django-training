from exercises.models import Textbook

def get_professor_all_names():
    """
    This function makes 11 queries when it really only needs one
    hint: # https://docs.djangoproject.com/en/2.1/ref/models/querysets/#select-related
    """
    prof_names = []
    for textbook in Textbook.objects.all():
        prof_names.append(textbook.author.first_name)
    return prof_names
