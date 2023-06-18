from flask import Flask, render_template, redirect, session, flash
from models import Pet, connect_db, db
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretpets'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_RECORD_QUERIES'] = True
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['DEBUG_TB_ENABLED'] = True

debug = DebugToolbarExtension(app)

with app.app_context():
    connect_db(app)
    db.create_all()


@app.route('/')
def homepage():
    pets = Pet.query.all()
    return render_template('homepage.html', pets=pets)

@app.route('/add_pet', methods=['GET', 'POST'])
def add_pet():

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        photo_url = form.photo.data
        new_pet = Pet(name=name, age=age, species=species, notes=notes, available=available, photo_url=photo_url)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet.html', form=form)
    

@app.route('/<int:pet_id>')
def pet_page(pet_id):
    pet = Pet.query.get_or_404(pet_id)

    return render_template('pet.html', pet=pet)

@app.route('/delete_pet/<int:pet_id>', methods=['GET', 'POST'])
def delete_pet(pet_id):
    pet = Pet.query.get(pet_id)
    Pet.delete_pet(pet)

    return  redirect('/')

@app.route('/<int:pet_id>/edit', methods=['GET','POST'])
def edit_pet(pet_id):
    
    pet = Pet.query.get(pet_id)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo.data
        db.session.commit()

        return redirect(f'/{pet.id}')
    else:
        return render_template('edit_pet.html', pet=pet, form=form)
