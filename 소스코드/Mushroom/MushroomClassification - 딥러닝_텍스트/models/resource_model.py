import requests
import random
from bs4 import BeautifulSoup


class Resource:
    def __init__(self, imgUrl=None, fngsGnrlNm=None, fngsScnm=None, fngsPilbkNo=None, cont12=None):
        # 이미지URL
        self.imgUrl = imgUrl
        # 국명
        self.fngsGnrlNm = fngsGnrlNm
        # 학명
        self.fngsScnm = fngsScnm
        # 도감번호
        self.fngsPilbkNo = fngsPilbkNo
        # 식용여부
        self.cont12 = cont12


class Service:
    def __init__(self):
        self.base_url = 'http://openapi.nature.go.kr/openapi/service/rest/FungiService'
        self.api_key = '%2B7ENsmTJVHqwerwPZHnG8GPPLGXJ%2Bim42X9aFmr08YiAZPAUHql4rn9Yvrcpi3MAmOl2FONgiJbMyeOXDzrqEw%3D%3D'

    # 버섯도감 목록 검색
    def searchRequest(self, st, sw, numOfRows, pageNo):
        url = self.base_url + '/fngsIlstrSearch?ServiceKey=' + self.api_key + '&st=' + st + '&sw=' + sw + '&numOfRows=' + numOfRows + '&pageNo=' + pageNo
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        code = root.find('resultCode').text
        resultMsg = root.find('resultMsg').text
        results = []

        if code == '00':
            items = root.select('item')
            for item in items:
                # 이미지URL
                imgUrl = item.find('imgUrl').text
                # 국명
                fngsGnrlNm = item.find('fngsGnrlNm').text
                # 학명
                fngsScnm = item.find('fngsScnm').text
                # 도감번호
                fngsPilbkNo = item.find('fngsPilbkNo').text

                # 맹독여부 확인 위해 버섯도감 상세정보 조회 실시
                url = self.base_url + '/fngsIlstrInfo?ServiceKey=' + self.api_key + '&q1=' + fngsPilbkNo
                html = requests.get(url).text
                root = BeautifulSoup(html, 'lxml-xml')
                code = root.find('resultCode').text

                if code == '00':
                    items = root.select('item')
                    for item in items:
                        # 식용여부
                        cont12 = item.find('cont12').text
                        if cont12 == ' ':
                            cont12 = '불명'

                results.append([imgUrl, fngsGnrlNm, fngsScnm, fngsPilbkNo, cont12])

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
                # 과국명
                familyKorNm = item.find('familyKorNm').text
                # 과명
                familyNm = item.find('familyNm').text
                # 속국명
                genusKorNm = item.find('genusKorNm').text
                # 속명
                genusNm = item.find('genusNm').text
                # 국명
                fngsGnrlNm = item.find('fngsGnrlNm').text
                # 전체학명
                fngsScnm = item.find('fngsScnm').text
                # 독성여부
                cont12 = item.find('cont12').text
                if cont12 == ' ':
                    cont12 = '불명'
                # 발생 계절
                occrrSsnNm = item.find('occrrSsnNm').text
                if occrrSsnNm == ' ':
                    occrrSsnNm = '사계절'
                # 발생 형태 설명
                occrrFomDscrt = item.find('occrrFomDscrt').text
                if occrrFomDscrt == ' ':
                    occrrFomDscrt = '불명'
                # 발생장소
                cont21 = item.find('cont21').text
                if cont21 == ' ':
                    cont21 = '불명'

                results.append([familyKorNm, familyNm, genusKorNm, genusNm, fngsGnrlNm, fngsScnm, cont12, occrrSsnNm, occrrFomDscrt, cont21])
            return results

        else:
            print('오류발생코드: ', code)
            print('오류 메시지: ', resultMsg)

    # 이미지퀴즈 오답페이지에 들어가는 버섯명언
    def advice(self):
        advice = [
            "버섯은 경고 표지를 달고 오지 않는다. 여러분은 입에 넣기 전에 손에 쥐고 있는 것이 무엇인지 알고 있어야 한다.",
            "자문을 청하는 사람은 버섯에 중독되지 않는 사람이다.(남태평양 독립국 토가 속담)",
            "의심나면 그대로 내버려두라!(If in doubt, leave it!)",
            "의심나면 그냥 버려라!(If in doubt, discard it!)",
            "버섯은 날로(生으로) 먹는 것이 아니고, 알코올음료와 함께 먹는 것도 아니며, 많이 먹는 것이 아니다.",
            "식용버섯을 버리는 것이 독버섯을 먹고 중독되는 것보다 백번 낫다.",
            "기억하라: 야생버섯 식용은 (클라이밍이나 스노우보드와 같은) 위험한 스포츠(extreme sport)도 아니고,"
            " 시식해 본 가장 긴 버섯목록 만들기 경쟁도 아니다.(Greg A. Marley)",
            "모든 버섯은 먹을 수 있지만, 어떤 버섯들은 오직 단 한번만 먹을 수 있다.",
            "늙은 버섯채취자와 용감한 버섯 채취자는 많지만 늙고 용감한 버섯 채취자는 없다"
        ]
        msg = random.choice(advice)
        return msg

    # 버섯요리
    def mushroomDish(self):
        url = 'http://apis.data.go.kr/1390804/NihhsRdaLifeInfo/selectLifeList?serviceKey=z87XiFqBjizhP7gRBLRttGzJYgKrESmLrKQNmb1aVULKjUTS9f6TBr2rppZBMSEXbq1ovC5bUdGj2N%2FYD6pKPg%3D%3D&iSubCode=A05&searchType=2&searchWord=버섯&pageNo=1&numOfRows=20'
        html = requests.get(url).text
        root = BeautifulSoup(html, 'lxml-xml')
        code = root.find('resultCode').text
        resultMsg = root.find('resultMsg').text
        results = []

        if code == '1':
            items = root.select('result')
            for item in items:
                # 이미지주소
                fileImageUrl = item.find('fileImageUrl').text
                # 제목
                title = item.find('title').text
                # 내용
                content = item.find('content').text
                content = content.replace('재료손질', '재료준비')
                ingredient = content.split('재료준비')
                ingredients = ingredient[0].replace('재료 및 분량','')
                ingredients = ingredients.replace('소스', ',')
                ingredients = ingredients.replace('양념장', ',')
                ingredients = ingredients.replace('곁들임', ',')
                ingredients = ingredients.replace('튀김반죽', ',')
                recipe = ingredient[1].replace('만드는 법', '')
                recipe = recipe.split('다.')
                del recipe[-1]

                results.append([fileImageUrl, title, ingredients, recipe])
            return results

        else:
            print('오류발생코드: ', code)
            print('오류 메시지: ', resultMsg)