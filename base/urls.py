from django.urls import path
from . import views

urlpatterns = [
    #     """ Class based view URL"""
    path('', views.endpoints),
    path('advocates', views.advocate_list, name='advocates'),
    # path('advocates/<str:username>/', views.advocate_detail),

    #    """ Class based view URL"""
    path('advocates/<str:username>/', views.AdvocateDetail.as_view()),

]