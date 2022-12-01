from django.shortcuts import get_object_or_404, render

from .models import Department, Medic


def product_all(request):
    products = Medic.objects.all()
    return render(request, "catalogue/index.html", {"products": products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Department, slug=category_slug)
    products = Medic.objects.filter(
        category__in=Department.objects.get(name=category_slug).get_descendants(include_self=True)
    )
    return render(request, "catalogue/category.html", {"category": category, "products": products})


def product_detail(request, slug):
    product = get_object_or_404(Medic, slug=slug)
    return render(request, "catalogue/single.html", {"product": product})
