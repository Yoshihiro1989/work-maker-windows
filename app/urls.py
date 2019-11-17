from django.urls import path

form . import views

app_name - 'app'

urlpatterns = [
    path("", views.index, name="index"),
]
