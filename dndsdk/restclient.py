
import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from urllib.parse import urlencode


class RestClient(object):

    @staticmethod
    def get(url, params={}):
        '''invokes an http GET on url
        Args:
            url(string): URL endpoint to request
            params(dict):dictionsry of url paramaters
        Returns:
            dict : JSON response as a dict
        '''

        request_url = url

        if len(params):
            request_url = "{}?{}".format(url, urlencode(params))

        try :
            req = Request(request_url, headers={'User-Agent' :'Mozilla/5.0'})
            print(request_url)
            response = json.loads(urlopen(req).read().decode("utf-8"))
            return response
        except HTTPError as err:
            raise DndException(err.read())

class DndException(Exception) :
    def __init__(self, description) :
        self.description = description

    def __str__(self):
        return self.description
