import hashlib

class EncrptyUtils(object):

    @staticmethod
    def getMd5(ustr):
        md5=hashlib.md5(ustr.encode('utf-8')).hexdigest()
        return  md5



if __name__=='__main__':
    print EncrptyUtils.getMd5('12345678')