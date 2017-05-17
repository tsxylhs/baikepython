#coding:utf-8
'''
Created on 2017年3月18日

@author: lhs
'''

import urllib2


class HtmlDownloader(object):
    
    
    def download(self,url):
        if url in None:
            return None
        response=urllib2.urlopen(url)
        if response.getcode()!=200:
            return None
        return response.read()
    
    



