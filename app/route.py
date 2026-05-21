from flask import  Blueprint, render_template, url_for


main = Blueprint('main',__name__)
auth = Blueprint('auth',__name__)


@main.route('/')
def dashboard():
    return render_template('index.html')

@main.route('/prestamo')
def prestamo():
    return render_template('prestamo.html')

@main.route('/plus')
def plus():
    return render_template('plus.html')

@main.route('/cliente')
def cliente():
    return render_template('cliente.html')

@main.route('/pago')
def pago():
    return render_template('pago.html')


@main.route('/config')
def config():
    return render_template('config.html')


