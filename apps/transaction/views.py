import json
from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, View

from datetime import datetime, timedelta

from mysite.views import ListView
from .models import Transaction, Transaction_product
from apps.inventory.models import Product

# Create your views here.
class TransactionSeason(View):
    def get(self, request):
        return render(request, 'modules/transaction/transaction_season.html')

class TransactionChart(View):
    def get(self, request):
        return render(request, 'modules/transaction/transaction_chart.html')

    def post(self, request):
        year = int(self.request.POST.get('year'))
        month = int(self.request.POST.get('month'))
        uv_s_sold = 0
        uv_auto_sold = 0
        uv_manual_sold = 0
        for trans_data in Transaction_product.objects.all():
            date_year = datetime.strptime(str(trans_data.transaction.date), "%Y-%m-%d").year
            date_month = datetime.strptime(str(trans_data.transaction.date), "%Y-%m-%d").month
            if date_year == year and date_month == month:
                if trans_data.product.name == "抗UV直傘":
                    uv_s_sold += trans_data.quantity
                elif trans_data.product.name == "抗UV自動摺傘":
                    uv_auto_sold += trans_data.quantity
                elif trans_data.product.name == "抗UV手開摺傘":
                    uv_manual_sold += trans_data.quantity

        # uv_s = {'name': '抗UV直傘', 'data': [uv_s_sold, 1], 'color': 'green',}
        # uv_au = {'name': '抗UV自動摺傘', 'data': [uv_auto_sold, 2], 'color': 'red',}

        chart = {
            'chart': {'type': 'column'},
            'title': {
                'text': str(year) + '年 ' + str(month) + '月雨傘銷售分布',
                'style': {
                    'fontFamily': 'Microsoft JhengHei'
                }
            },
            'xAxis': {'categories': ['抗UV直傘', '抗UV自動摺傘', '抗UV手開摺傘']},
            # 'series': [uv_s, uv_au],
            'series': [{ 
                'name': '銷售量',
                'data': [
                    {'y': uv_s_sold, 'color': 'red'},
                    {'y': uv_auto_sold, 'color': 'blue'},
                    {'y': uv_manual_sold, 'color': 'green'}
                ]
            }],
            'plotOptions': {
                'series': {
                    # 'grouping': False,
                }
            }
        }

        dump = json.dumps(chart)

        return render(request, 'modules/member/member.html', {'chart': dump})
    

    # def get(self, request):
    #         dataset = Transaction_product.objects \
    #         .values('product') \
    #         .annotate(uv_s=Count('product', filter=Q(product__u_feature='抗UV', product__u_type='直傘')), 
    #         uv_auto=Count('product', filter=Q(product__u_feature='抗UV', product__u_type='手開摺傘')))

    #         categories = list()
    #         straight = list()
    #         auto = list()
            
    #         for entry in dataset:
    #             categories.append(entry['product'])
    #             straight.append(entry['uv_s'])
    #             auto.append(entry['uv_auto'])

    #         s = {
    #             'name': '抗UV直傘',
    #             'data': straight,
    #             'color': 'green',
    #         }

    #         au = {
    #             'name': '抗UV手開摺傘',
    #             'data': auto,
    #             'color': 'red',
    #         }


    #         chart = {
    #             'chart': {'type': 'column'},
    #             'title': {'text': '傘'},
    #             'xAxis': {'categories': categories},
    #             'series': [s, au],
    #             'plotOptions': {
    #                 'series': {
    #                     'grouping': False,
    #                 }
    #             }
    #         }


    #         dump = json.dumps(chart)

    #         return render(request, 'modules/member/member.html', {'chart': dump})
