import torch
import torch.nn as nn
import torch.nn.functional as F
import joblib
from flask import Flask, render_template
# import routes
from routes import route_mushroom
from Mushroom.models import NetInfo
app = Flask(__name__)

# app.register_blueprint(routes.mushroom_bp)
app.register_blueprint(route_mushroom.mushroom_bp)

"""
업로드된 이미지 파일 다루기 테스트
"""
UPLOAD_FOLDER = "static/uploads/"
app.secret_key = "test"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1280 * 1024

@app.route('/')
def root():
    return render_template('index.html')

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 6, 5) # kernel=5, paddig=0. stride=1. 32-5+1=28
        self.pool = nn.MaxPool2d(2, 2)  # 14
        self.conv2 = nn.Conv2d(6, 16, 5) # kernel=5, paddig=0. stride=1. 14-5+1=10 => max pooling 후 5X5
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        # 84를 60으로 변경 테스트
        self.fc2 = nn.Linear(120, 20)
        self.fc3 = nn.Linear(20, 9)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = torch.flatten(x, 1) # 배치를 제외한 모든 차원을 평탄화(flatten)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

if __name__ == "__main__":
    app.run()

