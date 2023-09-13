from django.shortcuts import render
from djcelery.celery import add
from celeryapp.tasks import sub
from celery.result import AsyncResult
# Create your views here.


#Enqueue task using delay()
# def index(request):
#     print("Results: ")
#     result = add.delay(10,20)
#     print("Result: ", result)

#     res = sub.delay(90,100)
#     print("res: ", res)
#     return render(request,"celeryapp/home.html")

#Enqueue task using apply_async()
# def index(request):
#     print("Results: ")
#     result = add.apply_async(args=[10,20])
#     print("Result: ", result)

#     res = sub.apply_async(args=[908,100])
#     print("res: ", res)
#     return render(request,"celeryapp/home.html")


#Display adddittion value after task execution
def index(request):
    result = add.delay(10, 30)
    return render(request,"celeryapp/home.html",{'result': result})


def about(request):
    print("Results: ")
    return render(request,"celeryapp/about.html")


def check_result(request, task_id):
    #retrieve the task result using the task id
    result = AsyncResult(task_id)
    print("Ready: ", result.ready())
    print("Successful: ", result.successful())
    print("Failed: ", result.failed())
    #print("Get: ", result.get())
    return render(request,"celeryapp/result.html",{'result':result})

def contact(request):
    print("Results: ")
    return render(request,"celeryapp/contact.html")


