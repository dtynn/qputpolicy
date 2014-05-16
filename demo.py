#coding=utf-8
from qputpolicy import PutPolicy
from qsign import Mac

a = "a"
s = "s"
b = "b"
k = "k"

policy = PutPolicy(b)
policy.callbackUrl = "http://abc.com"
policy.callbackBody = "key=$(key)"

mac = Mac(a, s)
print(policy.data())
token = mac.sign_with_data(policy.data())
print(token)
print(type(token))