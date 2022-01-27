import imp
import json
from urllib import response
import requests
import pytest
from assertpy import assert_that

class TestGetData():
    curl = ('https://airportgap.dev-tester.com/api/airports')

    def _test_get_first_data(self):
        data = requests.get(self.curl)
        return data.json().get('data')[0].get('id')
    
    def testGetAll(self):
        response = requests.get(self.curl)

        assert_that(response.status_code).is_equal_to(200)
    
    def testGetById(self):
        airport_id = self._test_get_first_data

        response = requests.get(f"{self.curl}/{airport_id}")

        assert_that(response.status_code).is_equal_to(200)
        json_code = response.json().get('data')
        assert_that(json_code['data']['attributes']['id']).is_equal_to('WWK')
