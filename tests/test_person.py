from beings import Person

import pytest

@pytest.fixture()
def person():
    return Person("Ethan Smith", 24, jobs=["Software Engineer"])
def test_init(person : Person):
    assert person.name == "Ethan Smith"
    assert person.age == 24
    assert person.jobs == ["Software Engineer"]

def test_forename(person: Person):
    assert person.forename == "Ethan"

def test_surename(person: Person):
    assert person.surname == "Smith"

def test_no_surename(person: Person):
    person.name = "Ethan"
    assert not person.surname


def test_celebrate_birthdaY(person: Person):
    person.celebrate_birthday()
    assert person.age==25

def test_add_job(person: Person):
    person.add_job("Zookeeper")
    assert person.jobs == ["Software Engineer","Zookeeper" ]