import pytest

from exercises.models import Textbook, Professor, Subject
from exercises.exercise_2.use_cases import get_authors


@pytest.fixture
def textbooks():
    textbooks = []
    for i in range(3):
        prof = Professor.objects.create(
            first_name=f"Jacob the {i}",
            last_name="Isaac",
        )
        textbook = Textbook.objects.create(
            title=f"General Chemistry {i}",
            subject=Subject.objects.create(name="Chemistry"),
        )
        textbook.authors.add(prof)
        textbooks.append(textbook)
    return textbooks


@pytest.mark.django_db()
def test_get_authors(django_assert_num_queries, textbooks):
    with django_assert_num_queries(2):
        profs = get_authors([t.id for t in textbooks])
        assert len(profs) == len(textbooks)
