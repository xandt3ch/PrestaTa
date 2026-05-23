from flask import  Blueprint, render_template, url_for, redirect, request, flash
from app import db
from app.models import Usuarios, Clientes, Prestamos, Cuotas, Pagos


main = Blueprint('main',__name__)
auth = Blueprint('auth',__name__)

#ruta de inicio
@main.route('/')
def dashboard():
    return render_template('index.html')

# ruta de prestamo
@main.route('/prestamo')
def prestamo():
    prestamos = Prestamos.query.all()
    return render_template('prestamo.html', prestamos=prestamos)
    return render_template('prestamo.html')

# ruta plus
@main.route('/plus')
def plus():
    return render_template('plus.html')

#ruta cliente
@main.route('/cliente')
def cliente():
    clientes = Clientes.query.all()
    return render_template('cliente.html', clientes=clientes)

# ruta de pago
@main.route('/pago')
def pago():
    pagos = Pagos.query.all()
    return render_template('pago.html', pagos=pagos)        
    return render_template('pago.html')

# ruta de configuracion
@main.route('/config')
def config():
    return render_template('config.html')

# ruta de configuracion
@main.route('/usuario')
def usuario():
    usuarios = Usuarios.query.all()
    return render_template('usuario.html', usuarios=usuarios)
