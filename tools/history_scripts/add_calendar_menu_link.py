from pathlib import Path

p = Path("templates/dashboard/panel_base.html")
text = p.read_text(encoding="utf-8")

menu_item = '''
                <a href="/panel/calendar/" class="nav-link">
                    <span>Calendario</span>
                </a>
'''

if '/panel/calendar/' not in text:
    if '/panel/notifications/' in text:
        pos = text.find('/panel/notifications/')
        end = text.find('</a>', pos)
        if end != -1:
            end += 4
            text = text[:end] + '\n' + menu_item + text[end:]
    else:
        text = text.replace('</nav>', menu_item + '\n</nav>', 1)

p.write_text(text, encoding="utf-8")
print("Botón Calendario añadido al menú")
