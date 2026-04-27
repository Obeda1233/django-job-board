from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse
from.models import job
from django.core.paginator import Paginator
from .form import ApplyForm , JobForm
from django.contrib.auth.decorators import login_required
from.filters import JobFilter

# Create your views here.
def job_list(request):
    job_list = job.objects.all()
    myfilter = JobFilter(request.GET, queryset=job_list)
    job_list = myfilter.qs
    paginator = Paginator(job_list, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)



    context = {'jobs' : page_obj , 'myfilter': myfilter}
    return render(request,'job/job_list.html',context)


@login_required
def job_detail(request , slug):

    job_detail = job.objects.get(slug=slug)


    if request.method=='POST':
        form = ApplyForm(request.POST , request.FILES)
        print("test")
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
    else:
        form = ApplyForm()
    
    context = {'job': job_detail,'form' : form}
    return render(request,'job/job_detail.html',context)

@login_required
def add_job(request):
    if request.method=='POST':
        form = JobForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = JobForm()
    
    return render(request,'job/add_job.html',{'form':form})


def update(request , id):

    job_id = get_object_or_404(job,id=id)
    if request.method =='POST':
        job_save =JobForm(request.POST , request.FILES , instance=job_id)
        if job_save.is_valid():
            update_job=job_save.save(commit=False)
            update_job.owner=request.user
            update_job.save()
            
            return redirect('jobs:job_list')
    else: job_save = JobForm(instance=job_id)
    context={
        'form':job_save

    }
    

    return render(request,'job/update.html',context)


def delete (request,id):
    job_delete = get_object_or_404(job,id=id)
    if request.method == 'POST':
        job_delete.delete()
        return redirect('jobs:job_list')

    
    return render (request,'job/delete.html')