

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [path("",views.index),
    path("result/<slug:question>/<int:id>/>,",views.solutions,name="fetch_Detail"),
    path("submit/",views.imagesfn),
    path("ssearch/",views.search_str),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
