from flask import Flask, render_template
from routes import resource_routes as r
from routes import feature_route as f
from routes import img_routes as ir
from routes import system_routes as s
# 플라스크 객체 생성
app = Flask(__name__)

# 블루프린트 객체 등록
app.register_blueprint(r.re_bp)
app.register_blueprint(f.fe_bp)
app.register_blueprint(ir.is_bp)
app.register_blueprint(s.sy_bp)

@app.route('/')
def root():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()


