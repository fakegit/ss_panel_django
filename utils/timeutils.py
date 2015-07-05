# -*- coding:utf8-*-
import time


class TimeUtils(object):

    @staticmethod
    def getTimeStamp():
        return  int (time.time())


if __name__== '__main__':
    print TimeUtils.getTimeStamp()

    #test = "123321"
    #test1 = "123321"
    #print test!=test1
    #print len(test)
    #print 'fdsfsd'


