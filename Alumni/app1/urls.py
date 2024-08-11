from django.urls import path
from app1 import views

urlpatterns=[
    path("",views.home,name="homepage"),
    path("about",views.about,name="aboutpage"),
    path("contact",views.contact,name="contactpage"),
    path("profile",views.profile,name="profilepage"),
    path("more",views.more,name="morepage"),
    path("dedicate/<int:rid>",views.dedicate,name="dedicatepage"),
    path("login",views.loginView,name="loginpage"),
    path("register",views.register,name="registerpage"),
    path("update/<int:rid>",views.update,name="updatepage"),
    path("logout",views.logoutView,name="logoutpage"),
    path("delete/<int:rid>",views.delete,name="deletepage"),
    path("staff",views.staff,name="staffpage"),
]