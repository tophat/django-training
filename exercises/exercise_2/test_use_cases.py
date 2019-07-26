from typing import List

import pytest

from exercises.models import Textbook, Professor, Subject
from exercises.exercise_2.use_cases import get_authors


@pytest.fixture
def names() -> List[str]:
    return ["Racuul", "Rif", "Sora"]


@pytest.fixture
def textbooks(names) -> List[Textbook]:
    textbooks = []
    for name in names:
        prof = Professor.objects.create(first_name=name, last_name="Isaac")
        textbook = Textbook.objects.create(
            title=f"General Chemistry", subject=Subject.objects.create(name="Chemistry")
        )
        textbook.authors.add(prof)
        textbooks.append(textbook)
    return textbooks


@pytest.mark.django_db()
def test_get_authors(django_assert_num_queries, textbooks, names):
    with django_assert_num_queries(2):
        profs_names = get_authors([t.id for t in textbooks])
        assert len(profs_names) == len(textbooks)
        assert profs_names == names
