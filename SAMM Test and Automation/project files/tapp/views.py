from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import ticket
from accounts.models import accounts
from accounts.views import var
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from datetime import timedelta
# Create your views here.


def main(request):
   
    cu = request.user
    if cu.id==None:
         return redirect('loginuser')           
    user=""
    objects=[]
    current_datetime = timezone.now()
    one_week_ago = current_datetime - timedelta(weeks=1)
    one_month_ago = current_datetime - timedelta(weeks=4)
    
 
    totaletickets=len(ticket.objects.all())
    ticketsmonth=len(ticket.objects.filter(created_date__range=[one_month_ago,current_datetime]))
    ticketsweek=len(ticket.objects.filter(created_date__range=[one_week_ago,current_datetime]))
    ticketsday=len(ticket.objects.filter(created_date=current_datetime))
    treatedtickets=0
    pendingtickets=0
    if cu.is_superuser==False:
        for elem in ticket.objects.order_by('created_date') :
            if cu.id == elem.created_by_id :
                  if elem.treated ==True :
                       treatedtickets+=1
                  else :
                       pendingtickets +=1
                  
                  objects.append((elem,cu.username)) 
    else:
        tickets = [elem for elem in ticket.objects.order_by('created_date')  ]     
        for elem in tickets :
            for elem2 in User.objects.all():
                if elem2.id == elem.created_by_id :
                   if elem.treated ==True :
                       treatedtickets+=1
                   else :
                       pendingtickets +=1
                                
                   objects.append((elem,elem2.username))  
    empty=True  
    totaleusertickets=len(objects)

    if request.method == 'POST':
        title= request.POST['title']
        description= request.POST['message']

        ticket.objects.create(
            title=title,
            description=description,
            created_by=cu,
            treated=False
            )
        return redirect('/main')
    if len(objects)==0:
         empty=True
    else:
         empty=False     
    return  render (request ,'page2.html', {'objects':objects,'cu':cu,'empty':empty,'ticketsmonth':ticketsmonth,'totaletickets':totaletickets,'ticketsweek':ticketsweek,'ticketsday':ticketsday,'totaleusertickets':totaleusertickets,'treatedtickets':treatedtickets,'pendingtickets' : pendingtickets},)



def deletepost(request,id):
        item_to_delete = get_object_or_404(ticket, pk=id)
        item_to_delete.delete()
        return redirect('main')
   
def treatpost(request,id):
     item = get_object_or_404(ticket, pk=id)
     item.treated=True
     item.save()
     return redirect('main')
     
     