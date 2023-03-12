from django.urls import path
from ss.views import WatchesViews

app_name = 'watches'

urlpatterns = [
    path('', WatchesViews.as_view(), name='home'),
]