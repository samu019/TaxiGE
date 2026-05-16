from pathlib import Path

p = Path("config/urls.py")
text = p.read_text(encoding="utf-8")

if "from dashboard import views as dashboard_views" not in text:
    text = text.replace(
        "from django.urls import path, include",
        "from django.urls import path, include\nfrom dashboard import views as dashboard_views"
    )

if "invite/<str:token>/" not in text:
    text = text.replace(
        "urlpatterns = [",
        "urlpatterns = [\n    path('invite/<str:token>/', dashboard_views.accept_taxi_invite, name='accept_taxi_invite'),"
    )

p.write_text(text, encoding="utf-8")
print("Ruta /invite/<token>/ añadida")
