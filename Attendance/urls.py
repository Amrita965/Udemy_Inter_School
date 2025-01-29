from django.urls import path
from .views import mark_attendance

urlpatterns = [
    path("attendance/", mark_attendance, name="mark_attendance"),
    # path('attendance_view/', attendance_view, name='attendance_view'),
]

