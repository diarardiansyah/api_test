from email import header
import json
from urllib import response
from wsgiref import headers
import requests
import pytest
import jsonpath
from assertpy import assert_that

class TestKirim:
    authen = {'Authorization' : 'Bearer token=TV2PAY7e4UCvT64zxRLhK64t'}
    url = ('https://airportgap.dev-tester.com/api/favorites')
    
    def test_post(self):
        response = requests.post(self.url, params={
            "airport_id" : "AEY",
            "note" : "coba test API"
        }, headers=self.authen)

        assert_that(response.status_code).is_equal_to(201)
        airport = response.json()["data"]["attributes"]["airport"]
        assert_that(airport["name"]).is_equal_to("Akureyri Airport")
        assert_that(airport["country"]).is_equal_to("Iceland")
        print(response.text)

    def test_get(self):
        response = requests.get(self.url, headers=self.authen)
        assert_that(response.status_code).is_equal_to(200)
        print(response.text)
        assert_that(len(response.json().get("data"))).is_greater_than_or_equal_to(1)
    
    def test_patch(self):
        response_id = requests.get(self.url, self.authen)

        airport_id = response_id.json().get("data")[0].get("id")
        payload = {
            'note' : 'edit yaaa gann'
        }

        response = requests.patch(f"{self.url}/{airport_id}",headers=self.authen, data=payload)
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json()["data"]["attributes"]["note"]).is_equal_to('edit yaaa gann')        
        

        