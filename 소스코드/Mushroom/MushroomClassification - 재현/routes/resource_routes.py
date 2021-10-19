import random
from flask import request, render_template, Blueprint
from MushroomClassification.models import resource_model

re_bp = Blueprint('resource', __name__, url_prefix='/resource')
re_service = resource_model.Service()


# 입력 폼
@re_bp.route('/resourceForm')
def resourceForm():
    return render_template('resourceForm.html')


# 버섯도감 목록 검색
@re_bp.route('/searchRequest', methods=['POST'])
def searchRequest():
    # 검색어 구분 (1 : 국명, 2 : 학명, 3 : 국명일치, 4 : 학명일치)
    st = request.form['st']
    # 검색어
    sw = request.form['sw']
    # 한 페이지 결과 수
    numOfRows = request.form['numOfRows']
    # 페이지 번호
    pageNo = request.form['pageNo']

    List = re_service.searchRequest(st, sw, numOfRows, pageNo)
    return render_template('searchRequest.html', List=List)


# 버섯도감 상세정보 조회
@re_bp.route('/infoRequest', methods=['POST'])
def infoRequest():
    # 도감번호
    q1 = request.form['q1']
    List = re_service.infoRequest(q1)
    return render_template('infoRequest.html', List=List)


# 식용/독버섯 이미지 테스트
@re_bp.route('/testSurviveOrDeath')
def testSurviveOrDeath():
    x = random.randrange(1, 6)
    url = "/imgQuestion/question" + str(x) + ".html"
    # return render_template(url)
    return render_template('/imgQuestion/question1.html')


# 식용/독버섯 이미지 테스트
@re_bp.route('/wrongAnswer')
def wrongAnswer():
    advice = [
        "버섯은 경고 표지를 달고 오지 않는다. 여러분은 입에 넣기 전에 손에 쥐고 있는 것이 무엇인지 알고 있어야 한다.",
        "자문을 청하는 사람은 버섯에 중독되지 않는 사람이다.(남태평양 독립국 토가 속담)",
        "의심나면 그대로 내버려두라!(If in doubt, leave it!)",
        "의심나면 그냥 버려라!(If in doubt, discard it!)",
        "버섯은 날로(生으로) 먹는 것이 아니고, 알코올음료와 함께 먹는 것도 아니며, 많이 먹는 것이 아니다.",
        "식용버섯을 버리는 것이 독버섯을 먹고 중독되는 것보다 백번 낫다.",
        "기억하라: 야생버섯 식용은 (클라이밍이나 스노우보드와 같은) 위험한 스포츠(extreme sport)도 아니고, 시식해 본 가장 긴 버섯목록 만들기 경쟁도 아니다.(Greg A. Marley)",
        "모든 버섯은 먹을 수 있지만, 어떤 버섯들은 오직 단 한번만 먹을 수 있다.",
        "늙은 버섯채취자와 용감한 버섯 채취자는 많지만 늙고 용감한 버섯 채취자는 없다"
    ]
    msg = random.choice(advice)
    print(msg)
    return render_template('/imgQuestion/wrongAnswer.html', msg=msg)


@re_bp.route('/correctAnswer')
def correctAnswer():
    advice = [
        "버섯은 경고 표지를 달고 오지 않는다. 여러분은 입에 넣기 전에 손에 쥐고 있는 것이 무엇인지 알고 있어야 한다.",
        "자문을 청하는 사람은 버섯에 중독되지 않는 사람이다.(남태평양 독립국 토가 속담)",
        "의심나면 그대로 내버려두라!(If in doubt, leave it!)",
        "의심나면 그냥 버려라!(If in doubt, discard it!)",
        "버섯은 날로(生으로) 먹는 것이 아니고, 알코올음료와 함께 먹는 것도 아니며, 많이 먹는 것이 아니다.",
        "식용버섯을 버리는 것이 독버섯을 먹고 중독되는 것보다 백번 낫다.",
        "기억하라: 야생버섯 식용은 (클라이밍이나 스노우보드와 같은) 위험한 스포츠(extreme sport)도 아니고, 시식해 본 가장 긴 버섯목록 만들기 경쟁도 아니다.(Greg A. Marley)",
        "모든 버섯은 먹을 수 있지만, 어떤 버섯들은 오직 단 한번만 먹을 수 있다.",
        "늙은 버섯채취자와 용감한 버섯 채취자는 많지만 늙고 용감한 버섯 채취자는 없다"
    ]
    msg = random.choice(advice)
    print(msg)
    return render_template('/imgQuestion/correctAnswer.html', msg=msg)