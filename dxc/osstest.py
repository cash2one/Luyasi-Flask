import oss
from oss.oss_api import *
oss=OssAPI('oss.aliyuncs.com','SB92Xozt8KamUnCw','N5ytDUqkSMKrPcDLmypaVElXBwKI3k')
#res = oss.list_all_my_buckets()
#print res.read()
with open('todos', 'rb') as f:
	res = oss.put_object_from_fp('hz-kinorsi-bucket', 'test-object', f)
print res.status
print res.read()