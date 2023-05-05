import pytest
from app import create_app, db
from flask.signals import request_finished
from app.models.planet import Planet


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def one_planet(app):
    planet =  Planet(
        name = "Mercury",
        description = "It's the first planet in our solar system",
        num_moons = 0
    )
    db.session.add(planet)
    db.session.commit()
    return planet


@pytest.fixture
def saved_planets(app, one_planet):
    planet_two = Planet(name = "Venus",
        description = "It's the second planet in our solar system",
        num_moons = 0)
    planet_three = Planet(name = "Earth",
        description = "It's the third planet in our solar system",
        num_moons = 1)

    db.session.add_all([one_planet, planet_two, planet_three])
    db.session.commit()
