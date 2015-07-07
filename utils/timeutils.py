# -*- coding:utf8-*-
import time


class TimeUtils(object):

    @staticmethod
    def getTimeStamp():
        return  int (time.time())

    @staticmethod
    def getDatetimeFromTS(uts):
        
        timeArray = time.localtime(uts)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        return otherStyleTime


if __name__== '__main__':
    print TimeUtils.getDatetimeFromTS(1381419600)

    #test = "123321"
    #test1 = "123321"
    #print test!=test1
    #print len(test)
    #print 'fdsfsd'


