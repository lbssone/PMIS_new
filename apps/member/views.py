import json
from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, View
from django.db.models import Count, Q

from mysite.views import ListView
from .models import Member

# Create your views here.
class MemberList(View):
    # model = Member
    # template_name = 'modules/member/member.html'
    # context_object_name = 'member_list'
    # base_url = 'member:list'

    def get(self, request):
        dataset = Member.objects \
            .values('working_school_address') \
            .annotate(north_count=Count('working_school_address', filter=Q(working_school_address="北部")),
                    central_count=Count('working_school_address', filter=Q(working_school_address="中部")),
                    south_count=Count('working_school_address', filter=Q(working_school_address="南部"))) \
            .order_by('working_school_address')

        categories = list()
        north_data = list()
        central_data = list()
        south_data = list()

        for entry in dataset:
            categories.append(entry['working_school_address'])
            north_data.append(entry['north_count'])
            central_data.append(entry['central_count'])
            south_data.append(entry['south_count'])

        north = {
            'name': '北部',
            'data': north_data,
            'color': 'green',
        }

        central = {
            'name': '中部',
            'data': central_data,
            'color': 'red',
        }

        south = {
            'name': '南部',
            'data': south_data,
            'color': 'blue',
        }

        chart = {
            'chart': {'type': 'column'},
            'title': {'text': '會員居住地分布'},
            'xAxis': {'categories': categories},
            'series': [north, central, south],
            'plotOptions': {
			    'series': {
        	        'grouping': False,
			    }
		    }
        }


        dump = json.dumps(chart)

        return render(request, 'modules/member/member.html', {'chart': dump})