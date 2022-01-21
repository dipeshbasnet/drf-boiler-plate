from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.commons.mixins.viewsets import ListCreateRetrieveViewSetMixin
from apps.core.models import DemoModel
from ..serializer.demo import DemoSerializer


class DemoView(APIView):
    permission_classes = AllowAny,

    def get(self, *args, **kwargs):
        return Response({'detail': 'This is working!'})


class DemoViewSet(ListCreateRetrieveViewSetMixin):
    permission_classes = AllowAny,
    serializer_class = DemoSerializer
    queryset = DemoModel.objects.all()

