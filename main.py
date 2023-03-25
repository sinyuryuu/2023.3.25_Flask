from flask import Flask


#靜態檔案路徑
app = Flask(__name__,static_url_path='/static')

@app.route('/name/<string:x>/<string:y>')
def index(x,y):



    return f"<p>你好,</p>"


@app.route('/sum/<int:n>')
def sum(n):


    return





if __name__ == '__main__':

    app.run(debug=True,port = 5004)