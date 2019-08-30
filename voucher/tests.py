'''
Tests for documents endpoint
'''
from rest_framework.test import APIClient as Client
from rest_framework.test import APITestCase
from .factories import VoucherFactory

class VoucherViewsetTests(APITestCase):
    '''Tests for /vouchers/ endpoint'''

    def setUp(self):
        self.tester = Client()
        self.base_url = '/vouchers/'
        self.rec = VoucherFactory()
        self.rec_url = '{}{}/'.format(
            self.base_url,
            self.rec.id
        )

    def test_can_get_list(self):
        '''CAN LIST the index'''
        response = self.tester.get(self.base_url)
        self.assertEqual(response.status_code, 200)

    def test_can_create(self):
        '''CAN POST new records'''
        response = self.tester.post(self.base_url, {
            "code": "SNSD",
            "value": "100000",
            "during": {
                    "lower": "2017-11-14 17:00:00",
                    "upper": "2017-11-25 17:00:00",
                    "bounds": "[)"
                }
        }, 'json')
        self.assertEqual(response.status_code, 201)

    def test_cannot_create(self):
        '''CANNOT POST new overlap records'''
        response = self.tester.post(self.base_url, {
            "code": "SNSD",
            "value": "200000",
            "during": {
                    "lower": "2019-10-24 17:00:00",
                    "upper": "2019-11-29 17:00:00",
                    "bounds": "[)"
                }
        }, 'json')
        self.assertEqual(response.status_code, 400)

    def test_can_get_details(self):
        '''CAN GET the details on a Voucher'''
        response = self.tester.get(self.rec_url)
        self.assertEqual(response.status_code, 200)

    def test_can_update(self):
        '''Can PATCH a result to change a single field'''
        response = self.tester.patch(self.rec_url, {
            'value': '200000'
        }, 'json')
        self.assertEqual(response.status_code, 200)

    def test_can_delete(self):
        '''Can DELETE a post'''
        url = '{}{}/'.format(self.base_url, self.rec.id)
        response = self.tester.delete(url)
        self.assertEqual(response.status_code, 204)
