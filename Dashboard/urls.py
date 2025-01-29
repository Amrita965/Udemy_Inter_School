from django.urls import path
from .views import dashboard_view, DashboardView

urlpatterns = [
    path("dashboard/", DashboardView.as_view(), name="dashboard")
]
