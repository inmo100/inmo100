from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('add/<id>', views.CreatePrototype.as_view(), name='add_prototype'),
    path('', views.PrototypesListView.as_view(), name='prototypes'),
    path('update/<id>', views.UpdatePrototype.as_view(), name='update_prototype'),
    path('fix/<id>', views.FixPrototype.as_view(), name='fix_prototype'),
]
