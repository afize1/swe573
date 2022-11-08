from user.api.viewsets import userviewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('userr', userviewsets, base_name='user_apii')
