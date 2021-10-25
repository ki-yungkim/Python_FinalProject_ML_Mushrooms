import requests
from bs4 import BeautifulSoup


class Btnc:
    def __init__(self, fngsScnm=None, fngsGnrlNm=None, fngsScnmId=None):
        # 학명
        self.fngsScnm = fngsScnm
        # 국명
        self.fngsGnrlNm = fngsGnrlNm
        # 학명ID
        self.fngsScnmId = fngsScnmId

class Service:
    def __init__(self):
        self.base_url = 'http://apis.data.go.kr/1400119/KffniService1'
        self.api_key = 'MT2zKlHRiE1kVrI58aEpEc6Njl0gBMGIHyj6IuaQVhc4E574ANwfCZ55eOYGjaRaI4P5lFZhcXqBBQkXSaIkVg%3D%3D'

    # 국가표준버섯 학명목록 검색
    def btncsearchRequest(self, st, sw, numOfRows, pageNo):
        url = self.base_url + '/btncSearch?ServiceKey=' + self.api_key + '&st='+ st + '&sw=' + sw + '&numOfRows=' + numOfRows + '&pageNo=' + pageNo
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        code = root.find('resultCode').text
        resultMsg = root.find('resultMsg').text
        results = []

        if code == '00':
            items = root.select('item')
            for item in items:
                # 정이명구분
                biogyNmTpcd = item.find('biogyNmTpcd').text
                # 학명
                fngsScnm = item.find('fngsScnm').text
                # 국명
                fngsGnrlNm = item.find('fngsGnrlNm').text
                # 학명ID -> q1
                fngsScnmId = item.find('fngsScnmId').text

                results.append([biogyNmTpcd, fngsScnm, fngsGnrlNm, fngsScnmId])

            return results

        else:
            print('오류발생코드: ', code)
            print('오류 메시지: ', resultMsg)

    # 국가표준버섯 학명 상세정보 조회
    def btncinfoRequest(self, q1):
        url = self.base_url + '/btncInfo?ServiceKey=' + self.api_key + '&q1='+ q1
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        code = root.find('resultCode').text
        resultMsg = root.find('resultMsg').text
        results = []

        if code == '00':
            items = root.select('item')
            for item in items:
                # 명명자명
                fngsAthrNm = item.find('fngsAthrNm').text
                # 속명
                fngsGenusNm = item.find('fngsGenusNm').text
                # 종소명
                fngsTtnm = item.find('fngsTtnm').text
                # 국명
                korname = item.find('korname').text
                # 영문명
                engname = item.find('engname').text
                # 학명
                fngsScnm = item.find('fngsScnm').text
                # 학명ID -> q1
                fngsScnmId = item.find('fngsScnmId').text
                # 저작권설명
                cprtCtnt = item.find('cprtCtnt').text

                results.append([fngsAthrNm, fngsGenusNm, fngsTtnm, korname, engname, fngsScnm, fngsScnmId, cprtCtnt])

            return results

        else:
            print('오류발생코드: ', code)
            print('오류 메시지: ', resultMsg)
