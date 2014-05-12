qputpolicy
==========
用于构造七牛的上传策略(PutPolicy)以及token签发  

使用前需了解：  
[七牛云存储的安全机制](http://developer.qiniu.com/docs/v6/api/reference/security/)

范例1

    #coding=utf-8
    from qputpolicy import PutPolicy
    from qsign import Mac

    accesskey = "a"
    secretkey = "s"

    bucket = "b"

    scope = bucket
    policy = PutPolicy(scope)

    policy_data = policy.data()

    mac = Mac(accesskey, secretkey)
    uptoken = mac.sign_with_data(policy_data)
    
    
范例2

    #coding=utf-8
    from qputpolicy import PutPolicy
    from qsign import Mac

    accesskey = "a"
    secretkey = "s"

    bucket = "b"
    key = "k"

    scope = "%s:%s" % (bucket, key)
    policy = PutPolicy(scope)
    policy.callbackUrl = "http://abc.com/callback"
    policy.callbackBody = "key=$(key)&hash=$(etag)"

    policy_data = policy.data()

    mac = Mac(accesskey, secretkey)
    uptoken = mac.sign_with_data(policy_data)
