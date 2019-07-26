from typing import Tuple, List

from exercises.models import Professor

NameUpdate = Tuple[int, str]


def update_professor_first_names(first_name_updates: List[NameUpdate]):
    """
    Updates all the professors' first names to the string specified
    :param first_name_updates: List of tuples of prof ID and new first name
    """
    for prof_id, new_first_name in first_name_updates:
        prof = Professor.objects.get(id=prof_id)
        prof.first_name = new_first_name
        prof.save()
