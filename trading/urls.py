from django.urls import path

from trading.views import FactoryCreateAPIView, FactoryListAPIView, FactoryRetrieveUpdateDestroyAPIView, \
    RetailNetworkCreateAPIView, RetailNetworkListAPIView, RetailNetworkRetrieveUpdateDestroyAPIView, \
    IndividualEntCreateAPIView, IndividualEntListAPIView, IndividualEnRetrieveUpdateDestroyAPIView, \
    ProductCreateAPIView, ProductListAPIView, ProductUpdateDestroyAPIView

urlpatterns = [
    path('factory/create', FactoryCreateAPIView.as_view(), name='factory-create'),
    path('factory/list', FactoryListAPIView.as_view(), name='factory-list'),
    path('factory/<int:pk>', FactoryRetrieveUpdateDestroyAPIView.as_view(), name='factory-detail'),
    path('retail/create', RetailNetworkCreateAPIView.as_view(), name='retail-create'),
    path('retail/list', RetailNetworkListAPIView.as_view(), name='retail-list'),
    path('retail/<int:pk>', RetailNetworkRetrieveUpdateDestroyAPIView.as_view(), name='retail-detail'),
    path('individual/create', IndividualEntCreateAPIView.as_view(), name='individual-create'),
    path('individual/list', IndividualEntListAPIView.as_view(), name='individual-list'),
    path('individual/<int:pk>', IndividualEnRetrieveUpdateDestroyAPIView.as_view(), name='individual-detail'),
    path('product/create', ProductCreateAPIView.as_view(), name='product-create'),
    path('product/list', ProductListAPIView.as_view(), name='product-list'),
    path('product/<int:pk>', ProductUpdateDestroyAPIView.as_view(), name='product-detail'),
]

