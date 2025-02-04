from django.urls import re_path
from LibApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    re_path(r'^lib/([0-9]+)/$',views.LibView),
    re_path(r'^profile/$',views.save_image),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)