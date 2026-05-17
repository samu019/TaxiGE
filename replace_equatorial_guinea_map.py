from pathlib import Path
p = Path("templates/accounts/request_admin.html")
text = p.read_text(encoding="utf-8", errors="replace")

start = text.find('<div class="map-box">')
end = text.find('</div>', text.find('class="map-caption"'))
end = text.find('</div>', end)  # cierre de map-box

new_block = '''
<div class="map-box">
    <div style="display:flex; flex-direction:column; align-items:center; gap:18px;">
        <div style="
            font-size: 7rem;
            line-height: 1;
            filter: drop-shadow(0 18px 35px rgba(37,99,235,.35));
        ">🗺️</div>

        <div style="
            font-size: 1.4rem;
            font-weight: 900;
            color: #f8fafc;
            letter-spacing: -0.02em;
        ">
            Guinea Ecuatorial
        </div>

        <div class="map-caption">
            Cobertura operativa en Malabo, Bata y futuras ciudades del país.
        </div>
    </div>
</div>
'''

text = text[:start] + new_block + text[end+6:]
p.write_text(text, encoding="utf-8")
print("Mapa reemplazado por una representación real y profesional.")
