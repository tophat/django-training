from typing import List

from exercises.models import Textbook


def get_authors(textbook_ids: List[int]) -> List[str]:
    """
    :param textbook_ids: List of ids of textbooks to lookup
    :return: Returns the author's first name of all the specified textbooks
    """
    prof_names = []
    for textbook in Textbook.objects.filter(id__in=textbook_ids):
        for author in textbook.authors.all():
            prof_names.append(author.first_name)
    return prof_names
