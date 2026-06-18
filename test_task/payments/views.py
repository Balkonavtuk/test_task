from django.shortcuts import render
from django.http import JsonResponse
from .models import Payment


def index(request):
    return render(request, 'payments/index.html')


def chart_data(request):
    # Данные для линейного графика: список (дата, сумма), сортировка по дате
    payments = Payment.objects.select_related('payer').order_by('pay_date')
    line_data = [
        {
            'date': p.pay_date.isoformat(),
            'amount': float(p.amount),
            'payer': str(p.payer)
        }
        for p in payments
    ]
    # Данные для гистограммы: все платежи с именем плательщика
    bar_data = [
        {
            'label': str(p.payer),  # ФИО
            'amount': float(p.amount),
            'date': p.pay_date.isoformat()
        }
        for p in payments
    ]
    return JsonResponse({
        'line': line_data,
        'bar': bar_data
    })


from django.shortcuts import render

# Create your views here.
