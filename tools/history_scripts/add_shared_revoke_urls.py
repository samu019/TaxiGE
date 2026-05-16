from pathlib import Path

p = Path("dashboard/urls.py")
text = p.read_text(encoding="utf-8")

routes = [
    "    path('shared-access/invite/<int:invite_id>/deactivate/', views.deactivate_taxi_invite, name='deactivate_taxi_invite'),",
    "    path('shared-access/member/<int:member_id>/remove/', views.remove_company_member, name='remove_company_member'),",
]

for route in routes:
    if route not in text:
        text = text.replace("urlpatterns = [", "urlpatterns = [\n" + route, 1)

p.write_text(text, encoding="utf-8")
print("Rutas de desactivación añadidas")
