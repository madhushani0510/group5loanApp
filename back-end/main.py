from unicodedata import name
from flask.ext.cors import CORS, cross_origin
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world"


cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/add-pool",methods=["GET"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def addToPoolLoon():
    # file1 = open('myfile.txt', 'w')
    # L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
    # s = "Hello\n"
  
    # # Writing a string to file
    # file1.write(s)
  
    # # Writing multiple strings
    # # at a time
    # file1.writelines(L)
  
    # # Closing file
    # file1.close()
  
    # # Checking if the data is
    # # written to file or not
    # file1 = open('myfile.txt', 'r')
    # print(file1.read())
    # file1.close()
    return "Hello world"

if __name__ == "__main__":
    app.run()