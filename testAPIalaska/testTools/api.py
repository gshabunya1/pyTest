import logging
import requests

class Api:
    LOGGER = logging.getLogger(__name__)

    BASE_URL = "http://localhost:8091"
    BEAR_URL = BASE_URL + "/bear"
    BEAR_ID_URL = BASE_URL + "/bear/{0}"
    HEADER = {'Content-Type': 'application/json'}

    @staticmethod
    def get_info():
            result = requests.get(Api.BASE_URL+"/info")
            Api.LOGGER.info('TEST: Get info. Method: {0}, URL: {1}'.format("GET", Api.BASE_URL+"/info"))
            return result

    @staticmethod
    def create_bear(body):
            result = requests.post(Api.BEAR_URL,
                     json=body)
            Api.LOGGER.info('TEST: Create bear. Method: {0}, URL: {1}, Data: {2}'.format("POST", Api.BEAR_URL, body))
            return result

    @staticmethod
    def update_bear(bear_id, body):
            result = requests.put(Api.BEAR_ID_URL.format(bear_id),
                      params=body)
            Api.LOGGER.info('TEST: Update bear. Method: {0}, URL: {1}, Data: {2}'.format("PUT", Api.BEAR_ID_URL.format(bear_id), body))
            return result

    @staticmethod
    def get_bear(bear_id):
            result = requests.get(Api.BEAR_ID_URL.format(bear_id))
            Api.LOGGER.info('TEST: Get bear. Method: {0}, URL: {1}'.format("GET", Api.BEAR_ID_URL.format(bear_id)))
            return result

    @staticmethod
    def get_bears():
            result = requests.get(Api.BEAR_URL)
            Api.LOGGER.info('TEST: get bears. Method: {0}, URL: {1}'.format("GET", Api.BEAR_URL))
            return result

    @staticmethod
    def delete_bear(bear_id):
            result = requests.delete(Api.BEAR_ID_URL.format(bear_id))
            Api.LOGGER.info(
                'TEST: Delete bear. Method: {0}, URL: {1}'.format("DELETE", Api.BEAR_ID_URL.format(bear_id)))
            return result

    @staticmethod
    def delete_bears():
            result = requests.delete(Api.BEAR_URL)
            Api.LOGGER.info('TEST: Delete bears. Method: {0}, URL: {1}'.format("DELETE", Api.BEAR_URL))
            return result