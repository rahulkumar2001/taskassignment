from django.urls import path
#now import the views.py file into this code
from myapp import views
urlpatterns=[
  path('',views.Donordata.as_view(), name="donordata")

]