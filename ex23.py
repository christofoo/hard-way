# I was browsing github and found this stripe-python repo so I pulled up the api_requestor.py b/c i used to work with apis at paypal and wanted to see how they work
#th formatting is all fucked because I simply ctrl-c'd it instead of doing a git pull or anything. I kind of regret that. I could easily fix it.
# i don't know why i don't just pull it. I don't want more work i guess. Not that its that hard. now i've wasted so much time
#thats the lost time value fallacy or whatever. You should go do it its a good idea
# naaaaaahhhhhhhhhhhhhhhhhhhh......
#thats dumb
# i guess I'm kinda dumb
# do you want to just go through these or actually learn something?
#I am learning something
#ok now we're just wasting time
#you're wasting time
#thats what I said. I'm you. I'm just the smart version of you that keeps getting silenced by dumb you.
#lets move on, the purpose of this excercise is to identify pieces that you know from random .py code, not to have a formatting jerk-off session
#nvm I just ctrl-c'd from the "raw" version on github. Perfect formatting now :D


#this imports the calendar module. it doesn't say "from" anywhere... same with all the modules imported here
import calendar
import datetime
import platform
import time
import urllib
import urlparse
import warnings

import stripe
#except this one. it comes from 'stripe' which I'm guessing is on your system if you're working with this..
from stripe import error, http_client, version, util

# this make s a function called encode_datetime which callsthe argument dttime and has conditions based on some unknown other functions. if else stuff

def _encode_datetime(dttime):
    if dttime.tzinfo and dttime.tzinfo.utcoffset(dttime) is not None:
        utc_timestamp = calendar.timegm(dttime.utctimetuple())
    else:
        utc_timestamp = time.mktime(dttime.timetuple())

    return int(utc_timestamp)

# this makes a function called _api_encode which calls the argument 'data' has some for conditions and stuff
def _api_encode(data):
    #for condition referring to variables key and value in the argument with the funciton 'iteritems()' called
    for key, value in data.iteritems():
        #defines key using functions
        key = util.utf8(key)
        #starts an if else statement referring to value in this case
        if value is None:
            #pydoc says this is something that occurs in loops only
            continue
            # another 'if' regarding the function hasattr as it applies to argumets value and 'stripe_id' that says to yield something based on those args
        elif hasattr(value, 'stripe_id'):
            #yield has something to do with generator functions
            yield (key, value.stripe_id)
            #another elif reliant on the function isinstance and how the variable 'value' applies to those
        elif isinstance(value, list) or isinstance(value, tuple):
            # again uses the 'for' 
            for subvalue in value:
                #generator thing again
                yield ("%s[]" % (key,), util.utf8(subvalue))
                #another elif referring to function 'isinstance' reliant on value and dict args
        elif isinstance(value, dict):
            #subdict variable defined as the 'dict' arg subject to certain deets
            subdict = dict(('%s[%s]' % (key, subkey), subvalue) for
                           subkey, subvalue in value.iteritems())
            for subkey, subvalue in _api_encode(subdict):
                yield (subkey, subvalue)
        elif isinstance(value, datetime.datetime):
            yield (key, _encode_datetime(value))
        else:
            yield (key, util.utf8(value))

# creates a function called _build_api_url which takes arguments url and query
def _build_api_url(url, query):
    # names arguments for the urlsplit function when used on urlparse with url as an argument
    scheme, netloc, path, base_query, fragment = urlparse.urlsplit(url)
#start of an if statement about 'base_query' 
    if base_query:
        #sets the variable query to mean the string containing sring conversions that are pulled from the contents of base_query and query
        query = '%s&%s' % (base_query, query)
# provides the return 
    return urlparse.urlunsplit((scheme, netloc, path, query, fragment))

# I think this is a class definition that inherits from the 'object' class? APIRequestor inherits from the class "object" and then has further defs below. I think.
class APIRequestor(object):
# defines a function __init__ which is also a wrapper.... soo..... I think it gets defined differently than normal functions... idk
    def __init__(self, key=None, client=None):
        self.api_key = key

        from stripe import verify_ssl_certs

        self._client = client or http_client.new_default_http_client(
            verify_ssl_certs=verify_ssl_certs)
