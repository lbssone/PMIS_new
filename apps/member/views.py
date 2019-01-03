import json
from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, View
from django.db.models import Count, Q
from datetime import datetime, timedelta

from mysite.views import ListView
from .models import Member, Transaction, Transaction_product
from apps.inventory.models import Product

# Create your views here.
class MemberList(View):
    # model = Member
    # template_name = 'modules/member/member.html'
    # context_object_name = 'member_list'
    # base_url = 'member:list'

    # def get(self, request):
    #     dataset = Member.objects \
    #         .values('dwelling') \
    #         .annotate(north_count=Count('dwelling', filter=Q(dwelling="N")),
    #                 central_count=Count('dwelling', filter=Q(dwelling="M")),
    #                 south_count=Count('dwelling', filter=Q(dwelling="S"))) \
    #         .order_by('dwelling')

    #     categories = list()
    #     north_data = list()
    #     central_data = list()
    #     south_data = list()

    #     for entry in dataset:
    #         categories.append(entry['dwelling'])
    #         north_data.append(entry['north_count'])
    #         central_data.append(entry['central_count'])
    #         south_data.append(entry['south_count'])

    #     north = {
    #         'name': '北部',
    #         'data': north_data,
    #         'color': 'green',
    #     }

    #     central = {
    #         'name': '中部',
    #         'data': central_data,
    #         'color': 'red',
    #     }

    #     south = {
    #         'name': '南部',
    #         'data': south_data,
    #         'color': 'blue',
    #     }

    #     chart = {
    #         'chart': {'type': 'column'},
    #         'title': {'text': '會員居住地分布'},
    #         'xAxis': {'categories': categories},
    #         'series': [north, central, south],
    #         'plotOptions': {
	# 		    'series': {
    #     	        'grouping': False,
	# 		    }
	# 	    }
    #     }


    #     dump = json.dumps(chart)

    #     return render(request, 'modules/member/member.html', {'chart': dump})

    # def get(self, request):
    #     dataset = Transaction_product.objects \
    #     .values('product') \
    #     .annotate(uv_s=Count('product', filter=Q(product__u_feature='抗UV', product__u_type='直傘')), 
    #     uv_auto=Count('product', filter=Q(product__u_feature='抗UV', product__u_type='手開摺傘')))

    #     categories = list()
    #     straight = list()
    #     auto = list()
        
    #     for entry in dataset:
    #         categories.append(entry['product'])
    #         straight.append(entry['uv_s'])
    #         auto.append(entry['uv_auto'])

    #     s = {
    #         'name': '抗UV直傘',
    #         'data': straight,
    #         'color': 'green',
    #     }

    #     au = {
    #         'name': '抗UV手開摺傘',
    #         'data': auto,
    #         'color': 'red',
    #     }


    #     chart = {
    #         'chart': {'type': 'column'},
    #         'title': {'text': '傘'},
    #         'xAxis': {'categories': categories},
    #         'series': [s, au],
    #         'plotOptions': {
	# 		    'series': {
    #     	        'grouping': False,
	# 		    }
	# 	    }
    #     }


    #     dump = json.dumps(chart)

    #     return render(request, 'modules/member/member.html', {'chart': dump})

    def get(self, request):
        return render(request, 'modules/member/member.html')

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