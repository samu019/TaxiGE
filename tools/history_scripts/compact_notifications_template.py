from pathlib import Path

p = Path("templates/dashboard/notifications.html")
text = p.read_text(encoding="utf-8")

text = text.replace("padding: 18px;", "padding: 12px;")
text = text.replace("margin-bottom: 14px;", "margin-bottom: 8px;")
text = text.replace("border-radius: 18px;", "border-radius: 14px;")
text = text.replace("font-size: 17px;", "font-size: 15px;")
text = text.replace("margin: 10px 0;", "margin: 6px 0;")
text = text.replace("margin-top: 12px;", "margin-top: 8px;")
text = text.replace("padding: 9px 13px;", "padding: 6px 10px;")
text = text.replace("padding: 24px;", "padding: 16px;")
text = text.replace("font-size: 28px;", "font-size: 24px;")
text = text.replace("padding:20px;", "padding:14px;")

text = text.replace(
    '<p class="notification-message">{{ n.message }}</p>',
    '<p class="notification-message">{{ n.message|truncatechars:95 }}</p>'
)

p.write_text(text, encoding="utf-8")
print("Plantilla de notificaciones compactada")
