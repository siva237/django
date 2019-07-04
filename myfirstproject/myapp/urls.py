
from django.conf.urls import url
# from.views import  register
from  .views import marks

urlpatterns = [

   # url(r'registrationform/',register),
   url(r'marks/', marks)

]