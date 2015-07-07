# -*- coding:utf8 -*-
import os,sys
sys.path.append('..')
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ss_panel_django.settings")

from utils import strutils

class UsersService():
    
    @staticmethod
    def regParamCheck(username,email,userpwd,reuserpwd):

        if strutils.StrUtils.isNull(username) or strutils.StrUtils.isNull(email) or strutils.StrUtils.isNull(userpwd) or strutils.StrUtils.isNull(reuserpwd):
            return False,"必填项不能为空"
        if not (strutils.StrUtils.isRightLen(username,30,8) and strutils.StrUtils.isRightLen(email,30,8) and strutils.StrUtils.isRightLen(userpwd,30,8)):
            return False,"必填项过短或者过长"#
        if not strutils.StrUtils.isEmail(email):
            return False,"邮箱格式有误"
        if userpwd != reuserpwd:
            return False,"两次输入的密码不相同"
        return True,"success"


if __name__ == '__main__':
    print UsersService.regParamCheck("dsfsdffds","ducggg@foxmail.com","12322121","12332121")
