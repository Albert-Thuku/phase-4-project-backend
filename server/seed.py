from faker import Faker
from app import db, Animal, Centre, User, Adoption, app

fake = Faker()

def create_fake_animal(centre):
    name = fake.first_name()
    image = 'https://example.com/image.jpg'  # Replace with actual image URL
    description = fake.text()
    gender = fake.random_element(['Male', 'Female'])
    adopted = fake.boolean()

    animal = Animal(name=name, image=image, description=description, gender=gender, adopted=adopted, centre=centre)
    return animal

def create_fake_centre():
    name = fake.company()
    location = fake.address()

    centre = Centre(name=name, location=location)
    return centre

def create_fake_user():
    name = fake.name()
    age = fake.random_int(min=18, max=60)
    email = fake.email()
    password = fake.password(length=10)
    status = fake.random_element(['Active', 'Inactive'])

    user = User(name=name, age=age, email=email, password=password, status=status)
    return user

def create_fake_adoption(users, animals):
    user = fake.random_element(users)
    animal = fake.random_element(animals)

    adoption = Adoption(user=user, animal=animal)
    return adoption

def seed_database():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Create fake centres
        centres = []
        for _ in range(5):
            centre = create_fake_centre()
            centres.append(centre)
            db.session.add(centre)

        # Create fake animals
        animals = []
        for centre in centres:
            for _ in range(4):
                animal = create_fake_animal(centre)
                animals.append(animal)
                db.session.add(animal)

        # Create fake users
        users = []
        for _ in range(10):
            user = create_fake_user()
            users.append(user)
            db.session.add(user)

        # Create fake adoptions
        adoptions = []
        for _ in range(15):
            adoption = create_fake_adoption(users, animals)
            adoptions.append(adoption)
            db.session.add(adoption)

        db.session.commit()
        print('Database seeded successfully.')

if __name__ == '__main__':
    with app.app_context():
        seed_database()

