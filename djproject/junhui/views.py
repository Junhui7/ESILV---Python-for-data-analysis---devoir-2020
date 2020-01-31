from django.shortcuts import render

from junhui.predict_model import rf_model, rf_predict, rf_score, rf_hyper_score


# Create your views here.

def home(request):
    final_model = rf_model()

    x = rf_score(final_model)

    return render(request, 'home.html', {"api": x})


def predict(request):
    return render(request, 'predict.html', {})


def hyper_parameter(request):
    return render(request, 'hyperparameter.html', {})


def hyper_score(request):
    n_estimators = request.POST['n_estimators']
    max_features = request.POST['max_features']
    max_depth = request.POST['max_depth']

    score = rf_hyper_score(int(n_estimators), int(max_features), int(max_depth))

    return render(request, 'resultat_hyper.html', {"score": score})


def resultat(request):

    chest_ACC_0_mean = request.POST['chest_ACC_0_mean']
    chest_ACC_1_mean = request.POST['chest_ACC_1_mean']
    chest_ACC_2_mean = request.POST['chest_ACC_2_mean']
    chest_ECG_mean = request.POST['chest_ECG_mean']
    chest_EMG_mean = request.POST['chest_EMG_mean']
    chest_EDA_mean = request.POST['chest_EDA_mean']
    chest_Temp_mean = request.POST['chest_Temp_mean']
    chest_Resp_mean = request.POST['chest_Resp_mean']
    wrist_ACC_0_mean = request.POST['wrist_ACC_0_mean']
    wrist_ACC_1_mean = request.POST['wrist_ACC_1_mean']
    wrist_ACC_2_mean = request.POST['wrist_ACC_2_mean']
    wrist_BVP_mean = request.POST['wrist_BVP_mean']
    wrist_EDA_mean = request.POST['wrist_EDA_mean']
    wrist_TEMP_mean = request.POST['wrist_TEMP_mean']

    final_model = rf_model()
    b = [chest_ACC_0_mean,
         chest_ACC_1_mean,
         chest_ACC_2_mean,
         chest_ECG_mean,
         chest_EMG_mean,
         chest_EDA_mean,
         chest_Temp_mean,
         chest_Resp_mean,
         wrist_ACC_0_mean,
         wrist_ACC_1_mean,
         wrist_ACC_2_mean,
         wrist_BVP_mean,
         wrist_EDA_mean,
         wrist_TEMP_mean]

    final_predict = rf_predict(final_model, b)
    return render(request, 'resultat.html', {'final_predict': final_predict})


'''
def home(request):

    api = 10/2

    return render(request, 'home.html', {"api": api})
'''
