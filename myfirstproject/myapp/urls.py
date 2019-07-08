
from django.conf.urls import url
# from.views import  register
from  .views import marks,register_view,StudentMarks, reg_form

urlpatterns = [

   # url(r'registrationform/',register),
   url(r'marks/', marks),
   url(r'regform/', reg_form),
   url(r'register/', register_view),
   url(r'studentmarks/', StudentMarks.as_view),

]