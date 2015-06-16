# -*- coding:utf8-*-
import re


class Strutils(object):

    @staticmethod
    def isNull(ustr):
        flag = False
        if ustr == '' or ustr is None:
            flag = True
        return flag

    @staticmethod
    def isEmail(ustr):
        flag = False
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            flag = True
        return flag


