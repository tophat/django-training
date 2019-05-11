import pytest

from exercises.models import Textbook, Professor, Subject
from exercises.exercise_2.use_cases import get_all_professor_names

@pytest.mark.django_db()
def test_get_professor_names(django_assert_num_queries):
    expected_num_textbooks = 10
    for i in range(expected_num_textbooks):
        prof = Professor.objects.create(first_name=f"Jacob the {i}", last_name="Isaac")
        Textbook.objects.create(
            title=f"General Chemistry {i}",
            subject=Subject.objects.create(name="Chemistry"),
        ).authors.add(prof)

    with django_assert_num_queries(2):
        profs = get_all_professor_names()
        assert len(profs) == expected_num_textbooks
