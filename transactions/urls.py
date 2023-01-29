from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import  upload_file


urlpatterns = [
    # path("transactions/", views.TransactionsView.as_view()),
    # path("upload/", handle_upload, name="upload"),
    path("upload/", upload_file, name="upload"),
   
]