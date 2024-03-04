from django.shortcuts import render
from aggregate.models import Transaction
from django.db.models import Sum, Count, Avg, Max, Min
from django.http import HttpResponse

def total_transaction_amount(request):
    # total_amount = Transaction.objects.aggregate(total_amount=Sum('amount'))
    # maximum_amount = Transaction.objects.aggregate(maximum_amount=Max('amount'))
    # minimum_amount = Transaction.objects.aggregate(minimum_amount=Min('amount'))
    # average_amount = Transaction.objects.aggregate(average_amount=Avg('amount'))
    total_posts = Transaction.objects.aggregate(total_posts=Count('posts'))
    context = {
        # 'total_amount': total_amount,
        'total_posts': total_posts,
        # 'maximum_amount': maximum_amount,
        # 'minimum_amount': minimum_amount,
        # 'average_amount': average_amount,
    }
    return render(request, 'total_amount.html', context)

