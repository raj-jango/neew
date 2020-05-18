from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'testapp/home.html')

def movies(request):
    head_msg='latest movies'
    msg3='baby doll tested positive'
    msg1='salman in bigboss 100'
    msg2='Modi going to act'
    my_dict={'head_msg':head_msg, 'msg1':msg1, 'msg2':msg2, 'msg3':msg3}
    return render(request,'testapp/movies.html', context=my_dict)

def sports(request):
    return render(request, 'testapp/sports.html')

def politics(request):
    return render(request, 'testapp/politics.html')
