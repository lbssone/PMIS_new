import json
from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, View
from django.db.models import Count, Q
from datetime import datetime, timedelta

from mysite.views import ListView
from .models import Member
from apps.inventory.models import Product

# Create your views here.
class MemberSearch(View):
    def get(self, request):
        return render(request, 'modules/member/membersearch.html')

    def post(self, request):
        target_age = self.request.POST.get('target_age')
        target_gender = self.request.POST.get('target_gender')
        target_dwelling = self.request.POST.get('target_dwelling')
        if target_age == '全選' and target_gender == '全選' and target_dwelling == '全選':
            members = Member.objects.all()
        elif target_age == '全選' and target_gender == '全選':
            members = Member.objects.filter(dwelling=target_dwelling)
        elif target_age == '全選' and target_dwelling == '全選':
            members = Member.objects.filter(gender=target_gender)
        elif target_gender == '全選' and target_dwelling == '全選':
            members = Member.objects.filter(age=target_age)
        elif target_age == '全選':
            members = Member.objects.filter(gender=target_gender,dwelling=target_dwelling)
        elif target_gender == '全選':
            members = Member.objects.filter(age=target_age,dwelling=target_dwelling)
        elif target_dwelling == '全選':
            members = Member.objects.filter(age=target_age,gender=target_gender)
        else:
            members = Member.objects.filter(age=target_age, gender=target_gender, dwelling=target_dwelling)

        return render(request, 'modules/member/membersearch.html', locals())

class Piechart(View):
    def get(self, request):
        female_count=Member.objects.filter(gender='女性').count()
        male_count=Member.objects.filter(gender='男性').count()

        seventeen=Member.objects.filter(age='0-17歲').count()
        thirty=Member.objects.filter(age='18-30歲').count()
        forty=Member.objects.filter(age='31-40歲').count()
        fifty=Member.objects.filter(age='41-50歲').count()
        up=Member.objects.filter(age='51歲以上').count()

        north=Member.objects.filter(dwelling='北部').count()
        middle=Member.objects.filter(dwelling='中部').count()
        south=Member.objects.filter(dwelling='南部').count()
        east=Member.objects.filter(dwelling='東部').count()
        other=Member.objects.filter(dwelling='其他').count()

        return render(request, 'modules/member/piechart.html',locals())
