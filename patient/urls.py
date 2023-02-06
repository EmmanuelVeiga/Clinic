from django.contrib import admin
from django.urls import path

from . import views
from .views import render_pdf_view, PacienteListView, paciente_render_pdf_view


urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.paciente, name='paciente'),
    path('paciente/add/', views.paciente_add, name='paciente_add'),
    path('paciente/edit/<int:paciente_pk>', views.paciente_edit, name='paciente_edit'),
    path('paciente/delete/<int:paciente_pk>', views.paciente_delete, name='paciente_delete'),

    # path('', PacienteListView.as_view(), name='paciente-list-view'),
    path('test/', render_pdf_view, name='test-view'),
    path('paciente/pdf/<pk>', paciente_render_pdf_view, name='paciente_pdf_view'),

]
