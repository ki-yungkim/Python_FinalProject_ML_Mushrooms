from flask import request, render_template, Blueprint
from MushroomClassification.models import stand_out_model

co_bp = Blueprint('columns', __name__, url_prefix='/columns')
co_service = stand_out_model.ColumnsService()
columns = stand_out_model.Columns

# 입력 폼
@co_bp.route('/standOutForm')
def Form():
    print('form')
    return render_template('standOutForm.html')

# 버섯도감 목록 검색
@co_bp.route('/search', methods=['POST'])
def search():
    cap_shape = int(request.form['cap_shape'])
    cap_surface = int(request.form['cap_surface'])
    cap_color = int(request.form['cap_color'])
    bruises = int(request.form['bruises'])
    odor = int(request.form['odor'])
    gill_color = int(request.form['gill_color'])
    population = int(request.form['population'])
    c = [cap_shape, cap_surface, cap_color, bruises, odor, gill_color, population]
    res = co_service.getResult(c)
    if res == 1:
        res = '독버섯'
    else:
        res = '독버섯 아님'

    return str(res)