# -*- coding:utf8-*-
import re


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


if __name__== '__main__':
    print StrUtils.isRightLen("ducg@foxmail.comfdsfsdfsfdss",19,8)
    #test = "123321"
    #test1 = "123321"
    #print test!=test1
    #print len(test)
    #print 'fdsfsd'


