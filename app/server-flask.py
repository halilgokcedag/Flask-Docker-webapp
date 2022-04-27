from flask import Flask
from flask import request
from flask import jsonify
from datetime import datetime
from importlib_metadata import version
import docker

app = Flask(__name__)

@app.route("/")
def result(): 
    #dictionary with values to convert to json format
    values = [{
            "timestamp": datetime.now(),
            "hostname": get_host_ip(),
            "engine": get_module_version("flask"),
            "visitor ip": get_remote_ip()
        }]

    return jsonify(values)

def get_remote_ip():
    return request.remote_addr

def get_module_version(module):
    return module + " " + version(module)
    

def get_host_ip():
    return request.host.split(':')[0]

if __name__ == "__main__":
    #run the app from all interfaces with port 5000
    app.run(host='0.0.0.0', port=5000)