# decorator expression on classmethod.. might also be a wrapper for api_url function below? not fully understanding
    @classmethod
    # defines the 'api_url' function with the arguments cls and url=''
    def api_url(cls, url=''):
        #calls the library warnings with the function 'warn' which must be an internal thing in this app because it didnt come up in the pydoc
        #nah i found warn under warnings in pydoc. warn issues a warning... so cryptic
        warnings.warn(
            'The `api_url` class method of APIRequestor is '
            'deprecated and will be removed in version 2.0.'
            'If you need public access to this function, please email us '
            'at support@stripe.com.',
            #a 'base' class for warnings about deprecated features
            DeprecationWarning)
        # returns info
        return '%s%s' % (stripe.api_base, url)
# another decorator expression on classmethod. not totally getting this
    @classmethod
    #
    def _deprecated_encode(cls, stk, key, value):
        warnings.warn(
            'The encode_* class methods of APIRequestor are deprecated and '
            'will be removed in version 2.0. '
            'If you need public access to this function, please email us '
            'at support@stripe.com.',
            DeprecationWarning, stacklevel=2)
        stk.extend(_api_encode({key: value}))

    @classmethod
    def encode_dict(cls, stk, key, value):
        cls._deprecated_encode(stk, key, value)

    @classmethod
    def encode_list(cls, stk, key, value):
        cls._deprecated_encode(stk, key, value)

    @classmethod
    def encode_datetime(cls, stk, key, value):
        cls._deprecated_encode(stk, key, value)

    @classmethod
    def encode_none(cls, stk, key, value):
        cls._deprecated_encode(stk, key, value)

    @classmethod
    def encode(cls, d):
        """
        Internal: encode a string for url representation
        """
        warnings.warn(
            'The `encode` class method of APIRequestor is deprecated and '
            'will be removed in version 2.0.'
            'If you need public access to this function, please email us '
            'at support@stripe.com.',
            DeprecationWarning)
        return urllib.urlencode(list(_api_encode(d)))

    @classmethod
    def build_url(cls, url, params):
        warnings.warn(
            'The `build_url` class method of APIRequestor is deprecated and '
            'will be removed in version 2.0.'
            'If you need public access to this function, please email us '
            'at support@stripe.com.',
            DeprecationWarning)
        return _build_api_url(url, cls.encode(params))

    def request(self, method, url, params=None):
        rbody, rcode, my_api_key = self.request_raw(
            method.lower(), url, params)
        resp = self.interpret_response(rbody, rcode)
        return resp, my_api_key

    def handle_api_error(self, rbody, rcode, resp):
        try:
            err = resp['error']
        except (KeyError, TypeError):
            raise error.APIError(
                "Invalid response object from API: %r (HTTP response code "
                "was %d)" % (rbody, rcode),
                rbody, rcode, resp)

        if rcode in [400, 404]:
            raise error.InvalidRequestError(
                err.get('message'), err.get('param'), rbody, rcode, resp)
        elif rcode == 401:
            raise error.AuthenticationError(
                err.get('message'), rbody, rcode, resp)
        elif rcode == 402:
            raise error.CardError(err.get('message'), err.get('param'),
                                  err.get('code'), rbody, rcode, resp)
        else:
            raise error.APIError(err.get('message'), rbody, rcode, resp)

    def request_raw(self, method, url, params=None):
        """
        Mechanism for issuing an API call
        """
        from stripe import api_version

        if self.api_key:
            my_api_key = self.api_key
        else:
            from stripe import api_key
            my_api_key = api_key

        if my_api_key is None:
            raise error.AuthenticationError(
                'No API key provided. (HINT: set your API key using '
                '"stripe.api_key = <API-KEY>"). You can generate API keys '
                'from the Stripe web interface.  See https://stripe.com/api '
                'for details, or email support@stripe.com if you have any '
                'questions.')

        abs_url = '%s%s' % (stripe.api_base, url)

        encoded_params = urllib.urlencode(list(_api_encode(params or {})))

        if method == 'get' or method == 'delete':
            if params:
                abs_url = _build_api_url(abs_url, encoded_params)
            post_data = None
        elif method == 'post':
            post_data = encoded_params
        else:
            raise error.APIConnectionError(
                'Unrecognized HTTP method %r.  This may indicate a bug in the '
                'Stripe bindings.  Please contact support@stripe.com for '
                'assistance.' % (method,))
