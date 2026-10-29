from django.urls import path
from .views import (
    CategoryListView,
    CategoryDetailView,
    StoreListCreateView,
    StoreDetailView,
    ProductListCreateView,
    ProductDetailView,
    ReviewListCreateView,
    ReviewDetailView,
)

urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),


    path("stores/", StoreListCreateView.as_view(), name="store-list-create"),
    path("stores/<int:pk>/", StoreDetailView.as_view(), name="store-detail"),


    path("products/", ProductListCreateView.as_view(), name="product-list-create"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),


    path("reviews/", ReviewListCreateView.as_view(), name="review-list-create"),
    path("reviews/<int:pk>/", ReviewDetailView.as_view(), name="review-detail"),
]