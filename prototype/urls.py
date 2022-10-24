from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.CreatePrototype.as_view(),name='add_prototype'),
    path('prototipos/', views.PrototypeView.as_view(), name='prototypes'),
]
