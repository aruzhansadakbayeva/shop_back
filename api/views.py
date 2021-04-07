from django.http import HttpResponse, JsonResponse


def hello(request):
    return HttpResponse('<h1>hello message</h1>')


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


products = [
    {
        'id': i,
        'name': f'Product {i}',
        'price': i * 1000,
        'description': f'Product product',
        'count': i,
        'is_active': False

    }
    for i in range(1, 10)
]
categories = [
    {
        'id': i,
        'name': f'Category {i}'
    }
    for i in range(1, 10)

]


def product_list(request):
    return JsonResponse(products, safe=False)


def product_detail(request, product_id):
    for product in products:
        if product['id'] == product_id:
            return JsonResponse(product, status=200)
    return JsonResponse({'message': 'Product not found with selected ID'}, status=400)


def category_list(request):
    return JsonResponse(categories, safe=False)


def category_detail(request, category_id):
    for category in categories:
        if category['id'] == category_id:
            return JsonResponse(category, status=200)
    return JsonResponse({'message': 'Category not found with selected ID'}, status=400)
