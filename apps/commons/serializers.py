from django.utils.functional import cached_property
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class DynamicFieldsModelSerializer(ModelSerializer):
    # see: https://www.django-rest-framework.org/api-guide/serializers/#dynamically-modifying-fields
    # modified to support exclude_fields , and request as attribute
    def __init__(self, instance=None, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)
        exclude_fields = kwargs.pop('exclude_fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(
            instance, *args, **kwargs
        )

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    @cached_property
    def request(self):
        return self.context.get("request")


class DummySerializer(serializers.Serializer):
    # dummy serializer for using when serializer class is needed in viewset but actual serializer is not used
    # for maintaining swagger doc
    pass
