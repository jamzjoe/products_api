from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response({'products': serializer.data})

@api_view(['POST'])
def addItem(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deleteItem(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    
    except Product.DoesNotExist:
        return Response({'error': 'Product not found.'}, status=404)
    if product.type == 'water storage':
        return Response({'cant delete water storage item'})
    product.delete()
    return Response({'message': 'Product deleted successfully!'})

@api_view(['PUT'])
def updateItem(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found.'}, status=404)

    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)
