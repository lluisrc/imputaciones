from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registros/', views.RegistroListView.as_view(), name='registros'),
    path('create/', views.RegistroCreate.as_view(), name='registro-create'),
    re_path(r'^update/(?P<pk>\d+)$', views.RegistroUpdateView.as_view(), name='registro-update'),
    re_path(r'^registro/(?P<pk>\d+)$', views.RegistroDetailView.as_view(), name='registro-detail'),
]
