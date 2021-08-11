from flask_cors import CORS
from flask.globals import request
from flask import Flask, abort, request, jsonify, Response, render_template
from flask.templating import render_template
from flask import Flask, jsonify
from flask import request
from VideoCheck import VideoCheck
from CheckByVideo import CheckByVideo


videocheck = VideoCheck()
app = Flask(__name__,template_folder='templates')
CORS(app)

checkbyvideo = CheckByVideo()
app = Flask(__name__,template_folder='templates')
CORS(app)

@app.route('/')
def Index():
    return "Welcome"

def CheckKey():
        return (False, None)

@app.route('/detectbyvideo', methods=['POST'])
def UploadFile():
    keyStatus = CheckKey()
    if (keyStatus[0]):
        return keyStatus[1]
    jsonData = request.form.get('data',{})
    print(jsonData)
    return videocheck.UploadFile(jsonData)  

@app.route('/detectbyebcam', methods=['GET'])
def DetectByCamera():
    keyStatus = CheckKey()
    if (keyStatus[0]):
        return keyStatus[1]

    return videocheck.WebCam()  

@app.route('/checkbyvideo', methods=['GET'])
def CheckByVideo():
    keyStatus = CheckKey()
    if (keyStatus[0]):
        return keyStatus[1]

    return checkbyvideo.detectByPathVideo()


app.run(host='0.0.0.0', port=82, debug=True)