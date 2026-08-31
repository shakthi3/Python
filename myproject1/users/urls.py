from django.urls import path
from .import views

urlpatterns = [
  path("shakthi/",views.login1,name="shakthi"),
  path("home/",views.homepage,name="homepage"),
  path("loginprocess/",views.loginprocess,name="loginprocess"),
  path("adminpage/",views.adminpage,name="adminpage"),
  path("loaddata/",views.loaddata,name="loaddata"),
  path("loaddata/addrecordform/",views.addrecordform,name="addrecordform"),
  path("loaddata/addrecordform/addrecordprocess/",views.addrecordprocess,name="addrecordprocess"),
  path("loaddata/edit/<int:uid",views.editform,name="editform"),
  path("loaddata/edit/editrecordprocess/ss",views.editrecordprocess,name="editrecordprocess")
  #path("loaddata/delete",views.deleteform,name="deleteform"),
  ]