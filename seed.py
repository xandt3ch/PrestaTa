from app import create_app, db
from app.models import Usuarios, Clientes, Prestamos, Cuotas, Pagos
from datetime import date

app = create_app()

with app.app_context():

    # 🔹 Crear prestamistas
    usuarios = [
        Usuarios(apodo="acruz", 
                 nombre="Alexander Cruz", 
                 email="acruz@example.com",
                 cedula=12345678901,
                 password="password123", 
                 rol="prestamista",
                 creacion=date.today(),
                 estado=True),

        Usuarios(apodo="jcruz", 
                 nombre="Jairo Cruz", 
                 email="jcruz@example.com",
                 cedula=10987654321,
                 password="password456",
                 rol="colaborador",
                 creacion=date.today(),
                 estado=True),
       
    ]

    db.session.add_all(usuarios)
    db.session.commit()
"""
    # 🔹 Crear clientes
    clientes = [
        Clientes(nombre="Juan Perez", user_id=1),
        Clientes(nombre="Maria Lopez", user_id=2),
        Clientes(nombre="Carlos Diaz", user_id=3),
    ]

    db.session.add_all(clientes)
    db.session.commit()

    # 🔹 Crear préstamos
    prestamos = [
        Prestamos(cliente_id=1, prestamista_id=1, monto=10000, tasa_interes=5, fecha_inicio=date.today()),
        Prestamos(cliente_id=2, prestamista_id=1, monto=15000, tasa_interes=6, fecha_inicio=date.today()),
        Prestamos(cliente_id=3, prestamista_id=2, monto=20000, tasa_interes=7, fecha_inicio=date.today()),
    ]

    db.session.add_all(prestamos)
    db.session.commit()"""

print("✅ Datos insertados correctamente")