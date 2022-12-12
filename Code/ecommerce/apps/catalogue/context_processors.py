from .models import Department


def categories(request):
    return {"categories": Department.objects.all()}
