# jims URL Configuration


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("summernote/", include("django_summernote.urls")),
    path("", include("home.urls")),
    path("accounts/", include("allauth.urls")),
    path("", include("contact.urls")),
    path("", include("blog.urls")),
    path("", include("menus.urls")),
    path("", include("bookings.urls")),

]

