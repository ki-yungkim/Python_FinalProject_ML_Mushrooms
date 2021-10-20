import os
import urllib.request
import requests
from flask import *
from models import model_mushrooms as mushroom
from models import model_test as test

mushroom_bp = Blueprint("mushroom", __name__, url_prefix="/mushroom")

mushroom_service = mushroom.Service()
test_service = test.Test01Service()

@mushroom_bp.route("/test01")
def test01():
    return render_template("test/test01.html")

@mushroom_bp.route("/test01_result", methods=["GET"])
def test01Result():
    st = request.args.get("st")
    sw = request.args.get("sw")
    numOfRows = request.args.get("numOfRows")
    pageNo = request.args.get("pageNo")

    print("GET:", st, sw, numOfRows, pageNo)

    list = mushroom_service.Test01(st, sw, numOfRows, pageNo)

    return render_template("test/test01result.html", list=list)

@mushroom_bp.route("/test03")
def test03():
    return render_template("test/test03/test03.html")

@mushroom_bp.route("/test03search_text", methods=["GET"])
def test03input_A():
    return render_template("test/test03/test03inputText.html")

@mushroom_bp.route("/textSearch")
def test03resultText():
    return render_template("test/test03/test03result.html")

@mushroom_bp.route("/test03search_image")
def test03input_B():
    return render_template("test/test03/test03inputImage.html")

@mushroom_bp.route("/imageSearch", methods=["POST"])
def test03resultImage():
    inputImage = request.files["uploadfile"]
    inputImage.save("static/uploads/"+(inputImage.filename))
    print("Uploaded:",inputImage.filename)

    res = test_service.getResult(inputImage)
    print("Result:", res)

    return render_template("test/test03/test03result_image.html", img=inputImage.filename, res=res)