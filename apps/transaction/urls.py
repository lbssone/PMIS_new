from django.urls import path
from .views import TransactionYear, TransactionSeason, TransactionMonth, TransactionChart

# from .views import MemberList

app_name = "transaction"

urlpatterns = [
    # path('', MemberList.as_view(), name='list'),
    path('year/', TransactionYear.as_view(), name='year'),
    path('season/', TransactionSeason.as_view(), name='season'),
    path('month/', TransactionMonth.as_view(), name='month'),
    path('chart/', TransactionChart.as_view(), name='chart'),
]
