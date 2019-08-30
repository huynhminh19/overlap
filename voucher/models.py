from .contrib.postgres.constraints import ExclusionConstraint
from .contrib.postgres.fields import RangeOperators
from django.contrib.postgres.fields import DateTimeRangeField
from django.db import models

class Voucher(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=10, default='SNSD')
    value = models.DecimalField(max_digits=19, decimal_places=10)
    during = DateTimeRangeField()

    class Meta:
        ordering = ('created',)
        constraints = [
            ExclusionConstraint(
                name='exclude_overlapping_vouchers',
                expressions=[
                    ('during', RangeOperators.OVERLAPS),
                    ('code', RangeOperators.EQUAL),
                ]
            ),
        ]
