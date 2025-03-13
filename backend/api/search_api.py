from django.http import JsonResponse
from django.db.models import Q
from backend.core.models import Country

def country_search_api(request):
    query = request.GET.get('q', '').strip()
    results = []
    if query:
        countries = Country.objects.filter(
            Q(country_name__icontains=query) | Q(country_code__icontains=query)
        )[:10]
    else:
        countries = Country.objects.all()[:50]

    occurrence_map = {}

    for c in countries:
        key = (c.country_name, c.country_code)
        occurrence_map.setdefault(key, 0)
        if occurrence_map[key] < 1:
            results.append({
                "label": f"{c.country_name} ({c.country_code})",
                "value": c.country_name
            })
            occurrence_map[key] += 1
    return JsonResponse(results, safe=False)


def currency_search_api(request):
    query = request.GET.get('q', '').strip()
    results = []
    if query:
        currencies = Country.objects.filter(
            Q(currency_name__icontains=query) | Q(currency_code__icontains=query)
        )[:50]
    else:
        currencies = Country.objects.all()[:10]

    occurrence_map = {}

    for c in currencies:
        key = (c.currency_name, c.currency_code)
        occurrence_map.setdefault(key, 0)
        if occurrence_map[key] < 1:
            results.append({
                "label": f"{c.currency_name} ({c.currency_code})",
                "value": c.currency_code
            })
            occurrence_map[key] += 1

    return JsonResponse(results, safe=False)
