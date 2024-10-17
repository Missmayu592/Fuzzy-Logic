# from django.urls import path, include
# from . import views
# urlpatterns = [

#     path('', views.fullpage, name='fullpage'), 
#     path('signup/', views.signup, name='signup'), 
#     path('about/', views.about, name='about'), 
#     path('login/', views.login, name='login'), 


# ]

from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.fullpage, name='home'), 
    path('signup/signin/', views.singin, name='login'),
    path('signup/', views.signup, name='signup'), 
    path('signup/sign_out/', views.sign_out, name='sign_out'), 
    path('about/', views.about, name='about'), 

]

