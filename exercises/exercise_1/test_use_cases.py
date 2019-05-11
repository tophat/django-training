import pytest

from exercises.models import Textbook, Professor, Subject
from exercises.exercise_1.use_cases import get_all_subjects

@pytest.mark.django_db()
def test_get_all_subjects(django_assert_num_queries):
    expected_num = 10
    for i in range(expected_num):
        prof = Professor.objects.create(first_name=f"Jacob the {i}", last_name="Isaac")
        Textbook.objects.create(
            title=f"General Chemistry {i}",
            subject=Subject.objects.create(name="Chemistry"),
        ).authors.add(prof)

    with django_assert_num_queries(1):
        """
        This function makes 11 queries when it really only needs one
        hint: # https://docs.djangoproject.com/en/2.1/ref/models/querysets/#select-related
        """
        profs = get_all_subjects()
        assert len(profs) == expected_num
