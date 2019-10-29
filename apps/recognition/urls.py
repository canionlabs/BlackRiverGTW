from django.urls import path
from .views import RecFacesView


app_name = "recognition"

urlpatterns = [
    path("faces/", RecFacesView.as_view(), name="faces")
]
