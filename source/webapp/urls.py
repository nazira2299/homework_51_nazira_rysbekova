from django.urls import path
from webapp.views import index
from webapp.views import cat_stats

urlpatterns = [
    path('', index),
    path('cat_stats', cat_stats)
]