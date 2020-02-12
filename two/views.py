from django.shortcuts import render
from django.http import HttpResponse
import two.models as models
def index(request): 
    context ={
        'name' : 'yyy'
    }
    return render(request, 'index1.html',context=context)

def tindex1(request):
    return render(request, 'index.html')

def add(request):
    for i in range(10):
        stu = Student()
        stu.s_name = 'xiaoming' + str(i)
        stu.s_age = 15 + i
        stu.save()
    stu.save()
    return HttpResponse('add sucess')

#objects.all()展示数据
#context 传字典
def show(request):
    '''
    students = Student.objects.all()

    context = {
        'namels' : students
    }
    '''
    context = {'namels' :models.opmysql().getALL()}
    print(context)
    return render(request,'show.html',context= context)
    
#objects.get(字段名 = '')查询
#save 保存   delete 删除
def update(request):
    context = {}

    try:
        xm = Student.objects.get(s_name = 'xiaoming1')
    
        context = {
            'name' : xm.s_name
        }

        xm.s_name = 'xiao_ming'

        xm.save()
    except:
        print('not exist')
    return render(request,'update.html', context=context)

def search(request):
    return render(request, 'search.html')

def respond(request):
    name = request.GET['uname']
    passwd = request.GET['passwd']
    return HttpResponse(name + ' '+passwd)

def form_post(request):
    print(request.method)
    if(request.method == "POST"):
        return HttpResponse("post")
    return render(request, 'post.html')

def post(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    passwd = request.POST.get('passwd')

    return HttpResponse("info <p></p> %s %s %s"%(name,age,passwd))

def demo(request):
    return render(request, 'demo.html')