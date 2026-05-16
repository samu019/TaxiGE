from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

old1 = """            payment.save()
            return redirect('/panel/payments/')"""

new1 = """            payment.save()

            if payment.debt_amount > 0:
                create_notification(
                    payment.company.owner,
                    'Deuda pendiente registrada',
                    f'El conductor {payment.driver} tiene una deuda pendiente de {payment.debt_amount} XAF.',
                    'warning',
                    '/panel/payments/'
                )

            return redirect('/panel/payments/')"""

old2 = """            damage.save()
            return redirect('/panel/damages/')"""

new2 = """            damage.save()

            create_notification(
                damage.company.owner,
                'Nuevo daño registrado',
                f'Se registró un daño en {damage.vehicle}: {damage.title}. Costo estimado: {damage.estimated_cost} XAF.',
                'danger' if damage.status == 'pending' else 'warning',
                '/panel/damages/'
            )

            return redirect('/panel/damages/')"""

# Reemplaza en create y edit si existen ambos patrones
text = text.replace(old1, new1)
text = text.replace(old2, new2)

p.write_text(text, encoding="utf-8")
print("Notificaciones exactas para pagos y daños aplicadas")
