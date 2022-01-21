# """
# v1 view for swagger
# """
# from rest_framework.response import Response
# from rest_framework.schemas import SchemaGenerator
# from rest_framework.views import APIView
# from rest_framework_swagger import renderers
#
#
# class SwaggerSchemaView(APIView):
#     """
#     Swagger Schema View class
#     """
#     renderer_classes = [
#         renderers.OpenAPIRenderer,
#         renderers.SwaggerUIRenderer,
#     ]
#     permission_classes = []
#
#     def get(self, request):
#         """
#         :param request: request object
#         :return: schema response
#         """
#         generator = SchemaGenerator(title='Project APIs', urlconf='apps.api.v1.urls', url="/api/v1/")
#         schema = generator.get_schema(request=request)
#         return Response(schema)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