# in rails we called these hashes.looks like this is affecting the variable ua
        ua = {
            'bindings_version': version.VERSION,
            'lang': 'python',
            'publisher': 'stripe',
            'httplib': self._client.name,
        }
        for attr, func in [['lang_version', platform.python_version],
                           ['platform', platform.platform],
                           ['uname', lambda: ' '.join(platform.uname())]]:
            try:
                val = func()
            except Exception, e:
                val = "!! %s" % (e,)
            ua[attr] = val

        headers = {
            'X-Stripe-Client-User-Agent': util.json.dumps(ua),
            'User-Agent': 'Stripe/v1 PythonBindings/%s' % (version.VERSION,),
            'Authorization': 'Bearer %s' % (my_api_key,)
        }

        if method == 'post':
            headers['Content-Type'] = 'application/x-www-form-urlencoded'

        if api_version is not None:
            headers['Stripe-Version'] = api_version

        rbody, rcode = self._client.request(
            method, abs_url, headers, post_data)

        util.logger.info(
            'API request to %s returned (response code, response body) of '
            '(%d, %r)',
            abs_url, rcode, rbody)
        return rbody, rcode, my_api_key

    def interpret_response(self, rbody, rcode):
        try:
            if hasattr(rbody, 'decode'):
                rbody = rbody.decode('utf-8')
            resp = util.json.loads(rbody)
        except Exception:
            raise error.APIError(
                "Invalid response body from API: %s "
                "(HTTP response code was %d)" % (rbody, rcode),
                rbody, rcode)
        if not (200 <= rcode < 300):
            self.handle_api_error(rbody, rcode, resp)
        return resp

    # Deprecated request handling.  Will all be removed in 2.0
    def _deprecated_request(self, impl, method, url, headers, params):
        warnings.warn(
            'The *_request functions of APIRequestor are deprecated and '
            'will be removed in version 2.0. Please use the client classes '
            ' in `stripe.http_client` instead',
            DeprecationWarning, stacklevel=2)

        method = method.lower()

        if method == 'get' or method == 'delete':
            if params:
                url = self.build_url(url, params)
            post_data = None
        elif method == 'post':
            post_data = self.encode(params)
        else:
            raise error.APIConnectionError(
                'Unrecognized HTTP method %r.  This may indicate a bug in the '
                'Stripe bindings.  Please contact support@stripe.com for '
                'assistance.' % (method,))

        client = impl(verify_ssl_certs=self._client._verify_ssl_certs)
        return client.request(method, url, headers, post_data)

    def _deprecated_handle_error(self, impl, *args):
        warnings.warn(
            'The handle_*_error functions of APIRequestor are deprecated and '
            'will be removed in version 2.0. Please use the client classes '
            ' in `stripe.http_client` instead',
            DeprecationWarning, stacklevel=2)

        client = impl(verify_ssl_certs=self._client._verify_ssl_certs)
        return client._handle_request_error(*args)

    def requests_request(self, meth, abs_url, headers, params):
        from stripe.http_client import RequestsClient
        return self._deprecated_request(RequestsClient, meth, abs_url,
                                        headers, params)

    def handle_requests_error(self, err):
        from stripe.http_client import RequestsClient
        return self._deprecated_handle_error(RequestsClient, err)

    def pycurl_request(self, meth, abs_url, headers, params):
        from stripe.http_client import PycurlClient
        return self._deprecated_request(PycurlClient, meth, abs_url,
                                        headers, params)

    def handle_pycurl_error(self, err):
        from stripe.http_client import PycurlClient
        return self._deprecated_handle_error(PycurlClient, err)

    def urlfetch_request(self, meth, abs_url, headers, params):
        from stripe.http_client import UrlFetchClient
        return self._deprecated_request(UrlFetchClient, meth, abs_url,
                                        headers, params)

    def handle_urlfetch_error(self, err, abs_url):
        from stripe.http_client import UrlFetchClient
        return self._deprecated_handle_error(UrlFetchClient, err, abs_url)

    def urllib2_request(self, meth, abs_url, headers, params):
        from stripe.http_client import Urllib2Client
        return self._deprecated_request(Urllib2Client, meth, abs_url,
                                        headers, params)

    def handle_urllib2_error(self, err, abs_url):
        from stripe.http_client import Urllib2Client
        return self._deprecated_handle_error(Urllib2Client, err)