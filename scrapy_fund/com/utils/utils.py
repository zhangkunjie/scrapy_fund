import pymysql
#清空数据库
from com.constant import constant


def truncate_table(table_name):
    conn = pymysql.connect(host=constant.HOST, user=constant.USER, passwd=constant.PASSWORD, db=constant.DB,
                           port=constant.PORT, charset=constant.CHARSET)
    truncateSQL = "truncate " + table_name;
    cur = conn.cursor()
    cur.execute(truncateSQL)
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源
