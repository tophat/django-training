import pytest

from exercises.models import Textbook, Professor, Subject
from exercises.exercise_1.use_cases import get_textbook_subject


@pytest.fixture
def subject():
    return Subject.objects.create(name="Chemistry")


@pytest.fixture
def textbook(subject) -> Textbook:
    prof = Professor.objects.create(first_name="Bhil", last_name="Isaac")
    textbook = Textbook.objects.create(title=f"General Chemistry", subject=subject)
    textbook.authors.add(prof)
    return textbook


@pytest.mark.django_db()
def test_get_textbook_subject(django_assert_num_queries, textbook, subject):
    with django_assert_num_queries(1):
        actual_subject = get_textbook_subject(textbook.id)
        assert actual_subject == subject.name
