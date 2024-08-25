import json

from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Product, Category, Order, OrderItem
from .serializers import ProductSerializer, CategorySerializer, OrderSerializers, OrderItemSerializer


# Create your views here.
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def OrderList(request):
    try:
        orders = Order.objects.all()
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializers(orders, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        total_price = 0
        for product in request.data["products"]:
            product_price = Product.objects.get(id=product["id"])
            total_price += product_price.price * product["quantity"]
        request.data["total_price"] = total_price
        serializer = OrderSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def OrderListEach(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = OrderSerializers(order)
        return Response(serializer.data)
    elif request.method == 'PUT':
        total_price = 0
        products_data = request.data.get("products", [])

        for product in products_data:
            try:
                product_instance = Product.objects.get(id=product["id"])
            except Product.DoesNotExist:
                return Response({"error": f"Product with id {product['id']} not found"},
                                status=status.HTTP_404_NOT_FOUND)

            total_price += product_instance.price * product["quantity"]

        # Update the total_price in the request data
        request.data["total_price"] = total_price

        # Create the serializer instance, passing the order object to update
        serializer = OrderSerializers(order, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        order.delete()
        return Response({'message': 'Profile deleted'}, status=status.HTTP_204_NO_CONTENT)


class OrderItemList(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def OrderItemListDetail(request, pk):
    try:
        order = OrderItem.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = OrderItemSerializer(order)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = OrderItemSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        order.delete()
        return Response({'message': 'Profile deleted'}, status=status.HTTP_204_NO_CONTENT)
