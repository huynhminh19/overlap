from rest_framework import serializers
from .models import Voucher
from drf_extra_fields.fields import DateTimeRangeField

class VoucherSerializer(serializers.ModelSerializer):
    during = DateTimeRangeField()
    class Meta:
        model = Voucher
        fields = ('code', 'value', 'during', 'created')
