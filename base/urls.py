from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
                       # ADVOCATES
    #     """ Function based view URL """
    path('', views.endpoints),
    path('advocates/', views.advocate_list, name='advocates'),
    # path('advocates/<str:username>/', views.advocate_detail),

    #    """ Class based view URL """
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('advocates/<str:username>/', views.AdvocateDetail.as_view()),

                        # COMPANIES
    #     """ Function based view URL """
    path('companies/', views.companies_list, name='companies'),
    

]