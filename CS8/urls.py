
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

class UserSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerilizer

router = routers.DefaultRouter()
router.register(r'users',UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include(router.urls)),
    re_path(r'^api/v1/login', include('Login.urls')),
    re_path(r'^api/v1/servicio/', include('Servicios.urls'))
    # path(r'^api-auth/', include('rest_framework.urls'))
]
