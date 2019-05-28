import pytest

from exercises.exercise_6.use_cases import get_professor
from exercises.models import Professor


@pytest.fixture
def profs():
    Professor.objects.create(first_name="joe", last_name="Shmoe")
    Professor.objects.create(first_name="a", last_name="ElRair")
    Professor.objects.create(first_name="will", last_name="Arner")


@pytest.mark.django_db()
def test_get_professor(profs):
    profs = get_professor("joe")
    assert profs[0].first_name == "joe"
    assert "SCAN TABLE" not in profs.explain()
