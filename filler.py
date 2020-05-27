from faker import Faker
fake = Faker()
# Set the seed value of the shared `random.Random` object
# across all internal generators that will ever be created
Faker.seed(0)

# Creates and seeds a unique `random.Random` object for
# each internal generator of this `Faker` instance
fake.seed_instance(0)

# Creates and seeds a unique `random.Random` object for
# the en_US internal generator of this `Faker` instance
fake.seed_locale('en_US', 0)

