# This file has been copied from the following project:
# https://github.com/MattBCoding/druid-pp5/blob/main/products/utils.py

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginateProducts(request, products, results):
    """
    Returns a paginated range and the query
    """
    page = request.GET.get('page')
    paginator = Paginator(products, results)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        products = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        products = paginator.page(page)

    leftIndex = (int(page) - 1)
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = (int(page) + 2)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, products
