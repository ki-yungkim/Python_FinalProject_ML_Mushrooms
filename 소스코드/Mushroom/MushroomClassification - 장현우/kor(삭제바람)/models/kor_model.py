import requests
from bs4 import BeautifulSoup


class Kor:
    def __init__(self, fngsGnrlNm=None, fngsGnrlNmNo=None, fngsScnmId=None):
        # 국명
        self.fngsGnrlNm = fngsGnrlNm
        # 국명번호
        self.fngsGnrlNmNo = fngsGnrlNmNo
        # 학명ID
        self.fngsScnmId = fngsScnmId

class Service:
    def __init__(self):
        self.base_url = 'http://apis.data.go.kr/1400119/KffniService1'
        self.api_key = 'MT2zKlHRiE1kVrI58aEpEc6Njl0gBMGIHyj6IuaQVhc4E574ANwfCZ55eOYGjaRaI4P5lFZhcXqBBQkXSaIkVg%3D%3D'

    # 국명정보 목록 검색
    def korsearchRequest(self, st, sw, numOfRows, pageNo):
        url = self.base_url + '/korSearch?ServiceKey=' + self.api_key + '&st='+ st + '&sw=' + sw + '&numOfRows=' + numOfRows + '&pageNo=' + pageNo
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        code = root.find('resultCode').text
        resultMsg = root.find('resultMsg').text
        results = []

        if code == '00':
            items = root.select('item')
            for item in items:
                # 국명
                fngsGnrlNm = item.find('fngsGnrlNm').text
                # 국명번호 -> q1
                fngsGnrlNmNo = item.find('fngsGnrlNmNo').text
                # 학명ID -> q2
                fngsScnmId = item.find('fngsScnmId').text

                results.append([fngsGnrlNm, fngsGnrlNmNo, fngsScnmId])

            return results

        else:
            print('오류발생코드: ', code)
            print('오류 메시지: ', resultMsg)

    # 국명 상세정보 조회
    def korinfoRequest(self, q1, q2):
        url = self.base_url + '/korInfo?ServiceKey=' + self.api_key + '&q1='+ q1 + '&q2=' + q2
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        code = root.find('resultCode').text
        resultMsg = root.find('resultMsg').text
        results = []

        if code == '00':
            items = root.select('item')
            for item in items:
                # 국명
                fngsGnrlNm = item.find('fngsGnrlNm').text
                # 국명번호 -> q1
                fngsGnrlNmNo = item.find('fngsGnrlNmNo').text
                # 학명 -> q2
                fngsScnm = item.find('fngsScnm').text
                # 학명ID
                fngsScnmId = item.find('fngsScnmId').text
                # 저작권설명
                cprtCtnt = item.find('cprtCtnt').text

                results.append([fngsGnrlNm, fngsGnrlNmNo, fngsScnm, fngsScnmId, cprtCtnt])

            return results

        else:
            print('오류발생코드: ', code)
            print('오류 메시지: ', resultMsg)