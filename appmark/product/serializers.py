from rest_framework import serializers

from product.models import ProdFood


class ProdFoodSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    prod_code = serializers.CharField(max_length=20, required=True)
    prod_name = serializers.CharField(max_length=200, required=True)
    prod_price = serializers.FloatField(required=True)
    prod_gallery = serializers.CharField(max_length=200)
    prod_image = serializers.ImageField()

    def create(self, validated_data):
        return ProdFood.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.prod_code = validated_data.get('code', instance.prod_code)
        instance.prod_name = validated_data('name', instance.prod_name)
        instance.prod_price = validated_data('price', instance.prod_price)
        instance.prod_gallery = validated_data('gallery', instance.prod_gallery)
        instance.prod_image = validated_data('image', instance.prod_image)
        instance.save()
        return instance
