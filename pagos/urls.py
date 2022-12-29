from . import api
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from version2.v2.api import ExpiredPaymentViewUser, PaymentUsersViewUser, ServicesViewUser

router = routers.DefaultRouter()
router.register(r'pagos', api.PagoViewSet, 'pagos')

router.register(r"services", ServicesViewUser, basename = "services")
router.register(r"payment-users", PaymentUsersViewUser, basename = "payment-user")
router.register(r"expired-payment", ExpiredPaymentViewUser, basename = "expired-payment")



urlpatterns = router.urls


