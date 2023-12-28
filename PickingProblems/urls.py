"""PickingProblems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from ppLRPDN import views

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('menu/',views.menu_view,name='menu'),
    path('pick_menu/',views.pick_menu,name='pick_menu'),
    path('new_pp/', views.npp_view, name='npp'),
    path('admin/', admin.site.urls),
    path('success/<str:reference_number>/', views.success_view, name='success'),
    path('fetch_data/', views.fetch_data, name='fetch_data'),
    path('fpp/', views.fpp, name='fpp'),
    path('edit_fpp/<str:reference_number>/', views.edit_fpp, name='edit_fpp'),
    path('final_fpp/<str:reference_number>/', views.final_fpp, name='final_fpp'),
    path('fpp_fetch_data/', views.fpp_fetch_data, name='fpp_fetch_data'),
    path('fpp_success_page/', views.fpp_success_page, name='fpp_success_page'),
    path('epp_success_page/', views.epp_success_page, name='epp_success_page'),
    path('pp_reports_menu/', views.pp_reports_menu, name='pp_reports_menu'),
    path('mpr_menu/', views.mpr_menu, name='mpr_menu'),
    path('ppdept_menu/', views.ppdept_menu, name='ppdept_menu'),
    path('wtr_menu/', views.wtr_menu, name='wtr_menu'),
    path('eliminate_pp/', views.eliminate_pp, name='eliminate_pp'),
    path('elim_pp/<str:reference_number>/', views.elim_pp, name='elim_pp'),
    path('forbidden/', views.forbidden, name='forbidden'),
    path('super_menu/', views.super_menu, name='super_menu'),
    path('ticket_menu/', views.ticket_menu, name='ticket_menu'),
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    path('ticket_success/<int:ticket_number>/', views.ticket_success, name='ticket_success'),
    path('ticket_list', views.ticket_list, name='ticket_list'),
    path('edit_ticket/<int:ticket_number>/', views.edit_ticket, name='edit_ticket'),
    path('edit_ticket_success/<int:ticket_number>/', views.edit_ticket_success, name='edit_ticket_success'),
    path('ticket_report/', views.ticket_report, name='ticket_report'),
    path('elim_ticket_list/', views.elim_ticket_list, name='elim_ticket_list'),
    path('elim_ticket/<int:ticket_number>/', views.elim_ticket, name='elim_ticket'),
    path('rng_locations_menu/', views.rng_locations_menu, name='rng_locations_menu'),
    path('fer_menu/', views.fer_menu, name='fer_menu'),
    path('print_pp/', views.print_pp, name='print_pp'),
    path('pdf/<str:reference_number>/', views.create_filled_pdf, name='pdf'),
]


