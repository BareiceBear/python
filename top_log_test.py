"""
连接至postgresql远程数据库，并向其填入日志数据（测试用）
"""

import psycopg2 as pgsql
import time
import datetime
import random
import os
import io

try:
    conn = pgsql.connect(dbname="log", user="postgres", password="300607", host="10.110.40.79", port="5432")
    pg = conn.cursor()
except pgsql.Error as e:
    print(e.pgerror)
    os._exit(1)

codes = []
with open('logmap.txt', 'r', encoding="utf-8") as fd:
    fd.readline()
    for line in fd:
        log = line.split('\t')
        codes.append(log[0].strip())

for i in range(0, 400):
    idx = random.randrange(0, len(codes))
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pg.execute("INSERT INTO log (code, date, curuser) VALUES ('%s', '%s', 'Admin');" % (codes[idx], now))
    time.sleep(1)

conn.commit()

pg.close()
conn.close()
