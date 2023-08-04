from rest_framework import serializers

from trading.models import Factory, RetailNetwork, IndividualEntrepreneur, Product


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = "__all__"
        # fields = ['name', 'email', 'country', 'city', 'street', 'house_number',
        #           'product_name', 'product_model', 'product_release_date', 'supplier', 'debt']
        read_only_fields = ['debt_to_supplier']



class RetailNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetailNetwork
        fields = "__all__"
        read_only_fields = ['debt_to_supplier']


class IndividualEntrepreneurSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualEntrepreneur
        fields = "__all__"
        read_only_fields = ['debt_to_supplier']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ['debt_to_supplier']
