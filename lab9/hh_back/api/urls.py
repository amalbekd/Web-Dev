from django.urls import path
from .views import *

urlpatterns = [
    path('companies/', companylist),
    path('companies/<int:id>/', company),
    path('companies/<int:id>/vacancies/', company_vacancy),
    path('vacancies/', vacancylist),
    path('vacancies/<int:id>/', vacancy),
    path('vacancies/top_ten/', top10_vacancies),
]