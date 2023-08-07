from rest_framework import serializers

from trading.models import Factory, RetailNetwork, IndividualEntrepreneur, Product, CartItem


class FactorySerializer(serializers.ModelSerializer):
    """Сериализатор для объектов Factory (Завод).
    """
    class Meta:
        model = Factory
        fields = "__all__"
        read_only_fields = ['debt_to_supplier']#Поле 'debt_to_supplier' доступно только для чтения.


class RetailNetworkSerializer(serializers.ModelSerializer):
    """Сериализатор для объектов RetailNetwork (Розничная сеть).
    """
    class Meta:
        model = RetailNetwork
        fields = "__all__"
        read_only_fields = ['user', 'debt_to_supplier']#Поле 'debt_to_supplier' доступно только для чтения.


class IndividualEntrepreneurSerializer(serializers.ModelSerializer):
    """Сериализатор для объектов IndividualEntrepreneur (Индивидуальный предприниматель).
    """
    class Meta:
        model = IndividualEntrepreneur
        fields = "__all__"
        read_only_fields = ['user', 'debt_to_supplier']#Поле 'debt_to_supplier' доступно только для чтения.



class ProductSerializer(serializers.ModelSerializer):
    """ Сериализатор для объектов Product (Продукт).
    """
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'image', 'rating', 'user', 'release_date', 'supplier', 'model', 'created']
        read_only_fields = ['user', 'debt_to_supplier']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('id', 'user', 'product', 'quantity')
