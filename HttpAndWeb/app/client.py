import json
try:
    # For Python 3.0 and later
    from urllib.request import urlopen, Request
    from urllib.error import HTTPError
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen, Request, HTTPError


class ConsumingPublicApi(object):
    #Initialise the url path to the web api
    def __init__(self):
        self.url = 'https://api.github.com/users/'

    def get_api_data(self, user):
        #Check that the argument value passed is a string 
        if isinstance(user, str):
            #Add the argument variable to the initialised url
            self.url += "%s" % user
            #Create a request object that is to be passed to the web api
            request = Request(self.url)
            try:
                #Make a call to the web api and store the response in a variable
                response = urlopen(request)
            except HTTPError:
                #Return an error message in case of failure to get data
                return "Client doesnot exist"
            #Convert the returned json object to a dictionary and return it
            raw_data = response.read()
            return json.loads(raw_data)
        else:
            raise TypeError