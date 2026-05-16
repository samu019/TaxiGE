from pathlib import Path
import re

p = Path("templates/dashboard/panel_home.html")
text = p.read_text(encoding="utf-8")

text = re.sub(
    r'<style>\s*\.charts-grid.*?</style>',
    '',
    text,
    flags=re.DOTALL
)

p.write_text(text, encoding="utf-8")
print("OK: panel_home limpio, CSS de gráficos controlado desde panel_base")
