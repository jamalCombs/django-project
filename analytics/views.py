from django.shortcuts import render

def analytic_view(request):
    return render(request, 'analytics/overview.html')