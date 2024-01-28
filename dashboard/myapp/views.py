from django.shortcuts import render
from .models import DashboardData
import json
# Create your views here.
def index(request):
    country_count = DashboardData.objects.values('country').distinct().count()
    topics__count = DashboardData.objects.values('topic').distinct().count()
    region__count = DashboardData.objects.values('region').distinct().count()
    sector__count = DashboardData.objects.values('region').distinct().count()
    return render(request, 'dashboard/index.html', {'country_count': country_count,
                                                    'topics__count':topics__count,
                                                    'region_count':region__count,
                                                    'sector_count':sector__count})
    
def charts(request):
    data = DashboardData.objects.all()

    # Access model fields correctly
    sectors = [entry.sector for entry in data]
    intensities = [entry.intensity for entry in data]

    context = {
        'sectors': json.dumps(sectors),
        'intensities': json.dumps(intensities),
    }

    return render(request, 'dashboard/charts.html', context)

def tables(request):
    region_value = request.GET.get('region', None)
    endyear_value = request.GET.get('end_year', None)
    topics_value = request.GET.get('topic', None)
    sector_value = request.GET.get('sector', None)
    source_value = request.GET.get('source', None)

    data = DashboardData.objects.all()

    if region_value:
        data = data.filter(region=region_value)
    if endyear_value:
        data = data.filter(end_year=endyear_value)
    if topics_value:
        data = data.filter(topic=topics_value)
    if sector_value:
        data = data.filter(sector=sector_value)
    if source_value:
        data = data.filter(source=source_value)

    region_filter = DashboardData.objects.values('region').distinct()
    endyear_filter = DashboardData.objects.values('end_year').distinct()
    topics_filter = DashboardData.objects.values('topic').distinct()
    sector_filter = DashboardData.objects.values('sector').distinct()
    source_filter = DashboardData.objects.values('source').distinct()

    return render(request, 'dashboard/tables.html', {
        'data': data,
        'region_filter': region_filter,
        'endyear_filter': endyear_filter,
        'topics_filter': topics_filter,
        'sector_filter': sector_filter,
        'source_filter': source_filter
    })

