from apps.commons.serializers import DynamicFieldsModelSerializer

from ....models import DemoModel


class DemoSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model= DemoModel
        fields = '__all__'  # in real case scenario, don't use __all__, declare fields
