import requests
from bs4 import *

class Mushroom:
    def __init__(self, familyKorNm=None, familyNm=None, fngsGnrlNm=None, fngsPilbkNo=None, genusKorNm=None, genusNm=None):
        """
        과국명, 과명, 국명, 도감번호, 속국명, 속명
        """
        self.familyKorNm = familyKorNm
        self.familyNm = familyNm
        self.fngsGnrlNm = fngsGnrlNm
        self.fngsPilbkNo = fngsPilbkNo
        self.genusKorNm = genusKorNm
        self.genusNm = genusNm

class Service:
    def __init__(self):
        self.base_url = 'http://openapi.nature.go.kr/openapi/service/rest/FungiService'
        self.api_key = 'maOhzLUdWh%2B71An2U%2F5nloeLuy%2F2dJSnnTbxJx8sw4RkZapqOELDIIEJIZps6T6XuEv3Gz1NwlHby%2BLQE2L%2F1A%3D%3D'

    def Test01(self, st, sw, numOfRows, pageNo):
        # print("TEST01 GET:", st, sw, numOfRows, pageNo)

        url = self.base_url + '/fngsIlstrSearch?ServiceKey=' + self.api_key + '&st=' + st + '&sw=' + sw + "&numOfRows=" + numOfRows + "&PageNo=" + pageNo
        # print("TEST01 request URL", url)

        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        code = root.find('resultCode').text
        resultMsg = root.find("resultMsg").text
        results = []

        if code == "00":
            print("API Loading Complete!!")
            items = root.select("item")
            for item in items:
                familyKorNm = item.find('familyKorNm').text
                familyNm = item.find('familyNm').text
                fngsGnrlNm = item.find("fngsGnrlNm").text
                fngsPilbkNo = item.find("fngsPilbkNo").text
                genusKorNm = item.find("genusKorNm").text
                genusNm = item.find("genusNm").text

                results.append([familyKorNm, familyNm, fngsGnrlNm, fngsPilbkNo, genusKorNm, genusNm])
            return results

        else:
            print("API Loading Failed...")
            print("API Load ErrorCode: ", code)
            print("API Load Error Message: ", resultMsg)

