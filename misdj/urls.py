
from django.contrib import admin
from django.urls import path,include 
from django.views.generic.base import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('case005.urls')), 
    path('help/', TemplateView.as_view(template_name="club/help.html")),
    path('about/', TemplateView.as_view(template_name="portal/about.html")),
   
    path('', include('club.urls')), 
   
]
# https://wsvincent.com/django-image-uploads/
# if settings.DEBUG: # new
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)