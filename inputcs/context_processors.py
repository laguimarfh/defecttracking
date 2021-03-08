from django.db.models import Count
from . import models


def base_context(request):
    defects = models.Sheet.objects.all().order_by('id')[:10]
    coord = models.AjaxImage.objects.all()

    return {
        'defects': defects,
        'coord' : coord,
    }
