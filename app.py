#Import necessary libraries
from flask import Flask, render_template, Response, jsonify, request, abort
# from werkzeug.utils import secure_filename
# import imghdr
from get_data import prediction, get_sel_images
# from get_data import livePrediction
import os


#Initialize the Flask app
app = Flask(__name__)


# ---------------------prediction function---------------------------# 
def predicted_image(img_file):
    #print("img_file", img_file)
    experiment_images = ["people1.jpg", "people2.jpg", "people3.jpg", "people4.jpg", "people5.jpg", "people6.jpg", "people7.jpg"]
    if img_file not in experiment_images:
        base_path = "./static/upload/"
    else:
        base_path = "./Resources/Experiment/"
    img_path = base_path + img_file
    print("path:", img_path)
    data = prediction(img_path)
    return data
# -------------------------------------------------------------------#


# UPLOAD_FOLDER = './static/upload'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
# app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png']

# def validate_image(stream):
#     header = stream.read(512)
#     stream.seek(0) 
#     format = imghdr.what(None, header)
#     if not format:
#         return None
#     return '.' + (format if format != 'jpeg' else 'jpg')
   

# default app route
@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')


# #app route for uploading
# @app.route('/upload', methods=["GET", "POST"])
# def uploader():
#    if request.method == 'POST':
#       f = request.files['file']
#       filename = secure_filename(f.filename)
#       if filename != '':
#           file_ext = os.path.splitext(filename)[1]
#           if file_ext not in app.config['UPLOAD_EXTENSIONS'] or file_ext != validate_image(f.stream):
#               abort(400)
#           f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#           print("Yay! It Worked!")
#           return '', 204


# app route for image prediction
@app.route("/get_image/<img>", methods=["GET", "POST"])
def get_predicted_image(img):
    print("image file rendered:",img)
    #img = "people5.jpg"
    data = predicted_image(img)   
    print(data)
    return jsonify(data)

# app route for image file selection
@app.route("/api/v1.0/select_option", methods=["GET", "POST"])
def get_selected_images():    
    img_files = get_sel_images()
    return jsonify(img_files)


# # app route for video feed
# @app.route("/video_feed", methods=["GET", "POST"])
# def video_feed():    
#     return Response(livePrediction(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)