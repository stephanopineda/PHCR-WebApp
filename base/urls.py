from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('logout/', views.logout_client, name="logout"),
    path('login/', views.login_page, name="login"),
    path('register/', views.register_page, name="register"),

    path('staffdashboard/', views.staff_dashboard, name="staff_dashboard"),
    path('userdashboard/', views.user_dashboard, name="user_dashboard"),

    path('dashboard/', views.dashboard, name="dashboard"),
    path('unverifiedforms/', views.unverifiedforms, name="unverifiedforms"),
    path('viewrecords/', views.view_records, name="view_records"),
    path('manageusers/', views.manage_users, name="manage_users"),
    path('learnmore/', views.learn_more, name="learn_more"),
    path('datadashboard/', views.data_dashboard, name="data_dashboard"),
    
    path('patientprofile/', views.patient_profile, name="patient_profile"),
    path('patientrecord/', views.patient_record, name="patient_record"),

    path('choose_form/', views.choose_form_view, name='choose_form'),
    path('adultform/', views.adult_form, name="adult_form"),
    path('childform/', views.child_form, name="child_form"),
    path('pediatricform/', views.pediatric_form, name="pediatric_form"),

    path('viewform/<int:form_id>/', views.patient_view_form, name='patient_view_form'),
    path('updateform/<int:form_id>/', views.patient_update_form, name='patient_update_form'),
    path('deleteform/<int:form_id>/', views.patient_delete_form, name='patient_delete_form'),
    path('generate_pdf/<int:form_id>/', views.generate_pdf, name='generate_pdf'),

    path('staffviewform/<int:form_id>/', views.staff_view_form, name='staff_view_form'),
    path('staffupdateform/<int:form_id>/', views.staff_update_form, name='staff_update_form'),
    path('staffdeleteform/<int:form_id>/', views.staff_delete_form, name='staff_delete_form'),
    path('staffacceptform/<int:form_id>/', views.staff_accept_form, name='staff_accept_form'),
    path('staffviewprofile/<int:user_id>/', views.staff_view_profile, name='staff_view_profile'),
    path('staffsuspendprofile/<int:user_id>/', views.staff_suspend_user, name='staff_suspend_user'),
    path('staffgenerate_pdf/<int:form_id>/', views.staff_generate_pdf, name='staff_generate_pdf'),
]
