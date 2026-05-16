from pathlib import Path

p = Path("templates/dashboard/shared_access.html")
text = p.read_text(encoding="utf-8")

# Añadir columna Acciones a enlaces
text = text.replace(
    "<th>Enlace</th>",
    "<th>Enlace</th>\n                    <th>Acciones</th>"
)

text = text.replace(
    '''<td>
                        <div style="display:flex; gap:8px;">
                            <input id="invite-{{ invite.id }}" style="width:100%;" readonly value="{{ request.scheme }}://{{ request.get_host }}/invite/{{ invite.token }}/">
                            <button type="button" onclick="copiarInvitacion('invite-{{ invite.id }}')">Copiar</button>
                        </div>
                    </td>''',
    '''<td>
                        <div style="display:flex; gap:8px;">
                            <input id="invite-{{ invite.id }}" style="width:100%;" readonly value="{{ request.scheme }}://{{ request.get_host }}/invite/{{ invite.token }}/">
                            <button type="button" onclick="copiarInvitacion('invite-{{ invite.id }}')">Copiar</button>
                        </div>
                    </td>
                    <td>
                        {% if invite.is_active %}
                        <form method="post" action="/panel/shared-access/invite/{{ invite.id }}/deactivate/" onsubmit="return confirm('¿Desactivar esta invitación?');">
                            {% csrf_token %}
                            <button type="submit">Desactivar</button>
                        </form>
                        {% else %}
                            Cerrado
                        {% endif %}
                    </td>'''
)

text = text.replace(
    '<td colspan="5">Todavía no hay invitaciones.</td>',
    '<td colspan="6">Todavía no hay invitaciones.</td>'
)

# Añadir columna Acciones a socios
text = text.replace(
    "<th>Fecha</th>",
    "<th>Fecha</th>\n                    <th>Acciones</th>"
)

text = text.replace(
    '''<td>{{ member.created_at|date:"d/m/Y H:i" }}</td>
                </tr>''',
    '''<td>{{ member.created_at|date:"d/m/Y H:i" }}</td>
                    <td>
                        {% if member.is_active %}
                        <form method="post" action="/panel/shared-access/member/{{ member.id }}/remove/" onsubmit="return confirm('¿Quitar el acceso a este socio?');">
                            {% csrf_token %}
                            <button type="submit">Quitar acceso</button>
                        </form>
                        {% else %}
                            Sin acceso
                        {% endif %}
                    </td>
                </tr>'''
)

text = text.replace(
    '<td colspan="5">Todavía no hay socios vinculados.</td>',
    '<td colspan="6">Todavía no hay socios vinculados.</td>'
)

p.write_text(text, encoding="utf-8")
print("Plantilla actualizada con botones de control")
