from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime
from datetime import datetime
def index(request):
#   context = {
#   "time": strftime("%Y-%m-%d %H:%M %p", localtime())
#   }
    context = {
        "time": datetime.now()
    }
#   initially had gmtime() tried out localtime() to see the difference make sure you import at top, can't see the difference need to play with more.
    # datetime.now seems to work even better, again make sure to import
    return render(request,'showtime/index.html', context)