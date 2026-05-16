from pathlib import Path

items = [
    ("templates/dashboard/panel_vehicles.html", "vehicles"),
    ("templates/dashboard/panel_drivers.html", "drivers"),
    ("templates/dashboard/panel_payments.html", "payments"),
    ("templates/dashboard/panel_damages.html", "damages"),
]

for file_path, var in items:
    p = Path(file_path)
    text = p.read_text(encoding="utf-8")

    pagination = f"""
<div style="display:flex; gap:10px; justify-content:center; align-items:center; flex-wrap:wrap; margin-top:22px;">
    {{% if {var}.has_previous %}}
        <a href="?page={{{{ {var}.previous_page_number }}}}" style="padding:8px 12px; border-radius:12px; background:rgba(255,255,255,.08); color:inherit; text-decoration:none;">Anterior</a>
    {{% endif %}}

    {{% if {var}.paginator.num_pages > 1 %}}
        <span style="opacity:.8;">Página {{{{ {var}.number }}}} de {{{{ {var}.paginator.num_pages }}}}</span>
    {{% endif %}}

    {{% if {var}.has_next %}}
        <a href="?page={{{{ {var}.next_page_number }}}}" style="padding:8px 12px; border-radius:12px; background:rgba(255,255,255,.08); color:inherit; text-decoration:none;">Siguiente</a>
    {{% endif %}}
</div>
"""

    if f"{var}.paginator.num_pages" not in text:
        text = text.replace("{% endblock %}", pagination + "\n{% endblock %}")

    p.write_text(text, encoding="utf-8")

print("Controles de paginación añadidos a plantillas")
