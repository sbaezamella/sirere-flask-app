from flask import Blueprint, render_template
from flask_login import current_user, login_required

from sirere import db
from sirere.models import Diagnostico, Examen, FichaMedica, Paciente, Usuario

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def get_profile():
    return render_template('profile.html', name=current_user.nombre)


@main.route('/examenes')
@login_required
def get_examenes():
    examenes = db.session.query(Examen.tipo, Examen.valor, Examen.fechaEmision).join(
        FichaMedica).join(Paciente).join(Usuario).filter(Usuario.nombre == current_user.nombre).all()

    return render_template('examenes.html', exam_click=True, examenes=examenes)


@main.route('/diagnosticos')
@login_required
def get_diagnosticos():
    diagnosticos = db.session.query(Diagnostico.categoriaDanio, Diagnostico.resultado, Diagnostico.descripcion, Diagnostico.fechaCreacion).join(
        FichaMedica).join(Paciente).join(Usuario).filter(Usuario.nombre == current_user.nombre).all()
    return render_template('diagnosticos.html', diagnosis_click=True, diagnosticos=diagnosticos)
