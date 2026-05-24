from flask import  Blueprint, render_template, url_for, redirect, request, flash, session
from flask_login import login_required, LoginManager, user_loader, current_user
from app.models import Usuarios, Clientes, Prestamos, Cuotas, Pagos


main = Blueprint('main',__name__)
auth = Blueprint('auth',__name__)

@login_manager.user_loader
def load_user(user_id):
    return Usuarios.query.get(usuarios.id)

@auth.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        apodo = request.form.get('username')
        password = request.form.get('password')

        usuario = Usuarios.query.filter_by(apodo=apodo).first()

        if usuario and usuario.password == password:
            return redirect(url_for('main.dashboard'))
        else:
            flash('Credenciales inválidas. Por favor, inténtalo de nuevo.')

    return render_template('login.html')

#ruta de inicio
@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('index.html')

# ruta de prestamo
@main.route('/prestamo')
@login_required
def prestamo():
    prestamos = Prestamos.query.all()
    clientes = Clientes.query.where(Clientes.id == Prestamos.cliente_id).all()
    return render_template('prestamo.html', prestamos=prestamos, clientes=clientes)

# ruta plus
@main.route('/plus')
@login_required
def plus():
    return render_template('plus.html')

#ruta cliente
@main.route('/cliente')
@login_required
def cliente():
    clientes = Clientes.query.all()
    return render_template('cliente.html', clientes=clientes)

# ruta de pago
@main.route('/pago')
@login_required
def pago():
    pagos = Pagos.query.all()
    return render_template('pago.html', pagos=pagos)        
    return render_template('pago.html')

# ruta de configuracion
@main.route('/config')
@login_required
def config():
    return render_template('config.html', title='Configuración')

# ruta de configuracion
@main.route('/usuario')
@login_required
def usuario():
    usuarios = Usuarios.query.all()
    return render_template('usuario.html', usuarios=usuarios)
