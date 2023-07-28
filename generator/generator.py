from data.data import Person
from faker import Faker

fake = Faker()


def generated_person():
    yield Person(
        full_name=fake.first_name() + " " + fake.last_name(),
        email=fake.email(),
        current_addres=fake.street_name(),
        permanent_addres=fake.street_name()

    )
