from django.shortcuts import render
import pyttsx3

# Create your views here.
def index(request):
    print("hiiiiiiiiiii")
    engine = pyttsx3.init()
    print("init")
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-44)
    if 'input' in request.POST:
        input_lines = request.POST['input']
    else:
        input_lines = "hii, i am your Speecher! ,please give me text"

    print(input_lines)
    engine.say(input_lines)
    engine.runAndWait()
    return render(request,'index.html')
