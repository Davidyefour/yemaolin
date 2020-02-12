from django.db import models
import pymysql
class Student(models.Model):
    s_name = models.CharField(max_length=16)
    s_age = models.IntegerField(default=18)
    s_id = models.CharField(max_length=16)

class lib(models.Model):
    name = models.CharField(max_length=16)
    age = models.IntegerField(default=18)
    bid = models.CharField(max_length=16)
# Create your models here.



class opmysql(object):
    def __init__(self):
        self.conn = None
        self.cur = None
        try:
            self.conn = pymysql.connect(host='127.0.0.1', port=3306,
                            user='yemaolin', password='123456',
                            db='djtest', charset='utf8')
            self.cur = self.conn.cursor()
        except Exception:
            print(Exception)
        
    def getALL(self):
        sql = "select * from two_student"
        
        #执行sql语句
        self.cur.execute(sql)

        #获取信息
        result = self.cur.fetchall()

        return result