from django.urls import path

from resumes import views
urlpatterns=[
    path('form',views.form,name="form"),
    path('form2',views.form2,name="form2"),
    path('pdf_reader',views.pdf_reader,name="pdf_reader"),
    path('uploadresume',views.uploadresume,name="uploadresume"),
  
   path('extract_details_from_cv',views.extract_details_from_cv,name="extract_details_from_cv"),
   path('savedetails',views.savedetails,name="savedetails"),

]