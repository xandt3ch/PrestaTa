from flask import  Blueprint, render_template, url_for


main = Blueprint('main',__name__)
auth = Blueprint('auth',__name__)

#ruta de inicio
@main.route('/')
def dashboard():
    return render_template('index.html')

# ruta de prestamo
@main.route('/prestamo')
def prestamo():
    return render_template('prestamo.html')

# ruta plus
@main.route('/plus')
def plus():
    return render_template('plus.html')

#ruta cliente
@main.route('/cliente')
def cliente():
    return render_template('cliente.html')

# ruta de pago
@main.route('/pago')
def pago():
    return render_template('pago.html')

# ruta de configuracion
@main.route('/config')
def config():
    return render_template('config.html')

