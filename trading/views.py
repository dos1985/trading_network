from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from trading.permissions import *
from trading.serializers import *
from rest_framework.generics import *


class FactoryCreateAPIView(CreateAPIView):
    """Класс для создания записей о фабриках"""
    permission_classes = [IsAdminUser]
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class FactoryListAPIView(ListAPIView):
    """Класс для просмотра списка фабрик с возможностью сортировки, фильтрации и поиска"""
    permission_classes = [IsAuthenticated, IsActiveEmployee]
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = ['name', 'country']
    ordering_fields = ["name", "created", 'debt_to_supplier']
    ordering = ["name"]
    search_fields = ["name"]


class FactoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """Класс для просмотра, обновления или удаления конкретной записи о фабрике"""
    permission_classes = [IsAuthenticated, IsActiveEmployee, IsOwnerOrReadOnly]
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class RetailNetworkCreateAPIView(CreateAPIView):
    """Класс для создания записей о розничных сетях"""
    permission_classes = [IsAuthenticated]
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer

    def perform_create(self, serializer):
        # Устанавливаем текущего пользователя в качестве владельца продукта
        serializer.save(user=self.request.user)


class RetailNetworkListAPIView(ListAPIView):
    """Класс для просмотра списка розничных сетей с возможностью сортировки, фильтрации и поиска"""
    permission_classes = [IsAuthenticated, IsActiveEmployee]
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = ['name', 'country']
    ordering_fields = ["name", "created", 'debt_to_supplier']
    ordering = ["name"]
    search_fields = ["name"]


class RetailNetworkRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """Класс для просмотра, обновления или удаления конкретной записи о розничной сети"""
    permission_classes = [IsAuthenticated, IsActiveEmployee, IsOwnerOrReadOnly]
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer




class IndividualEntCreateAPIView(CreateAPIView):
    """Класс для создания записей о индивидуальных предпринимателях"""
    permission_classes = [IsAuthenticated]
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = IndividualEntrepreneurSerializer

    def perform_create(self, serializer):
        # Устанавливаем текущего пользователя в качестве владельца продукта
        serializer.save(user=self.request.user)



class IndividualEntListAPIView(ListAPIView):
    """Класс для просмотра списка индивидуальных предпринимателей с возможностью сортировки, фильтрации и поиска"""
    permission_classes = [IsAuthenticated, IsActiveEmployee]
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = IndividualEntrepreneurSerializer
    filterset_fields = ['name', 'country']
    ordering_fields = ["name", "created", 'debt_to_supplier']
    ordering = ["name"]
    search_fields = ["name"]



class IndividualEnRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """Класс для просмотра, обновления или удаления конкретной записи об индивидуальном предпринимателе"""
    permission_classes = [IsAuthenticated, IsActiveEmployee, IsOwnerOrReadOnly]
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = IndividualEntrepreneurSerializer


class ProductCreateAPIView(CreateAPIView):
    """Класс для создания записей о продуктах"""
    permission_classes = [IsAuthenticated, IsActiveEmployee]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # Устанавливаем текущего пользователя в качестве владельца продукта
        serializer.save(user=self.request.user)


class ProductListAPIView(ListAPIView):
    """Класс для просмотра списка продуктов с возможностью сортировки, фильтрации и поиска"""
    permission_classes = []
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['name']
    ordering_fields = ["name", 'model', 'release_date', "created", 'price', 'category', 'rating']
    ordering = ["name"]
    search_fields = ["name"]


class ProductDetailAPIView(RetrieveAPIView):
    """Класс для просмотра деталей о конкретном продукте"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """Класс для просмотра, обновления или удаления конкретной записи о продукте"""
    permission_classes = [IsAuthenticated, IsActiveEmployee, IsOwnerOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartItemListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemSerializer

    def get_queryset(self):
        user = self.request.user
        return CartItem.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CartItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemSerializer

    def get_queryset(self):
        user = self.request.user
        return CartItem.objects.filter(user=user)
