from flask import Flask, render_template
# import routes
from routes import route_mushroom

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

if __name__ == "__main__":
    app.run()