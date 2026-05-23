from . import db

class Usuarios(db.Model):

    __tablename__ = 'Usuarios'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    apodo = db.Column(db.String(100), unique=True)
    nombre = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    cedula = db.Column(db.Integer, unique=True)
    password = db.Column(db.String(100))
    rol = db.Column(db.String(50))
    creacion = db.Column(db.DateTime)
    estado = db.Column(db.Boolean)
    clients = db.relationship('Clientes', backref='user', lazy=True)
    prestamos = db.relationship('Prestamo', backref='user', lazy=True)

class Clientes(db.Model):

    __tablename__ = 'Clientes'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nombre = db.Column(db.String(100))
    cedula = db.Column(db.Integer, unique=True)
    telefono = db.Column(db.Integer, unique=True)
    direccion = db.Column(db.String(100))
    creacion = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)


class Prestamos(db.Model):

    __tablename__ = 'Prestamos'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    monto = db.Column(db.Float)
    interes = db.Column(db.Float)
    total_pagar = db.Column(db.Float)
    cuotas = db.Column(db.Integer)
    frecuencia = db.Column(db.String(100))
    fecha_inicio = db.Column(db.Date)
    estado = db.Column(db.String(100), default='activo')


class Cuotas(db.Model):

    __tablename__ = 'Cuotas'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    prestamo_id = db.Column(db.Integer, db.ForeignKey('prestamos.id'), nullable=False)
    numero_cuota = db.Column(db.Integer)
    fecha_pago = db.Column(db.Date)
    monto = db.Column(db.Float)
    estado = db.Column(db.String(100), default='pendiente')

    __table_args__ = (
        db.ForeignKeyConstraint(['prestamo_id'], ['prestamos.id']),
    )


class Pagos(db.Model):

    __tablename__ = 'Pagos'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cuota_id = db.Column(db.Integer, db.ForeignKey('cuotas.id'), nullable=False)
    fecha = db.Column(db.DateTime, default=db.func.current_timestamp())
    monto_pagado = db.Column(db.Float)
    metodo_pago = db.Column(db.String(100))

    __table_args__ = (
        db.ForeignKeyConstraint(['cuota_id'], ['cuotas.id']),
    )

class Garantias(db.Model):

    __tablename__ = 'Garantias'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    prestamo_id = db.Column(db.Integer, db.ForeignKey('prestamos.id'), nullable=False)
    descripcion = db.Column(db.Text)
    valor_estimado = db.Column(db.Float)

    __table_args__ = (
        db.ForeignKeyConstraint(['prestamo_id'], ['prestamos.id']),
    )