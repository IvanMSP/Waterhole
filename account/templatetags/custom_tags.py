from django import template
from django.db.models import Count,Sum
from ..models import ContractModel
from finanzas.models import Earning,OutflowsModel

register = template.Library()


@register.simple_tag
def contract_number():
    return ContractModel.objects.count()

@register.simple_tag
def total_earnings():
    total = Earning.objects.aggregate(total=Sum('quantity'))['total']
    return total

@register.simple_tag
def total_outflows():
    total = OutflowsModel.objects.aggregate(total=Sum('quantity'))['total']
    return total

@register.simple_tag
def dif_earnings():
    dif = total_earnings() - total_outflows()
    return dif