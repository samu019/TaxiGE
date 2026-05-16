from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

old = """    if not user_has_any_export_permission(request.user):
        messages.error(request, 'No tienes permiso para exportar reportes.')
        return redirect('/panel/')"""

new = """    if not user_has_any_export_permission(request.user):
        audit_event(
            request,
            AuditLog.ACTION_VIEW,
            'dashboard',
            'Export',
            None,
            'Exportación bloqueada',
            'Intento de exportación sin permiso'
        )
        messages.error(request, 'No tienes permiso para exportar reportes.')
        return redirect('/panel/')"""

text = text.replace(old, new)

p.write_text(text, encoding="utf-8")
print("Auditoría de exportaciones bloqueadas aplicada")
