# flask

from flask import Flask,request,jsonify
import util

app=Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response=jsonify({       #jsonify: This is a function provided by Flask that converts a Python dictionary into a JSON response object.
        'location':util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')   # response.headers: This accesses the headers of the HTTP response.
                                                              # .add('Access-Control-Allow-Origin', '*'): This adds a header to the response that specifies which origins are allowed to access the resource. In this case, the value '*' means that any origin is allowed to access the resource, which is useful for enabling Cross-Origin Resource Sharing (CORS)
    
    return response

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    total_sqft=float(request.form['total_sqft'])
    location=(request.form['location'])
    bhk=int(request.form['bhk'])
    bath=int(request.form['bath'])
    
    response=jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    
    response.headers.add('Access-Control-Allow-Origin','*')
    
    return response

if __name__=="__main__":
    app.run(debug=True)