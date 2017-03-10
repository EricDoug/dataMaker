# -*- coding:utf-8 -*-
__author__ = 'EricDoug'
import MySQLdb

from DBUtils.PooledDB import PooledDB

class MySQLHelper:
    """
    MySQL
    """
    def __init__(self, info):
        self.host = info["host"]
        self.port = info["port"]
        self.db = info["db"]
        self.user = info["user"]
        self.passwd = info["passwd"]
        self.connect_timeout = 30
        self.use_unicode = True
        self.charset = "utf8"

    def connection(self):
        # Establish a connection
        return MySQLdb.connect(host=self.host, port=self.port, db=self.db,
                               user=self.user, passwd=self.passwd,
                               connect_timeout=self.connect_timeout,
                               use_unicode=self.use_unicode,
                               charset=self.charset)

    def execute(self, sql):
        """
        执行
        :param sql:
        :return:
        """
        conn = None
        cur = None
        try:
            conn = self.connection()
            cur = conn.cursor()
        except MySQLdb.Error, e:
            if e.args[0] in (2006,    # MySQL server has gone away
                             2013):   # Lost connection to MySQL server during query
                conn = self.connection()
                cur = conn.cursor()
            else:
                raise e
        try:
            cur.execute(sql)
            conn.commit()
            return True
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    def query(self, sql):
        """
        查询
        :param sql:
        :return:
        """
        conn = None
        cur = None
        try:
            conn = self.connection()
            cur = conn.cursor()
        except MySQLdb.Error, e:
                conn = self.connection()
                cur = conn.cursor()
        try:
            cur.execute(sql)
            return cur.fetchall()
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    def find_one(self, sql):
        """
        查询一条记录
        :param sql:
        :return:
        """
        conn = None
        cur = None
        try:
            conn = self.connection()
            cur = conn.cursor()
        except MySQLdb.Error, e:
            conn = self.connection()
            cur = conn.cursor()

        try:
            cur.execute(sql)
            return cur.fetchone()
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

