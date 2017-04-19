import os.path

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

import unittest

try:
    from urllib.parse import urlparse
    from urllib.error import HTTPError
except ImportError:
    from urlparse import urlparse
    from urllib2 import HTTPError

from app.client import ConsumingPublicApi


def fake_urlopen(request):
    """
    A stub urlopen() implementation that load json responses from
    the filesystem.
    """
    # Map path from url to a file
    parsed_url = urlparse(request.get_full_url())
    resource_file = os.path.normpath('test/resources%s' % parsed_url.path)
    # Must return a file-like object
    try:
        return open(resource_file, mode='rb')
    except IOError:
        raise HTTPError(request.get_full_url, 404, "HTTP Error : 404 - Resource not found", {}, None)

    

class ClientTestCase(unittest.TestCase):
    """Test case for the client methods."""
    def setUp(self):
        self.patcher = patch('app.client.urlopen', fake_urlopen)
        self.patcher.start()
        self.client = ConsumingPublicApi()
    def tearDown(self):
        self.patcher.stop()
    def test_request(self):
        """Test a simple request."""
        user = 'test_user'
        response = self.client.request(user)
        self.assertIn('name', response)
        self.assertEqual(response['name'], 'Male Michael')
    def test_unknown_user(self):
        """Test a simple request."""
        user = 'unknown_test'
        response = self.client.request(user)
        self.assertEqual(response, 'Client doesnot exist')
    def test_arg_not_string_raises_type_error(self):
        self.assertRaises(TypeError, self.client.request, 1)