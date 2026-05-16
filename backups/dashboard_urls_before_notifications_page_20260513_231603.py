from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('shared-access/member/<int:member_id>/remove/', views.remove_company_member, name='remove_company_member'),
    path('shared-access/invite/<int:invite_id>/deactivate/', views.deactivate_taxi_invite, name='deactivate_taxi_invite'),
    path('shared-access/', views.panel_shared_access, name='panel_shared_access'),
    path('export/excel/', views.dashboard_export_excel, name='dashboard_export_excel'),
    path('export/pdf/', views.dashboard_export_pdf, name='dashboard_export_pdf'),
    path('', views.panel_home, name='panel_home'),

    path('vehicles/', views.panel_vehicles, name='panel_vehicles'),
    path('vehicles/create/', views.panel_vehicle_create, name='panel_vehicle_create'),
    path('vehicles/<int:vehicle_id>/edit/', views.panel_vehicle_edit, name='panel_vehicle_edit'),
    path('vehicles/<int:vehicle_id>/delete/', views.panel_vehicle_delete, name='panel_vehicle_delete'),

    path('drivers/', views.panel_drivers, name='panel_drivers'),
    path('drivers/create/', views.panel_driver_create, name='panel_driver_create'),
    path('drivers/<int:driver_id>/edit/', views.panel_driver_edit, name='panel_driver_edit'),
    path('drivers/<int:driver_id>/delete/', views.panel_driver_delete, name='panel_driver_delete'),

    path('payments/', views.panel_payments, name='panel_payments'),
    path('payments/create/', views.panel_payment_create, name='panel_payment_create'),
    path('payments/<int:payment_id>/edit/', views.panel_payment_edit, name='panel_payment_edit'),
    path('payments/<int:payment_id>/delete/', views.panel_payment_delete, name='panel_payment_delete'),

    path('damages/', views.panel_damages, name='panel_damages'),
    path('damages/create/', views.panel_damage_create, name='panel_damage_create'),
    path('damages/<int:damage_id>/edit/', views.panel_damage_edit, name='panel_damage_edit'),
    path('damages/<int:damage_id>/delete/', views.panel_damage_delete, name='panel_damage_delete'),

    path('api/summary/', views.api_panel_summary, name='api_panel_summary'),
    path('api/vehicles/', views.api_panel_vehicles, name='api_panel_vehicles'),
    path('api/drivers/', views.api_panel_drivers, name='api_panel_drivers'),
    path('api/payments/', views.api_panel_payments, name='api_panel_payments'),
    path('api/damages/', views.api_panel_damages, name='api_panel_damages'),

    path('reports/vehicles.csv', views.export_vehicles_csv, name='export_vehicles_csv'),
    path('reports/drivers.csv', views.export_drivers_csv, name='export_drivers_csv'),
    path('reports/payments.csv', views.export_payments_csv, name='export_payments_csv'),
    path('reports/damages.csv', views.export_damages_csv, name='export_damages_csv'),

    path('reports/vehicles.pdf', views.export_vehicles_pdf, name='export_vehicles_pdf'),
    path('reports/drivers.pdf', views.export_drivers_pdf, name='export_drivers_pdf'),
    path('reports/payments.pdf', views.export_payments_pdf, name='export_payments_pdf'),
    path('reports/damages.pdf', views.export_damages_pdf, name='export_damages_pdf'),
]
