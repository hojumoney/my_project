import requests
from bs4 import BeautifulSoup


def check_url(url_receive):
    # 1. 클라이언트로부터 데이터를 받기
    # 2. meta tag를 스크래핑하기
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    result = {}

    fbkakao_image = soup.select_one('meta[property="og:image"]')
    if fbkakao_image is not None:
        result['fbkakao_image'] = fbkakao_image['content']
        print('fbkakao_image : ', fbkakao_image['content'])
    else:
        result['fbkakao_image'] = None
        print('no fbkakao_image')

    fbkakao_title = soup.select_one('meta[property="og:title"]')
    if fbkakao_title is not None:
        result['fbkakao_title'] = fbkakao_title['content']
        print('fbkakao_title : ', fbkakao_title['content'])
    else:
        result['fbkakao_title'] = None
        print('no fbkakao_title')

    fbkakao_desc = soup.select_one('meta[property="og:description"]')
    if fbkakao_desc is not None:
        result['fbkakao_desc'] = fbkakao_desc['content']
        print('fbkakao_desc : ', fbkakao_desc['content'])
    else:
        result['fbkakao_desc'] = None
        print('no fbkakao_desc')

    fbkakao_sitename = soup.select_one('meta[property="og:sitename"]')
    if fbkakao_sitename is not None:
        result['fbkakao_sitename'] = fbkakao_sitename['content']
        print('fbkakao_sitename : ', fbkakao_sitename['content'])
    else:
        result['fbkakao_sitename'] = None
        print('no fbkakao_sitename')

    fbkakao_url = soup.select_one('meta[property="og:url"]')
    if fbkakao_url is not None:
        result['fbkakao_url'] = fbkakao_url['content']
        print('fbkakao_url : ', fbkakao_url['content'])
    else:
        result['fbkakao_url'] = None
        print('no fbkakao_url')

    twitter_image = soup.select_one('meta[property="twitter:image"]')
    if twitter_image is not None:
        result['twitter_image'] = twitter_image['content']
        print('twitter_image : ', twitter_image['content'])
    else:
        result['twitter_image'] = None
        print('no twitter_image')

    twitter_title = soup.select_one('meta[property="twitter:title"]')
    if twitter_title is not None:
        result['twitter_title'] = twitter_title['content']
        print('twitter_title : ', twitter_title['content'])
    else:
        result['twitter_title'] = None
        print('no twitter_title')

    twitter_desc = soup.select_one('meta[property="twitter:description"]')
    if twitter_desc is not None:
        result['twitter_desc'] = twitter_desc['content']
        print('twitter_desc : ', twitter_desc['content'])
    else:
        result['twitter_desc'] = None
        print('no twitter_desc')

    twitter_sitename = soup.select_one('meta[property="twitter:sitename"]')
    if twitter_sitename is not None:
        result['twitter_sitename'] = twitter_sitename['content']
        print('twitter_sitename : ', twitter_sitename['content'])
    else:
        result['twitter_sitename'] = None
        print('no twitter_sitename')

    #print(fbkakao_desc, fbkakao_image, fbkakao_title, fbkakao_sitename, fbkakao_url, twitter_desc, twitter_image, twitter_title, twitter_sitename)
    return result



# result = check_url('https://www.naver.com')
# print(result)