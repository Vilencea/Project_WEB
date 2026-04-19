from rest_framework import serializers

class itemSerial(serializers.Serializer):
    product_id= serializers.IntegerField()
    quantity= serializers.IntegerField(min_value=1)
class checkoutSerial(serializers.Serializer):
    items= itemSerial(many=True)
    delivery_address= serializers.CharField()
    promik= serializers.CharField(required=False, allow_blank=True)
    