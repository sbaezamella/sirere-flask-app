from datetime import datetime

from flask import Blueprint, render_template, session
from flask_login import current_user, login_required

from sirere.models import Usuario, Paciente, FichaMedica, Examen, Diagnostico
from sirere import db


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.nombre)


@main.route('/examenes')
@login_required
def examenes():
    examenes = db.session.query(Examen.tipo, Examen.valor, Examen.fechaEmision).join(
        FichaMedica).join(Paciente).join(Usuario).filter(Usuario.nombre == current_user.nombre).all()

    return render_template('examenes.html', exam_click=True, examenes=examenes)


@main.route('/diagnosticos')
@login_required
def diagnosticos():
    diagnosticos = db.session.query(Diagnostico.categoriaDanio, Diagnostico.resultado, Diagnostico.descripcion, Diagnostico.fechaCreacion).join(
        FichaMedica).join(Paciente).join(Usuario).filter(Usuario.nombre == current_user.nombre).all()
    print(diagnosticos)
    print(diagnosticos[0])
    print(type(diagnosticos[0][2]))
    return render_template('diagnosticos.html', diagnosis_click=True, diagnosticos=diagnosticos)
