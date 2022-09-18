
from .models import Category


def categories(request):
    return {
        'categories': Category.objects.all()  # use as context processor
    }
