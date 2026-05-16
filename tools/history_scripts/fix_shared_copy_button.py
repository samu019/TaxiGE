from pathlib import Path

p = Path("templates/dashboard/shared_access.html")
text = p.read_text(encoding="utf-8")

old = '''<input style="width:100%;" readonly value="{{ request.scheme }}://{{ request.get_host }}/invite/{{ invite.token }}/">'''

new = '''<div style="display:flex; gap:8px;">
                            <input id="invite-{{ invite.id }}" style="width:100%;" readonly value="{{ request.scheme }}://{{ request.get_host }}/invite/{{ invite.token }}/">
                            <button type="button" onclick="copiarInvitacion('invite-{{ invite.id }}')">Copiar</button>
                        </div>'''

text = text.replace(old, new)

script = '''
<script>
function copiarInvitacion(inputId) {
    const input = document.getElementById(inputId);
    input.select();
    input.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(input.value);
    alert("Enlace copiado correctamente");
}
</script>
'''

if "function copiarInvitacion" not in text:
    text = text.replace("{% endblock %}", script + "\n{% endblock %}")

p.write_text(text, encoding="utf-8")
print("Botón copiar añadido")
