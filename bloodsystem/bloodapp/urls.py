from django.urls import path
from . import views 





urlpatterns=[
    path('home',views.home),
    path('admin_login',views.admin_login),
    path('login',views.Login_User),
    path('signup',views.signup),
    path('user',views.user_page),
    path('reg',views.reg),
    path('profile/',views.profile),
    path('view_user',views.view_user),
    path('req_blood',views.request_blood),
    path('confirmation',views.confirmation),
    path('confirmation/<str:username>/<str:blood_group>/<int:quantity>/', views.confirmation),
    path('all_order',views.all_order),
    path("admin_home",views.admin_home),
    path('donate_blood', views.donate_blood),
    path('donation_confirmation', views.donation_confirmation),
    path('donator_blood',views.donator_blood),
    
]

    
    

