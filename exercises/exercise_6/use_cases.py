from exercises.models import Professor


def get_professor(first_name: str) -> Professor:
    """
    :param first_name: Specified first name
    :return: Professor with a matching first name
    """
    return Professor.objects.filter(first_name=first_name)
