import joblib
import numpy as np
import pandas as pd


class Feature:
    def __init__(self,bruises, odor, gill_size, gill_color, stalk_surface_above_ring,\
                                stalk_surface_below_ring, ring_type, spore_print_color, population):
        self.bruises = bruises
        self.odor = odor
        self.gill_size = gill_size
        self.gill_color = gill_color
        self.stalk_surface_above_ring = stalk_surface_above_ring
        self.stalk_surface_below_ring = stalk_surface_below_ring
        self.ring_type = ring_type
        self.spore_print_color = spore_print_color
        self.population = population

class FeatureService:
    def getResult(self, feature):
        model = joblib.load('mushroom_model.pkl')  # 사용할 모델 파일 로드
        arr = np.zeros(53, dtype=int)
        for f in feature:
            arr[f] = 1
        res = model.predict([arr])
        return res