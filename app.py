from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('model_LR_ayam.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', insurance_cost=0)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    pasar1, pasar2, pasar3, pasar4, pasar5 = [x for x in request.form.values()]

    data = []

    data.append(int(pasar1))
    data.append(int(pasar2))
    data.append(int(pasar3))
    data.append(int(pasar4))
    data.append(int(pasar5))
    
    
    prediction = model.predict([data])
    output = round(prediction[0][0], 2)

    return render_template('index.html', prediction=output, pasar1 = pasar1, pasar2 = pasar2, pasar3=pasar3, pasar4=pasar4, pasar5=pasar5)


if __name__ == '__main__':
    app.run(debug=True)