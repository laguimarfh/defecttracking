from django.db.models import Count
from . import models


def base_context(request):
    defects = models.Sheet.objects.all()

    return {
        'defects': defects,
    }
