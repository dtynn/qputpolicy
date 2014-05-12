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
    # PutPolicy参数使用
    # policy.item = value
    # 的形式赋值。注意大小写。新增支持的参数不需要修改代码也可以使用。

    policy_data = policy.data()

    mac = Mac(accesskey, secretkey)
    uptoken = mac.sign_with_data(policy_data)
