from flask import request, render_template, Blueprint
from MushroomClassification.models import system_model

sy_bp = Blueprint('system', __name__, url_prefix='/system')
sy_service = system_model.Service()


# 입력 폼
@sy_bp.route('/systemForm')
def systemForm():
    return render_template('systemForm.html')


# 분류군정보 목록 검색
@sy_bp.route('/searchRequest', methods=['POST'])
def searchRequest():
    # 검색어 구분 (1 : 분류군국명, 2 : 분류군명)
    st = request.form['st']
    # 검색어
    sw = request.form['sw']
    # 한 페이지 결과 수
    numOfRows = request.form['numOfRows']
    # 페이지 번호
    pageNo = request.form['pageNo']

    List = sy_service.searchRequest(st, sw, numOfRows, pageNo)
    return render_template('systemRequest.html', List=List)


# 분류군정보 상세정보 조회
@sy_bp.route('/infoRequest', methods=['POST'])
def infoRequest():
    # 분류군
    q1 = request.form['q1']
    List = sy_service.infoRequest(q1)
    return render_template('systemInfoRequest.html', List=List)