from django.urls import include, path
from django.conf.urls import url
from rest_framework_nested import routers
from . import views

router = routers.SimpleRouter()
router.register(r'vouchers', views.VoucherViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
urlpatterns += [url(r'^silk/', include('silk.urls', namespace='silk'))]
