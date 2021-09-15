#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Created on 2021年9月14日
@author: yuejing
'''

import pymysql
import json
from flask import Flask,request
app = Flask(__name__)

@app.route('/data',methods=('GET','POST'))
def data():
	if request.method=='GET':
		searchword=request.args.get('dealer','')
		temp_data=get_dealer(searchword)
		return temp_data
	elif request.method=='POST':
		searchword=request.form.get("dealer")
		print(searchword)
		temp_data=get_dealer(searchword)
		return temp_data

def get_dealer(dealer_code):
    conn = pymysql.connect(host='DB_IP',port=3306,user='XXX',passwd='XXX',db='XXX',use_unicode=True, charset="utf8")
    cur = conn.cursor()
    sql = "select DEALER_CODE,DEALER_NAME from tb_dealer_info where DEALER_CODE='%s'" % (dealer_code)
    cur.execute(sql)
    data = cur.fetchone()
    if data==None:
    	result={'status':1,'msg2Dev':'经销店不存在!','data':'null'}
    else:
    	result = {'status':0,'msg2Dev':'ok','data':{'DEALER_CODE':data[0],'DEALER_NAME':data[1]}}
    	
    return json.dumps(result, ensure_ascii=False, indent=3)

if __name__ == '__main__':
    app.run(host='SERVICE_IP', port=5000)
