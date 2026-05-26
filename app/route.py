from . import db
from flask import  Blueprint, render_template, url_for, redirect, request, flash
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
    clientes = Clientes.query.where(Clientes.id == Prestamos.cliente_id).all()
    return render_template('prestamo.html', prestamos=prestamos, clientes=clientes)

# ruta plus
@main.route('/plus')
def plus():
    return render_template('plus.html')

#ruta cliente
@main.route('/cliente', methods=['GET', 'POST'])
def cliente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cedula = int(request.form['cedula'])
        telefono = int(request.form['telefono'])
        direccion = request.form['direccion']

        nuevo_cliente = Clientes(id=None, nombre=nombre, cedula=cedula, telefono=telefono, direccion=direccion, creacion=None, user_id=1)
        db.session.add(nuevo_cliente)
        db.session.commit()

        flash('Cliente agregado exitosamente', 'success')
        return redirect(url_for('main.cliente'))
    
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
    return render_template('config.html', title='Configuración')

# ruta de configuracion
@main.route('/usuario')
def usuario():
    usuarios = Usuarios.query.all()
    return render_template('usuario.html', usuarios=usuarios)
