from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.index, name="dashboard"),
    path("charts/", views.charts, name="charts"),
    path("tables/", views.tables, name="tables"),
]