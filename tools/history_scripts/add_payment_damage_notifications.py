from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

old1 = """            payment.save()

            messages.success(request, 'Pago registrado correctamente.')"""

new1 = """            payment.save()

            if payment.debt_amount > 0:
                create_notification(
                    payment.company.owner,
                    'Deuda pendiente registrada',
                    f'El conductor {payment.driver} tiene una deuda pendiente de {payment.debt_amount} XAF.',
                    'warning',
                    '/panel/payments/'
                )

            messages.success(request, 'Pago registrado correctamente.')"""

old2 = """            payment.save()

            messages.success(request, 'Pago actualizado correctamente.')"""

new2 = """            payment.save()

            if payment.debt_amount > 0:
                create_notification(
                    payment.company.owner,
                    'Pago actualizado con deuda',
                    f'El pago de {payment.driver} mantiene una deuda de {payment.debt_amount} XAF.',
                    'warning',
                    '/panel/payments/'
                )

            messages.success(request, 'Pago actualizado correctamente.')"""

old3 = """            damage.save()

            messages.success(request, 'Daño registrado correctamente.')"""

new3 = """            damage.save()

            create_notification(
                damage.company.owner,
                'Nuevo daño registrado',
                f'Se registró un daño en {damage.vehicle}: {damage.title}. Costo estimado: {damage.estimated_cost} XAF.',
                'danger' if damage.status == 'pending' else 'warning',
                '/panel/damages/'
            )

            messages.success(request, 'Daño registrado correctamente.')"""

old4 = """            damage.save()

            messages.success(request, 'Daño actualizado correctamente.')"""

new4 = """            damage.save()

            if damage.status in ['pending', 'in_repair']:
                create_notification(
                    damage.company.owner,
                    'Daño pendiente actualizado',
                    f'El daño "{damage.title}" sigue pendiente o en reparación. Costo estimado: {damage.estimated_cost} XAF.',
                    'warning',
                    '/panel/damages/'
                )

            messages.success(request, 'Daño actualizado correctamente.')"""

for old, new in [(old1, new1), (old2, new2), (old3, new3), (old4, new4)]:
    text = text.replace(old, new)

p.write_text(text, encoding="utf-8")
print("Notificaciones automáticas de pagos y daños añadidas")
