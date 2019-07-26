from typing import Tuple, List

from exercises.models import Professor

FullName = Tuple[str, str]


def add_new_professors(names: List[FullName]):
    """
    Creates multiple professors
    :param names: Tuple of first and last names
    """
    for first_name, last_name in names:
        Professor.objects.create(first_name=first_name, last_name=last_name)
