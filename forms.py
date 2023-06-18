from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, TextAreaField

class AddPetForm(FlaskForm):
    """Adding pet form"""

    name = StringField("Pet Name")
    species = StringField("Pet Species")
    age = FloatField("Pet Age")
    photo = StringField("Image URL")
    notes = TextAreaField("Notes")
    available = BooleanField("Available for Adoption", default=True)

