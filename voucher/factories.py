'''
Factories for Document
'''
from django.utils import timezone
import factory
from .models import Voucher
from psycopg2.extras import DateTimeTZRange

class VoucherFactory(factory.DjangoModelFactory):
    '''
    Class to generate fake Voucher
    '''

    class Meta:
        '''Metaclass'''
        model = Voucher
    created = factory.LazyFunction(timezone.now)
    code = 'SNSD'
    value = 50000
    during = DateTimeTZRange('2019-10-01T07:00:00Z', '2019-11-01T09:00:00Z', "[]")
