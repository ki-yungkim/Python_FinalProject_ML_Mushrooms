from flask import Flask, render_template
from routes import btnc_routes as bt

# 플라스크 객체 생성
app = Flask(__name__)

# 블루프린트 객체 등록
app.register_blueprint(bt.bt_bp)

@app.route('/')
def root():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()