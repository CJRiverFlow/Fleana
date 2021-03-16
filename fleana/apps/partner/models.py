from django.db import models
from oscar.apps.partner.abstract_models import AbstractPartner

#Check documentation about overriding apps.
class Partner(AbstractPartner):
    Company = models.CharField(max_length=200, blank=True)


from oscar.apps.partner.models import *  # noqa isort:skip
