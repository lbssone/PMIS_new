import json
from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, View
from django.db.models import Count, Q

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

    def get(self, request):
        dataset = Transaction_product.objects \
        .values('product') \
        .annotate(uv_s=Count('product', filter=Q(product__u_feature='抗UV', product__u_type='直傘')), 
        uv_auto=Count('product', filter=Q(product__u_feature='抗UV', product__u_type='手開摺傘')))

        categories = list()
        straight = list()
        auto = list()
        
        for entry in dataset:
            categories.append(entry['product'])
            straight.append(entry['uv_s'])
            auto.append(entry['uv_auto'])

        s = {
            'name': '抗UV直傘',
            'data': straight,
            'color': 'green',
        }

        au = {
            'name': '抗UV手開摺傘',
            'data': auto,
            'color': 'red',
        }


        chart = {
            'chart': {'type': 'column'},
            'title': {'text': '傘'},
            'xAxis': {'categories': categories},
            'series': [s, au],
            'plotOptions': {
			    'series': {
        	        'grouping': False,
			    }
		    }
        }


        dump = json.dumps(chart)

        return render(request, 'modules/member/member.html', {'chart': dump})