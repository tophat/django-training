from typing import List

from exercises.models import Professor


def get_professors(ids: List[int]) -> List[Professor]:
    """
    :param ids: Specified professors
    :return: Get a list of Professors by id
    """
    profs = []
    for prof_id in ids:
        try:
            profs.append(Professor.objects.get(id=prof_id))
        except Professor.DoesNotExist:
            pass
    return profs
