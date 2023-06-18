from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):

    __tablename__ = "pets"

    def __repr__(self):
        """Shows pet info"""
        return f"Hi my name is {self.name} and I am a {self.age} years old {self.species}"
    
    id = db.Column(db.Integer,
                   autoincrement =  True,
                   primary_key = True)
    
    name = db.Column(db.Text,
                     nullable = False,
                     unique = True)
    
    species = db.Column(db.Text,
                        nullable = False)
    
    photo_url = db.Column(db.Text)

    age = db.Column(db.Integer)

    notes = db.Column(db.Text)

    available = db.Column(db.Boolean,
                          nullable = False,
                          default = True)
    
    def delete_pet(self):
        """Deletes a pet"""
        db.session.delete(self)
        db.session.commit()