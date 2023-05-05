from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    num_moons = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
                "id": self.id,
                "name": self.name,
                "description": self.description,
                "num_moons": self.num_moons
                }

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            name = data_dict["name"],
            description = data_dict["description"],
            num_moons = data_dict["num_moons"]
        )