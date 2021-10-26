import joblib
import numpy as np
import pandas as pd


class Columns:
    def __init__(self, cap_shape, cap_surface, cap_color, bruises, odor, gill_color, population):
        self.cap_shape = cap_shape
        self.cap_surface = cap_surface
        self.cap_color = cap_color
        self.bruises = bruises
        self.odor = odor
        self.gill_color = gill_color
        self.population = population

class ColumnsService:
    def getResult(self, columns):
        model = joblib.load('mushroom_stand_out_model.pkl')  # 사용할 모델 파일 로드
        arr = np.zeros(49, dtype=int)
        for c in columns:
            arr[c] = 1
        res = model.predict([arr])
        return res