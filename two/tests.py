from django.test import TestCase
import pymysql 
# Create your tests here.
class mysql(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306,
                           user='yemaolin', password='123456',
                           db='djtest', charset='utf8')

        self.cursor = self.conn.cursor()

    def search(self, uname, uid):
      #  search_sql = "select * from two_student where s_name = '%s' and id =' %s'" %  (uname,id)
        
        #防止sql注入
        sql = "select * from two_student where s_name = %s and id = %s"
        values = [uname, uid]
        self.cursor.execute(sql,values)

        result = self.cursor.fetchall()
        
        return result

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
