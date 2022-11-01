from django.urls import path
from . import views

urlpatterns = [
                       # ADVOCATES
    #     """ Class based view URL"""
    path('', views.endpoints),
    path('advocates/', views.advocate_list, name='advocates'),
    # path('advocates/<str:username>/', views.advocate_detail),

    #    """ Class based view URL"""
    path('advocates/<str:username>/', views.AdvocateDetail.as_view()),

                        # COMPANIES
    path('companies/', views.companies_list, name='companies'),
    

]