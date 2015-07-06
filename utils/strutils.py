# -*- coding:utf8 -*-
import re
import random
import uuid,base64

class StrUtils(object):

    @staticmethod
    def isNull(ustr):
        flag = False
        if ustr == '' or ustr is None:
            flag = True
        return flag

    @staticmethod
    def isEmail(ustr):
        flag = False
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", ustr) != None:
            flag = True
        return flag

    @staticmethod
    def isRightLen(ustr,umaxlength,uminlength):
        flag = False
        if len(ustr)<=int(umaxlength) and len(ustr)>=int(uminlength):
            flag = True

        return flag

    @staticmethod
    def getRandomStr(unum):
        return ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890',unum))

    @staticmethod
    def getUUUID(name):
        return str(uuid.uuid5(uuid.NAMESPACE_DNS,str(name)))


if __name__== '__main__':
    name = "strengthening12312312123getUUUID"
    print base64.urlsafe_b64encode(StrUtils.getUUUID(name))
    print base64.urlsafe_b64decode(base64.urlsafe_b64encode(StrUtils.getUUUID(name)))
    #test = "123321"
    #test1 = "123321"
    #print test!=test1
    #print len(test)
    #print 'fdsfsd'


