
from django.conf.urls import url
from django.contrib import admin
from App01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^form/', views.feedbackview),
]
