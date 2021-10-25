from flask import request, render_template, Blueprint
from btnc.models import btnc_model

bt_bp = Blueprint('btnc', __name__, url_prefix='/btnc')
bt_service = btnc_model.Service()


# 입력 폼
@bt_bp.route('/btncForm')
def btncForm():
    return render_template('btncForm.html')


# 국가표준버섯 학명목록 검색
@bt_bp.route('/btncsearchRequest', methods=['POST'])
def btncsearchRequest():
    # 검색어 구분 (1 : 국명, 2 : 학명)
    st = request.form['st']
    # 검색어
    sw = request.form['sw']
    # 한 페이지 결과 수
    numOfRows = request.form['numOfRows']
    # 페이지 번호
    pageNo = request.form['pageNo']

    List = bt_service.btncsearchRequest(st, sw, numOfRows, pageNo)
    return render_template('btncRequest.html', List=List)


# 국가표준버섯 학명 상세정보 조회
@bt_bp.route('/btncinfoRequest', methods=['POST'])
def btncinfoRequest():
    # 국가표준버섯 학명
    q1 = request.form['q1']
    List = bt_service.btncinfoRequest(q1)
    return render_template('btncinfoRequest.html', List=List)