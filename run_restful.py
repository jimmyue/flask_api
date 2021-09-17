#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Created on 2021年9月16日
@author: yuejing
'''
import pymysql
from flask import Flask
from flask_restful import reqparse, Api, Resource

app = Flask(__name__)
api = Api(app)

def get_dealer(dealer_code):
    conn = pymysql.connect(host='DB_IP',port=3306,user='XXX',passwd='XXX',db='XXX',use_unicode=True, charset="utf8")
    cur = conn.cursor()
    sql = "select DEALER_CODE,DEALER_NAME from tb_dealer_info where DEALER_CODE='%s'" % dealer_code
    cur.execute(sql)
    data = cur.fetchone()
    cur.close()
    conn.close()
    if data==None:
        result = {'status':204,'message':'经销店不存在','data':{'DEALER_CODE':'null','DEALER_NAME':'null'}}
    else:
        result = {'status':200,'message':'获取成功','data':{'DEALER_CODE':data[0],'DEALER_NAME':data[1]}}
    return result

class dealer(Resource):
	def __init__(self):
		self.parser = reqparse.RequestParser()
		self.parser.add_argument('dealer_code', type=str, required=True, help='dealer_code is a required field')
		self.args = self.parser.parse_args()

	def get(self):
		get_data=get_dealer(self.args.dealer_code)
		return get_data

	def post(self):
		post_data=get_dealer(self.args.dealer_code)
		return post_data

api.add_resource(dealer, '/dealer')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
