import os
import urllib.request
import requests
from flask import *
from flask_cors import CORS
from bs4 import *

from models import imgClassifier_model as imgClassifier

imgClassifierService = imgClassifier.imgClassifierService()

mushroom_bp = Blueprint("mushroom", __name__, url_prefix="/mushroom")
cors = CORS()
CORS(mushroom_bp)

@mushroom_bp.route("/imgClassifier")
def imgClassifierInput():
    print("Call imgClassifier_input.html")
    listdir = os.listdir("static/uploads/imgClassifier/")

    for i in range(len(listdir)):
        print("Delete",listdir[i])
        if listdir[i] != ".DS_Store":
            os.remove("static/uploads/imgClassifier/"+listdir[i])
        else:
            continue

    return render_template("imgClassifier/imgClassifier_input.html")

@mushroom_bp.route("/imageSearch", methods=["GET", "POST"])
def imgClassifierInputAction():
    inputImage = request.files["uploadfile"]
    inputImage.save("static/uploads/imgClassifier/"+(inputImage.filename))
    print("Uploaded:", inputImage.filename)

    res = imgClassifierService.getResult(inputImage)
    print("Result:", res)
    list = searchMushInfo(res)

    return render_template("imgClassifier/imgClassifier_output.html", img=inputImage.filename, res=res, list=list)

def searchMushInfo(sw):
    sw = sw
    api_Key = 'maOhzLUdWh%2B71An2U%2F5nloeLuy%2F2dJSnnTbxJx8sw4RkZapqOELDIIEJIZps6T6XuEv3Gz1NwlHby%2BLQE2L%2F1A%3D%3D'
    url = 'http://openapi.nature.go.kr/openapi/service/rest/FungiService/fngsIlstrSearch?ServiceKey=' + api_Key
    url += '&st=2'
    url += '&sw='+sw
    url += '&numOfRows=5&PageNo=1'

    html = requests.get(url).text
    root = BeautifulSoup(html, 'lxml-xml')
    code = root.find('resultCode').text
    resultMsg = root.find("resultMsg").text
    results = []

    if code == "00":
        print("API Loading Complete!!")
        items = root.select("item")
        for item in items:
            imgUrl = item.find("imgUrl").text
            genusKorNm = item.find("genusKorNm").text
            genusNm = item.find("genusNm").text
            fngsGnrlNm = item.find("fngsGnrlNm").text

            results.append([imgUrl, genusKorNm, genusNm, fngsGnrlNm])
        return results

    else:
        print("API Loading Failed...")
        print("API Load ErrorCode: ", code)
        print("API Load Error Message: ", resultMsg)

        return None