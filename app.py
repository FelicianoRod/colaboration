from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta'

class MascotaForm(FlaskForm):
    nombre = StringField('Nombre')
    edad = StringField('Edad')  # Cambiado a StringField para validación manual
    raza = StringField('Raza')
    genero = SelectField('Género', choices=[
        ('', 'Seleccione un género'),
        ('hembra', 'Hembra'),
        ('macho', 'Macho')
    ])
    ciudad = StringField('Ciudad')
    submit = SubmitField('Registrar Mascota')

def validar_formulario(form):
    errores = {}

    # ----------------- AQUÍ VALIDACIONES ------------------
    # Validación del nombre
    if not form.nombre.data or len(form.nombre.data.strip()) == 0:
        errores['nombre'] = 'El nombre es obligatorio'
    elif not form.nombre.data.replace(' ', '').isalpha():
        errores['nombre'] = 'El nombre solo puede contener letras'
    elif len(form.nombre.data) < 2 or len(form.nombre.data) > 50:
        errores['nombre'] = 'El nombre debe tener entre 2 y 50 caracteres'

    # Validación de la edad

    try:
        edad = int(form.edad.data)
        if edad < 0 or edad > 30:
            errores['edad'] = 'La edad debe estar entre 0 y 30 años'
    except ValueError:
        errores['edad'] = 'La edad debe ser un número entero'

    # Validación de la raza
    if not form.raza.data or len(form.raza.data.strip()) == 0:
        errores['raza'] = 'La raza es obligatoria'
    elif len(form.raza.data) < 2 or len(form.raza.data) > 50:
        errores['raza'] = 'La raza debe tener entre 2 y 50 caracteres'
    
    if not form.genero.data or form.genero.data == '':
        errores['genero'] = 'Debe seleccionar un género'
    elif form.genero.data not in ['hembra', 'macho']:
        errores['genero'] = 'Género no válido'

    # Validación de la ciudad

    if not form.ciudad.data or len(form.ciudad.data.strip()) == 0:
        errores['ciudad'] = 'La ciudad es obligatoria'
    elif not form.ciudad.data.replace(' ', '').isalpha():
        errores['ciudad'] = 'La ciudad solo puede contener letras'
    elif len(form.ciudad.data) < 2 or len(form.ciudad.data) > 50:
        errores['ciudad'] = 'La ciudad debe tener entre 2 y 50 caracteres'
    # ------------------------------------------------------
    return errores

@app.route('/', methods=['GET', 'POST'])
def registro_mascota():
    form = MascotaForm()
    errores = {}

    if request.method == 'POST':
        errores = validar_formulario(form)

        if not errores:
            # Aquí procesarías los datos del formulario
            flash('Mascota registrada exitosamente!', 'success')
            return redirect(url_for('registro_mascota'))

    return render_template('formulario.html', form=form, errores=errores)

if __name__ == '__main__':
    app.run(debug=True)
