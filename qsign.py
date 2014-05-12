#coding=utf-8
import hmac
from hashlib import sha1
from base64 import urlsafe_b64encode


class Mac(object):
    def __init__(self, access, secret):
        self.access, self.secret = access, secret

    def __sign(self, data):
        hashed = hmac.new(self.secret, data, sha1)
        return urlsafe_b64encode(hashed.digest())

    def sign(self, data):
        # for Download Token/Access Token
        # http://developer.qiniu.com/docs/v6/api/reference/security/download-token.html
        # http://developer.qiniu.com/docs/v6/api/reference/security/access-token.html
        return '%s:%s' % (self.access, self.__sign(data))

    def sign_with_data(self, b):
        # for Up Token
        # http://developer.qiniu.com/docs/v6/api/reference/security/upload-token.html
        data = urlsafe_b64encode(b)
        return '%s:%s:%s' % (self.access, self.__sign(data), data)