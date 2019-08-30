from .serializers import VoucherSerializer
from rest_framework import viewsets
from .models import Voucher
from django.db import IntegrityError
from rest_framework.views import Response, exception_handler
from rest_framework import status
from psycopg2.extras import DateTimeTZRange

class VoucherViewSet(viewsets.ModelViewSet):
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer

    def get_queryset(self):
        queryset = self.queryset
        start = self.request.query_params.get('start', None)
        end = self.request.query_params.get('end', None)
        if start is not None and end is not None:
            queryset = queryset.filter(during__contained_by=DateTimeTZRange(start, end))

        return queryset

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            response = Response(
                {
                    'message': 'It seems there is a conflict between the data you are trying to save and your current '
                               'data. Please review your entries and try again.'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

            return response
