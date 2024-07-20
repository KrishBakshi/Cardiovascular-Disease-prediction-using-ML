import joblib
import json
import numpy as np

__model = None
__data_columns = None

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']

    global __model
    if __model is None:
        with open('./artifacts/model.pkl', 'rb') as f:
            __model = joblib.load(f)
    print("loading saved artifacts...done")



def predict(general_health, checkup, exercise, skin_cancer, other_cancer, depression, diabetes, arthritis, age_category, height, weight, bmi, smoking_history, 
            alcohol_consumption, fruit_consumption, green_vegetables_consumption, friedpotato_consumption,sex_female):
    x = np.zeros(len(__data_columns))
    x[0] = general_health[0]
    x[1] = checkup[0]
    x[2] = exercise[0]
    x[3] = skin_cancer[0]
    x[4] = other_cancer[0]
    x[5] = depression[0]
    x[6] = diabetes[0]
    x[7] = arthritis[0]
    x[8] = age_category[0]
    x[9] = height[0]
    x[10] = weight[0]
    x[11] = bmi[0]
    x[12] = smoking_history[0]
    x[13] = alcohol_consumption[0]
    x[14] = fruit_consumption[0]
    x[15] = green_vegetables_consumption[0]
    x[16] = friedpotato_consumption[0]
    x[17] = sex_female

    if  __model.predict([x]) == 0:
        return False
    else:
        return True


if __name__ == "__main__":
    load_saved_artifacts()
    #print(predict(0,3,0,0,0,0,0,1,10,10,32.66,14.54,1,0,1,1,1,1))
    # print(predict(2,4,1,0,0,0,0,1,9,165,108.86,39.94,1,1,1,1,1,1))