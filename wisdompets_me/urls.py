from django.contrib import admin
from django.urls import path

#need to import the views module inorder to refer those views on the patterns
#views will be defined in the adoptions app.
from adoptions import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('adoptions/<int:pet_id>/', views.pet_detail, name='pet_detail')
]#now go to adoptions annd views in it to write views