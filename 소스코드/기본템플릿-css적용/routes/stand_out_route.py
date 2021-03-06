from flask import request, render_template, Blueprint
from MushroomClassification.models import stand_out_model

co_bp = Blueprint('columns', __name__, url_prefix='/columns')
co_service = stand_out_model.ColumnsService()
columns = stand_out_model.Columns

# 입력 폼
@co_bp.route('/standOutForm')
def Form():
    cap_shape = None
    cap_surface = None
    cap_color = None
    bruises = None
    odor = None
    gill_color = None
    population = None
    return render_template('featureForm.html', cap_shape=cap_shape, cap_surface=cap_surface, cap_color=cap_color,bruises=bruises,odor=odor, gill_color=gill_color,population=population)

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
    cap_shapeList = ['bell', 'conical', 'flat', 'knobbed', 'sunken', 'convex']
    cap_surfaceList = ['fibrous', 'grooves', 'smooth', 'scaly']
    cap_colorList = ['buff', 'cinnamon', 'red', 'gray', 'pink', 'green', 'purple', 'white', 'yellow']
    bruisesList = ['없음', '있음']
    odorList = ['almond', 'creosote', 'foul', 'anise', 'musty', 'none', 'pungent', 'spicy', 'fishy']
    gill_colorList = ['buff', 'red', 'gray', 'chocolate', 'black', 'brown', 'orange', 'pink', 'green', 'purple', 'white','yellow']
    populationList = ['abundant', 'clustered', 'numerous', 'scattered', 'several', 'solitary']

    cap_shape = cap_shapeList[cap_shape]
    cap_surface = cap_surfaceList[cap_surface-6]
    cap_color = cap_colorList[cap_color-10]
    bruises = bruisesList[bruises-20]
    odor = odorList[odor-22]
    gill_color = gill_colorList[gill_color-31]
    population = populationList[population-43]


    return render_template('featureForm.html', res=res, cap_shape=cap_shape, cap_surface=cap_surface, cap_color=cap_color,bruises=bruises,odor=odor, gill_color=gill_color,population=population)