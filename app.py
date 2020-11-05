from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
import tag_reader


app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.


@app.route('/')
def home():
    return render_template('index.html')

#
@app.route('/check', methods=['POST'])
def check_url():
    url_receive = request.form['url_give']
    url_result = tag_reader.check_url(url_receive)
    # 3. mongoDB에 데이터 넣기
    # doc = {
    #     'url' : url_receive , 'comment' : comment_receive, 'image' : image , 'title' : title , 'desc' : desc
    # }
    # db.articles.insert_one(doc)
    #

    return jsonify({'result': 'success', 'msg' : url_receive + '태그 확인 되었습니다','data': url_result})
#
#
# @app.route('/memo', methods=['GET'])
# def read_articles():
#     # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기(Read)
#     articles = list(db.articles.find({},{'_id':False}))
#     print(articles)
#     # 2. articles라는 키 값으로 articles 정보 보내주기
#     return jsonify({'result': 'success', 'data': articles})
#

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)