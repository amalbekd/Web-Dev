from django.http.response import JsonResponse
from .models import * 

def companylist(request):
    company = Company.objects.all()
    # company_json = [c.to_json() for c in company]

    company_json = []
    for i in company:
        company_json.append(i.to_json())


    return JsonResponse(company_json, safe=False)

def company(request, id):
    try:
        c = Company.objects.get(id=id)
    except Company.DoesNotExist as error:
        return JsonResponse({'massege: {error}'})
    return JsonResponse(c.to_json())

def vacancylist(request):
    vacancies = Vacancy.objects.all()
    vacancy_json = [v.to_json() for v in vacancies]
    return JsonResponse(vacancy_json, safe=False)

def vacancy(request, id):
    try:
        v = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist as error:
        return JsonResponse({'massage: {error}'})
    return JsonResponse(v.to_json())

def company_vacancy(request, id):
    try:
        c = Company.objects.all().get(id=id)
        vacancy = Vacancy.objects.filter(company = c)
        vacancy_json = [v.to_json() for v in vacancy]
    except Company.DoesNotExist as error:
        return JsonResponse({'massege: {error}'})
    return JsonResponse(vacancy_json, safe=False)

def top10_vacancies(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10]
    vacancy_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancy_json, safe=False)