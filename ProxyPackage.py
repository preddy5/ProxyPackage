
import urllib2

class ProxyPackage:
    """
        This class is used for installing python packages or to use urllib or urllib2 under proxy server
    """
    def __init__(self,kind='http',name='',password='',proxy='',port=''):
        if name=='':
            auth = '%s://%s:%s' % (kind, proxy , port)
        else:
            auth = '%s://%s:%s@%s:%s' % (kind,name , password , proxy , port)
        self.handler = urllib2.ProxyHandler({kind: auth})
        self.opener = urllib2.build_opener(self.handler)

   def set_global():        
	"""sets the given proxy settings globally"""
	urllib2.install_opener(self.opener)

   def open_url(url):
	"""opens url using the given proxy settings"""
	return self.opener.open(url)  
