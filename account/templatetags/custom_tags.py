from django import template
register = template.Library()


from .models import ContractModel

@register.simple_tag
def contract_number():
    return ContractModel.objects..filter()count()