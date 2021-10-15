import requests
from bs4 import BeautifulSoup

class Resource:
    def __init__(self, familyKorNm=None,familyNm=None, fngsGnrlNm=None,
                 fngsPilbkNo=None, genusKorNm=None, genusNm=None):
        # 과 한글 이름
        self.familyKorNm = familyKorNm
        # 과 이름
        self.familyNm = familyNm
        # 이름
        self.fngsGnrlNm = fngsGnrlNm
        # 도감번호
        self.fngsPilbkNo = fngsPilbkNo
        # 속 한글 이름
        self.genusKorNm = genusKorNm
        # 속 이름
        self.genusNm = genusNm


class Service:
    def __init__(self):
        self.base_url = 'http://openapi.nature.go.kr/openapi/service/rest/FungiService'
        self.api_key = '서비스 키 입력해주세요'

    # 버섯도감 목록 검색
    def searchRequest(self, st, sw, numOfRows, pageNo):
        url = self.base_url + '/fngsIlstrSearch?ServiceKey=' + self.api_key + '&st='+ st + '&sw=' + sw + '&numOfRows=' + numOfRows + '&pageNo=' + pageNo
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        code = root.find('resultCode').text
        resultMsg = root.find('resultMsg').text
        results = []

        if code == '00':
            items = root.select('item')
            for item in items:
                familyKorNm = item.find('familyKorNm').text
                familyNm = item.find('familyNm').text
                fngsGnrlNm = item.find('fngsGnrlNm').text
                fngsPilbkNo = item.find('fngsPilbkNo').text
                genusKorNm = item.find('genusKorNm').text
                genusNm = item.find('genusNm').text

                results.append([familyKorNm, familyNm, fngsGnrlNm,
                                fngsPilbkNo, genusKorNm, genusNm])

            return results

        else:
            print('오류발생코드: ', code)
            print('오류 메시지: ', resultMsg)

    # 버섯도감 상세정보 조회
    def infoRequest(self, q1):
        url = self.base_url + '/fngsIlstrInfo?ServiceKey=' + self.api_key + '&q1='+ q1
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        code = root.find('resultCode').text
        resultMsg = root.find('resultMsg').text
        results = []

        if code == '00':
            items = root.select('item')
            for item in items:
                # 자실체 크기 설명
                crpphMgntdDscrt = item.find('crpphMgntdDscrt').text
                # 발생 형태 설명
                occrrFomDscrt = item.find('occrrFomDscrt').text
                # 발생 계절명
                occrrSsnNm = item.find('occrrSsnNm').text
                # 식용여부
                cont12 = item.find('cont12').text
                # 발생장소
                cont21 = item.find('cont21').text

                results.append([crpphMgntdDscrt, occrrFomDscrt, occrrSsnNm,
                                cont12, cont21])

            return results

        else:
            print('오류발생코드: ', code)
            print('오류 메시지: ', resultMsg)


