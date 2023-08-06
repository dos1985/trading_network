from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from trading.models import Factory, RetailNetwork, IndividualEntrepreneur, Product
from trading.permissions import IsActiveEmployee
from trading.serializers import FactorySerializer, RetailNetworkSerializer, IndividualEntrepreneurSerializer, \
    ProductSerializer


class FactoryCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated, IsActiveEmployee]
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class FactoryListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated, IsActiveEmployee]
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = ['name', 'country']
    ordering_fields = ["name", "created"]
    ordering = ["name"]
    search_fields = ["name"]

    # def get_queryset(self):
    #     user = self.request.user
    #     return Factory.objects.filter(
    #         board__participants__user=user
    #     ).exclude(is_deleted=True).distinct()


class FactoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class RetailNetworkCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer


class RetailNetworkListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer


class RetailNetworkRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer


class IndividualEntCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = IndividualEntrepreneurSerializer


class IndividualEntListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = IndividualEntrepreneurSerializer


class IndividualEnRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = IndividualEntrepreneurSerializer


class ProductCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
