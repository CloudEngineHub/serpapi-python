"""SerpApi client library for python"""
import json
import urllib3
from .error import SerpApiException
from .object_decoder import ObjectDecoder

class HttpClient:
    """Simple HTTP client wrapper around urllib3"""

    def __init__(self, parameter: dict = {}):
        # initialize the http client
        self.http = urllib3.PoolManager()

        # urllib3 configurations
        # HTTP connect timeout 
        if 'timeout' in parameter:
            self.timeout = parameter['timeout']
        else:
            # 60s default
            self.timeout = 60.0
        
        # no HTTP retry
        if 'retries' in parameter:
            self.retries = parameter['retries']
        else:
            self.retries = False

    def start(self, path : str, parameter: dict = None, decoder : str = 'json'):
        """
        start HTTP request and decode response using urllib3
         the response is decoded using the selected decoder:
          - html: raw HTML response
          - json: deep dict contains search results
          - object: containing search results as a dynamic object

        Parameters:
        ---
        path: str
          HTTP endpoint path under serpapi.com/<path>
        decoder: str
          define how to post process the HTTP response.
           for example: json -> convert response to a dict
            using the default JSON parser from Python
        parameter: dict
          search query

        Returns:
        ---
        dict|str|object
        decoded HTTP response
        """
        # set client language
        self.parameter['source'] = 'python'

        # set output type
        if decoder == 'object':
            self.parameter['output'] = 'json'
        else:
            self.parameter['output'] = decoder

        # merge parameter defaults and overrides
        fields = self.parameter.copy()
        fields.update(parameter)

        # execute HTTP get request
        response = self.http.request('GET',
                                     self.BACKEND + path,
                                     fields=fields,
                                     timeout=self.timeout,
                                     retries=self.retries)
        # decode response
        return self.decode(response, decoder)

    def decode(self, response: any, decoder: str):
        """Decode HTTP response using a given decoder"""
        # handle HTTP error
        if response.status != 200:
            try:
                raw = response.data.decode('utf-8')
                payload = json.loads(raw)
                raise SerpApiException(payload['error'])
            except Exception as ex:
                raise SerpApiException(raw) from ex

        # HTTP success 200
        payload = response.data.decode('utf-8')

        # successful response decoding
        if decoder == 'json':
            return json.loads(payload)

        if decoder == 'html':
            return payload

        if decoder == 'object':
            data = json.loads(payload)
            return self.dict2object(data)

        raise SerpApiException("Invalid decoder: " +
                               decoder + ", available: json, html, object")

class Client(ObjectDecoder, HttpClient):
    """
    Client performend http query to serpApi.com using urllib3 under the hood.

    The HTTP connection be tuned to allow
     - retries : attempt to reconnect if the connection fail by default: False
     - timeout : connection timeout by default 60s
    for more details:  https://urllib3.readthedocs.io/en/stable/user-guide.html

    """

    BACKEND = 'https://serpapi.com'
    SUPPORTED_DECODER = ['json', 'html', 'object']

    def __init__(self, parameter: dict = None):
        # define default parameter
        if parameter is None:
            self.parameter = {}
        else:
            # assign user parameter
            self.parameter = parameter
        HttpClient.__init__(self, self.parameter)

    def search(self, parameter: dict = None, decoder: str = 'json'):
        """
        make search then decode the output
         decoder supported 'json', 'html', 'object'

        Parameters
        ----------
        parameter : dict
            search query
        decoder : str
            set decoder to convert the datastructure received from

        Returns
        -------
        dict|str
            search results returns as :
             dict if decoder = 'json'
             str if decoder = 'html'
             object if decoder = 'object'
        """
        return self.start(path='/search', parameter=parameter, decoder=decoder)

    def html(self, parameter: dict = None):
        """
        html search

        Parameters
        ----------
        parameter : dict
            search query see: https://serpapi.com/search-api

        Returns
        -------
        str
        raw html search results directly from the search engine
        """
        return self.start('/search', parameter, 'html')

    def location(self, parameter: dict = None):
        """
        Get location using Location API

        Parameters
        ----------
        parameter : dict
            location query like: {q: "Austin", limit: 5}
             see: https://serpapi.com/locations-api

        Returns
        -------
        array
        list of matching locations
        """
        return self.start('/locations.json', parameter, 'json')

    def search_archive(self, search_id : str, decoder : str ='json'):
        """
        Retrieve search results from the Search Archive API

        Parameters:

        """
        path = "/searches/" + str(search_id) + "."
        if decoder in self.SUPPORTED_DECODER:
            if decoder == "object":
                path += "json"
            else:
                path += decoder
        else:
            raise SerpApiException('Decoder must be json or html or object')
        return self.start(path, {}, decoder)

    def account(self, api_key: str = None):
        """
        Get account information using Account API

        Parameters
        ---
        api_key: str
          secret user key provided by serpapi.com

        Returns
        ---
        dict
        user account information
        """
        if api_key is not None:
            self.parameter['api_key'] = api_key
        return self.start('/account', self.parameter, 'json')
