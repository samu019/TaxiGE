from pathlib import Path

p = Path("templates/dashboard/panel_base.html")
text = p.read_text(encoding="utf-8")

menu_item = '''
                <a href="/panel/shared-access/" class="nav-link">
                    <span>Acceso compartido</span>
                </a>
'''

# Intentar insertarlo después del enlace de Daños
if '/panel/shared-access/' not in text:
    if 'href="/panel/damages/"' in text:
        pos = text.find('href="/panel/damages/"')
        end = text.find('</a>', pos)
        if end != -1:
            end += 4
            text = text[:end] + '\n' + menu_item + text[end:]
    else:
        # Si no encuentra el enlace de daños, insertarlo antes de cerrar la navegación
        text = text.replace('</nav>', menu_item + '\n</nav>', 1)

p.write_text(text, encoding="utf-8")
print("Enlace de Acceso compartido añadido al menú")
