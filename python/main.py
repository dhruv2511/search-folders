from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
import os

app = Flask(__name__)
dirName = '../files'
@app.route("/")
def index():
    fileName = request.args.get("fileName", "")
    if fileName:
      list_of_files = search_box(fileName)
    else:
      list_of_files = ""
    return render_template("form.html", data=list_of_files)


@app.route("/<string:fileName>")
def search_box(search_id):
  files = os.walk(dirName)
  list_of_files = []
  returned_list = []
  for dirpath, dirname, filenames in files:
    list_of_files += [os.path.join(dirpath, file) for file in filenames]
    
  for elem in list_of_files:
    fileName = elem.replace(dirName+"/", '')
    if search_id in fileName:
      returned_list += [fileName]

  return returned_list


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)