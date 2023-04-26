from main import views
from django.urls import path

urlpatterns = [
    path("login/", views.login_page,name="login"),
    path("newuser/", views.createAccount,name="newUser"),
    path("",views.mainPage,name="mainPage"),
    path("update/",views.updateDeviceData,name="updateData"),
    path("getdata",views.getdevicedata,name="getdata"),
    path("userinfo/",views.userProfileData,name="userinfo"),
    # path("test/",views.test,name="test"),
    path("logout/",views.logout_page,name="logout"),
    path("alldata/",views.get_all_data,name="alldata"),
    path("edituser/",views.user_edit,name="edituser"),
    path("seg/",views.seg,name="edituser"),
]