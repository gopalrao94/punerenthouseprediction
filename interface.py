from project_app.utils import HouseRentPrediction
from flask import Flask, jsonify, render_template, request
import config

app = Flask(__name__)

#################################################################################
################################## Home API #####################################
#################################################################################

@app.route('/')
def rent_model():
    print('Welcome to the House Rent Prediction Model')
    return render_template('index.html')


#################################################################################
################################## Model API #####################################
#################################################################################

@app.route('/predict_rent', methods= ['POST','GET'])
def get_house_rent():
    if request.method == 'POST':
        print('We are in POST Method')
        data = request.form
        seller_type = data['seller_type']
        bedroom = eval(data['bedroom'])
        layout_type = data['layout_type']
        property_type = data['property_type'] 
        area = eval(data['area'])
        furnish_type = data['furnish_type']
        bathroom = eval(data['bathroom'])
        locality = data['locality']

        print(f'seller_type = {seller_type}, bedroom = {bedroom}, layout_type = {layout_type} ,property_type = {property_type}, area = {area},furnish_type = {furnish_type},bathroom = {bathroom}, locality = {locality} ')

        house_rent = HouseRentPrediction(seller_type, bedroom, layout_type, property_type, area, furnish_type, bathroom, locality)
        rent = house_rent.get_predicted_rent()
        return jsonify({'Result': f"Price of House Rent is : RS. {round(rent[0], 2)}"})
    
    else:

        print('We are in GET Method')
        data1 = request.args
        seller_type = data1.get('seller_type')
        bedroom = eval(data1.get('bedroom'))
        layout_type = data1.get('layout_type')
        property_type = data1.get('property_type')
        area = eval(data1.get('area'))
        furnish_type = data1.get('furnish_type')
        bathroom = eval(data1.get('bathroom'))
        locality = data1.get('locality')

        print(f'seller_type = {seller_type}, bedroom = {bedroom}, layout_type = {layout_type} ,property_type = {property_type}, area = {area},furnish_type = {furnish_type},bathroom = {bathroom}, locality = {locality} ')

        house_rent1 = HouseRentPrediction(seller_type, bedroom, layout_type, property_type, area, furnish_type, bathroom, locality)
        rent1 = house_rent1.get_predicted_rent()
        return jsonify({'Result': f"Price of House Rent is : RS. {round(rent1[0], 2)}"})



if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = config.PORT_NUMBER, debug=False)