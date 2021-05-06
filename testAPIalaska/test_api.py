import pytest
from requests import Response
from testAPIalaska.testTools.api import Api
import logging

class Test_bear:
    LOGGER = logging.getLogger(__name__)
    first_test_id = 1

    def test_info_bear(self):
        result = Response = Api.get_info()
        print(result.text)
        assert 200 == result.status_code
        assert result.text.find("Welcome to Alaska!") == 0

    def test_create_bear(self):
        firstBear = {"bear_type": "POLAR", "bear_name": "Snowball", "bear_age": 7.5}
        result: Response = Api.create_bear(firstBear)
        assert 200 == result.status_code

        result: Response = Api.get_bears()
        assert 200 == result.status_code
        Test_bear.first_test_id = result.json()[0]["bear_id"]
        assert "EMPTY" != result.text

    def test_update_bear(self):
        secondBear = {"bear_type": "BROWN", "bear_name": "Mikhail", "bear_age": 12.5}
        updateBear = {"bear_type": "BLACK", "bear_name": "Mikhail", "bear_age": 12.5}
        result: Response = Api.create_bear(secondBear)
        assert 200 == result.status_code
        Test_bear.first_test_id = Test_bear.first_test_id + 1

        result: Response = Api.update_bear(Test_bear.first_test_id, updateBear)
        assert 200 == result.status_code

        result: Response = Api.get_bear(Test_bear.first_test_id)
        assert 200 == result.status_code
        assert updateBear['bear_type'] == result.json()['bear_type']

    def test_delete_bear(self):
        thirdBear = {"bear_type": "GUMMY", "bear_name": "Wizard", "bear_age": 117.5}

        result: Response = Api.create_bear(thirdBear)
        assert 200 == result.status_code

        Test_bear.first_test_id = Test_bear.first_test_id + 1
        print("===> ID", Test_bear.first_test_id + 1)

        result: Response = Api.delete_bear(Test_bear.first_test_id)
        assert 200 == result.status_code

        result: Response = Api.get_bear(Test_bear.first_test_id)
        assert 200 == result.status_code
        assert "EMPTY" == result.text

    def test_delete_bears(self):
        result: Response = Api.get_bears()
        assert 200 == result.status_code
        assert 2 == len(result.json())

        result: Response = Api.delete_bears()
        assert 200 == result.status_code

        result: Response = Api.get_bears()
        assert 200 == result.status_code
        assert "[]" == result.text



