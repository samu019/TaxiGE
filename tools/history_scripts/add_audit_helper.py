from pathlib import Path

p = Path("dashboard/views.py")
text = p.read_text(encoding="utf-8")

if "from audits.models import AuditLog" not in text:
    text = "from audits.models import AuditLog\n" + text

helper = r'''

def get_client_ip(request):
    forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if forwarded_for:
        return forwarded_for.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR')


def audit_event(request, action, app_label, model_name, object_id=None, object_repr=None, description=None):
    try:
        AuditLog.objects.create(
            user=request.user if request.user.is_authenticated else None,
            action=action,
            app_label=app_label,
            model_name=model_name,
            object_id=str(object_id) if object_id is not None else None,
            object_repr=str(object_repr)[:255] if object_repr else None,
            description=description,
            ip_address=get_client_ip(request),
            user_agent=request.META.get('HTTP_USER_AGENT', ''),
        )
    except Exception:
        pass

'''

if "def audit_event(request, action," not in text:
    text = text.replace("def shared_permissions_for_role(role):", helper + "\ndef shared_permissions_for_role(role):", 1)

p.write_text(text, encoding="utf-8")
print("Helper de auditoría añadido")
