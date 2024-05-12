from django.shortcuts import render

from joblib import load

model = load('./savedModel/model.joblib')
def predictor(request):
    if request.method == 'POST':
        url = request.POST['url']
        prediction = model.predict([url])
        return render(request, 'main.html', {'result': prediction})
    return render(request, 'main.html')
