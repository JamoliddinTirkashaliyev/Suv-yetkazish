from django.contrib import admin
from django.urls import path, include
from mainApp.views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("adminlar", AdminSerializers)
router.register("buyurtmalar", BuyurtmalarModelViewSet)
router.register("suvlar", SuvlarModelViewSet)
router.register("haydovchilar", HaydovchilarModelViewSet)
router.register("mijozlar", MijozlarModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]
