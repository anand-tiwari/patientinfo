from django.conf.urls import url, include
from django.contrib import admin
from patientinformation import views as patientinformation_views

urlpatterns = [
	url(r'^$',patientinformation_views.home, name='home'),
    
    url(r'^addpatient/$',patientinformation_views.addpatient, name='addpatient'),
	url(r'^showpatient$',patientinformation_views.showpatient, name='showpatient'),
    url(r'^deletepatient$',patientinformation_views.deletepatient, name='deletepatient'),

    url(r'^admin/', admin.site.urls),
]