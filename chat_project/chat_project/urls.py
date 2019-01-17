from django.contrib import admin
from django.urls import path, include

from django.views.generic.base import TemplateView

# Template View :::: TemplateView should be used when you want to present some information in a html page.
# eg. about us like pages which are static .

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('chat/', include('chat.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

]