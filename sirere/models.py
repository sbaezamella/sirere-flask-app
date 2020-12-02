from flask_login import UserMixin

from sirere import db


class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.Text, nullable=False, default='0')
    nombre = db.Column(db.Text, nullable=False, default='0')
    direccion = db.Column(db.Text, nullable=False, default='0')
    email = db.Column(db.Text, nullable=False, default='0')
    telefono = db.Column(db.Text, nullable=False, default='0')
    contrasena = db.Column(db.Text,  nullable=True)
    fechaCreacion = db.Column(db.DateTime(
        timezone=True), server_default=db.func.current_timestamp())

    def __repr__(self):
        return f'<User {self.nombre}>'


class Personal(db.Model):
    __tablename__ = 'personal'
    id = db.Column(db.Integer, primary_key=True)
    idUsuario = db.Column(db.Integer, db.ForeignKey(
        'usuario.id'), nullable=False, default='0')
    tipoPersonal = db.Column(db.Integer, nullable=False, default='0')


class Paciente(db.Model):
    __tablename__ = 'paciente'
    id = db.Column(db.Integer, primary_key=True)
    idUsuario = db.Column(db.Integer, db.ForeignKey(
        'usuario.id'), nullable=False, default='0')
    fechaNacimiento = db.Column(db.DateTime, nullable=False)
    emailAlternativo = db.Column(db.Text, nullable=False, default='0')
    telefonoAlternativo = db.Column(db.Text, nullable=False, default='0')
    prevision = db.Column(db.Integer,  nullable=True)
    nacionalidad = db.Column(db.Text, nullable=True)


class FichaMedica(db.Model):
    __tablename__ = 'fichamedica'
    id = db.Column(db.Integer, primary_key=True)
    idPaciente = db.Column(db.Integer, db.ForeignKey(
        'paciente.id'), nullable=False, default='0')
    sexo = db.Column(db.Integer, nullable=False, default='0')
    peso = db.Column(db.Integer, nullable=False, default='0')
    altura = db.Column(db.Integer, nullable=False, default='0')
    etnia = db.Column(db.Integer, nullable=False, default='0')
    fechaCreacion = db.Column(db.DateTime, nullable=True)


class Examen(db.Model):
    __tablename__ = 'examen'
    id = db.Column(db.Integer, primary_key=True)
    idFicha = db.Column(db.Integer, db.ForeignKey(
        'fichamedica.id'), nullable=False)
    fechaEmision = db.Column(db.DateTime, nullable=True)
    tipo = db.Column(db.Integer, nullable=True)
    valor = db.Column(db.Integer, nullable=True)


class Diagnostico(db.Model):
    __tablename__ = 'diagnostico'
    id = db.Column(db.Integer, primary_key=True)
    idFicha = db.Column(db.Integer, nullable=False)
    fechaCreacion = db.Column(db.DateTime, nullable=True)
    fechaActualizacion = db.Column(db.DateTime, nullable=True)
    resultado = db.Column(db.Integer, nullable=True)
    descripcion = db.Column(db.Text)
    categoriaDanio = db.Column(db.Integer, nullable=True)
