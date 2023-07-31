import pickle
import json
import numpy as np
import warnings
warnings.filterwarnings('ignore')

class HouseRentPrediction():
    
    def __init__(self,seller_type, bedroom, layout_type, property_type, area, furnish_type, bathroom, locality):
        self.seller_type = seller_type
        self.bedroom = bedroom
        self.layout_type = layout_type
        self.property_type = property_type
        self.area = area
        self.furnish_type = furnish_type
        self.bathroom = bathroom
        self.locality = 'locality_' + locality

    def load_model(self):
        with open('project_app/Linear_model.pkl', 'rb') as f:
            self.model = pickle.load(f)

        with open('project_app/project_data.json', 'rb') as f:
            self.project_data = json.load(f)

    def get_predicted_rent(self):
        self.load_model()

        test_array = np.zeros(len(self.project_data['columns']))
        test_array[0] = self.project_data['seller_type'][self.seller_type]
        test_array[1] = self.bedroom
        test_array[2] = self.project_data['layout_type'][self.layout_type]
        test_array[3] = self.project_data['property_type'][self.property_type]
        test_array[4] = self.area
        test_array[5] = self.project_data['furnish_type'][self.furnish_type]
        test_array[6] = self.bathroom
        locality_index = self.project_data['columns'].index(self.locality)
        test_array[locality_index] = 1

        predicted_rent = self.model.predict([test_array])
        # print(f"Rent per month is : RS. {round(predicted_rent[0], 2)}")
        return predicted_rent
    
if __name__== '__main__':
    seller_type = 'OWNER'
    bedroom = 2
    layout_type =  'BHK'
    property_type = 'Apartment' 
    area = 916
    furnish_type = 'Unfurnished'
    bathroom = 2
    locality = 'Wakad'
    house_rent = HouseRentPrediction(seller_type, bedroom, layout_type, property_type, area, furnish_type, bathroom, locality)
    # house_rent.get_predicted_rent()