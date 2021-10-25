from flask import request, render_template, Blueprint
from kor.models import kor_model

kor_bp = Blueprint('kor', __name__, url_prefix='/kor')
kor_service = kor_model.Service()


# 입력 폼
@kor_bp.route('/korForm')
def korForm():
    return render_template('korForm.html')


# 국명정보 목록 검색
@kor_bp.route('/korsearchRequest', methods=['POST'])
def korsearchRequest():
    # 검색어 구분 (1 : 국명, 2 : 국명일치)
    st = request.form['st']
    # 검색어
    sw = request.form['sw']
    # 한 페이지 결과 수
    numOfRows = request.form['numOfRows']
    # 페이지 번호
    pageNo = request.form['pageNo']

    List = kor_service.korsearchRequest(st, sw, numOfRows, pageNo)
    return render_template('korRequest.html', List=List)


# 국명 상세정보 조회
@kor_bp.route('/korinfoRequest', methods=['POST'])
def korinfoRequest():
    # 국명
    q1 = request.form['q1']
    q2 = request.form['q2']
    List = kor_service.korinfoRequest(q1, q2)
    return render_template('korinfoRequest.html', List=List)