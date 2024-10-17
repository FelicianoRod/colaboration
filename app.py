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

    # Validación de la raza

    # Validación del género

    # Validación de la ciudad

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
