from django.urls import path
from . import views
from quotes.views import Imab5View

urlpatterns = [
    # path('v1/cota', Imab5View.as_view(), name='imab5'),
    path('v1/cota', views.get_imab5_quote, name='imab5'),
]