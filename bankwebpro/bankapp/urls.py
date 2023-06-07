from django.urls import path
from bankapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('in/',views.log_in,name='in'),
    path('reg/', views.reg_ster, name='reg'),
    path('log_new/',views.lognew,name='log_new'),
    path('ek_m/', views.ekm, name='ek_m'),
    path('kozh_i/', views.kozhikode, name='kozh_i'),
    path('mala_p/', views.mala, name='mala_p'),
    path('waya/', views.waya, name='waya'),
    path('kannur/', views.kannur, name='kannur'),
    path('form_p/', views.formpage, name='form_p'),
    path('form2_p/',views.person_det,name='form2_p'),
    path('form_new/',views.formnew,name='form_new'),
    path('log_out/',views.log_out,name='log_out'),

]
