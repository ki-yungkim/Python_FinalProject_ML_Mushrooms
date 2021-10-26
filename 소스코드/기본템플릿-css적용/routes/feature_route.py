from flask import request, render_template, Blueprint
from MushroomClassification.models import feature_model

fe_bp = Blueprint('feature', __name__, url_prefix='/feature')
fe_service = feature_model.FeatureService()
feature = feature_model.Feature

# 입력 폼
@fe_bp.route('/featureForm')
def resourceForm():
    return render_template('featureForm.html')

# 버섯도감 목록 검색
@fe_bp.route('/search', methods=['POST'])
def search():
    bruises = int(request.form['bruises'])
    odor = int(request.form['odor'])
    gill_size = int(request.form['gill_size'])
    gill_color = int(request.form['gill_color'])
    stalk_surface_above_ring = int(request.form['stalk_surface_above_ring'])
    stalk_surface_below_ring = int(request.form['stalk_surface_below_ring'])
    ring_type = int(request.form['ring_type'])
    spore_print_color =int(request.form['spore_print_color'])
    population = int(request.form['population'])
    f = [bruises, odor, gill_size, gill_color, stalk_surface_above_ring,\
                                stalk_surface_below_ring, ring_type, spore_print_color, population]
    res = fe_service.getResult(f)
    if res == 1:
        res = '독버섯'
    else:
        res = '독버섯 아님'

    return str(res)