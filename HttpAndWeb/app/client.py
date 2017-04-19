import json
try:
    from urllib.request import urlopen, Request
    from urllib.error import HTTPError
except ImportError:
    from urllib2 import urlopen, Request, HTTPError


class ConsumingPublicApi(object):
    def __init__(self):
        self.url = 'https://api.github.com/users/'

    def request(self, user):
        if isinstance(user, str):
            self.url += "%s" % user
            request = Request(self.url)
            try:
                response = urlopen(request)
            except HTTPError:
                return "Client doesnot exist"
            raw_data = response.read()
            return json.loads(raw_data)
        else:
            raise TypeError