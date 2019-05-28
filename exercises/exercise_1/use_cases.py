from exercises.models import Textbook


def get_textbook_subject(textbook_id) -> str:
    """
    :param textbook_id: Specifies which textbook to lookup
    :return: Get the subject of a textbook
    """
    return Textbook.objects.get(id=textbook_id).subject.name
