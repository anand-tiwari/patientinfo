"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from patientinformation import views as patientinformation_views

urlpatterns = [
	url(r'^$',patientinformation_views.home, name='home'),
    # delete below tow lines of code for navigation
    url(r'^patientform$',patientinformation_views.patientform, name='patientform'),
    url(r'^displaylist$',patientinformation_views.displayPage, name='displayPage'),

    url(r'^addpatient/$',patientinformation_views.addpatient, name='addpatient'),
	url(r'^showpatient$',patientinformation_views.showpatient, name='showpatient'),
    url(r'^deletepatient$',patientinformation_views.deletepatient, name='deletepatient'),

    url(r'^admin/', admin.site.urls),
]