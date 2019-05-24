from typing import List

from exercises.models import Professor


def get_professors(ids: List[int]) -> List[Professor]:
    profs = []
    for prof_id in ids:
        try:
            profs.append(Professor.objects.get(id=prof_id))
        except Professor.DoesNotExist:
            pass
    return profs
