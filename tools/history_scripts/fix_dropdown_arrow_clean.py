from pathlib import Path
import re

p = Path("templates/dashboard/panel_home.html")
text = p.read_text(encoding="utf-8-sig").replace("\ufeff", "")

old = r'''
.premium-section summary::after {
    content: "⌄";
    width: 34px;
    height: 34px;
    border-radius: 999px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: var(--surface-soft, rgba(255,255,255,.08));
    color: var(--text-primary, #f8fafc);
    font-size: 24px;
    transition: .2s ease;
}

.premium-section[open] summary::after {
    transform: rotate(180deg);
}
'''

new = r'''
.premium-section summary::after {
    content: "›";
    display: inline-flex;
    align-items: center;
    justify-content: center;
    margin-left: 12px;
    color: #f59e0b;
    font-size: 30px;
    font-weight: 1000;
    line-height: 1;
    transform: rotate(90deg);
    transition: transform .22s ease, color .22s ease;
}

.premium-section[open] summary::after {
    transform: rotate(-90deg);
    color: #facc15;
}
'''

text = text.replace(old, new)

p.write_text(text, encoding="utf-8")
print("OK: desplegable profesional aplicado")
