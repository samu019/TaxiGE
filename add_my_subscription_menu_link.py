from pathlib import Path

p = Path("templates/dashboard/panel_base.html")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

link = '''
<a href="/panel/subscription/" class="sidebar-link">
    <span>Mi suscripción</span>
</a>
'''

if "/panel/subscription/" not in text:
    marker = '<a href="/panel/notifications/"'
    pos = text.find(marker)

    if pos != -1:
        text = text[:pos] + link + "\n" + text[pos:]
    else:
        text = text.replace("</nav>", link + "\n</nav>", 1)

p.write_text(text, encoding="utf-8")
print("Enlace Mi suscripción agregado al menú.")
