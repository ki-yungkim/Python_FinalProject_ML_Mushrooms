import requests
from flask import render_template, request, Blueprint, flash

from models import model_mushrooms as mushroom

"""
mushroom_bp = Blueprint("mushroom", __name__, url_prefix="/mushroom")

mushroom_service = mushroom.Service()

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
"""