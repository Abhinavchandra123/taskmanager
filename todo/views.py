from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Employee, Operation, Branch, Department, Thought, Strategy, Strgtask,Job,Estatus
# from openpyxl import Workbook
import datetime
# import mimetypes
# import pandas as pd
# import os

# for login page


def loginmanager(request):
    if request.method == "POST":
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        user = authenticate(request, username=uname, password=pwd)
        if user:
            if user.is_staff == 1:
                login(request, user)
                return redirect('ind')
        # messages.error(request, 'Incorrect username or Password', extra_tags='text-danger')
    return render(request, 'login.html')

# logout function


def logoutUser(request):
    logout(request)
    return redirect('login')

# dashboard(index)


@login_required(login_url='login')
def index(request):
    date = datetime.datetime.now()
    tday = datetime.date.today()
    print(tday)
    da=date.strftime("%j")
    print(da)
    try:th=Thought.objects.get(day=da)
    except:th=None
    stg=Strategy.objects.all()
    nums=len(stg)
    op=Operation.objects.all()
    numo=len(op)
    print(nums)
    context={'th':th,'nums':nums,'numo':numo,'tday':tday}
    return render(request, 'index.html',context)


# master page
@login_required(login_url='login')
def master(request):
    tday = datetime.date.today()
    if request.method == "GET":
        bran = Branch.objects.all()
        dep = Department.objects.all()
        est=Estatus.objects.all()
        context = {'bran': bran, 'dep': dep,'tday':tday,'est':est}
        return render(request, 'master.html', context)
    if request.method == "POST":
        data = request.POST
        button = data['button1']
        print(button)
        if button == 'branch':
            bran = data['branch']
            Branch.objects.create(
                branch=bran
            )
        elif button == 'depart':
            dep = data['dep']
            Department.objects.create(
                department=dep
            )
        elif button == 'status':
            status=data['status']
            est=Estatus.objects.create(
                status=status
            )
        elif button == 'delbr':
            ids = data.getlist('check')
            print(ids)
            for i in ids:
                bks = Branch.objects.get(id=i)
                bks.delete()
        elif button == 'deldep':
            ids = data.getlist('check')
            print(ids)
            for i in ids:
                bks = Department.objects.get(id=i)
                bks.delete()
        elif button == 'delma':
            ids = data.getlist('check')
            print(ids)
            for i in ids:
                bks = Estatus.objects.get(id=i)
                bks.delete()
    return redirect('master')

# get count of meeting


# def count(request):
#     now = datetime.datetime.now()
#     sdate = f'{now.year}{now.month}{now.strftime("%d")}'
#     counts = Count.objects.order_by('-id')[0]
#     if counts.date == sdate:
#         pass
#     else:
#         # for count in counts:
#         coun = int(counts.count)+1
#         print(coun)
#         Count.objects.create(
#             count=coun,
#             date=sdate,
#         )
#     return redirect('manage')


# list employe
@login_required(login_url='login')
def listemp(request):
    tday = datetime.date.today()
    emps = Employee.objects.all()
    if request.method == 'POST':
        print('bdbj')
        data = request.POST
        if data.get('check') == None:
            print('hi')
            estatus = data['estatus']
            empid = data['empid']
            emp = Employee.objects.get(id=empid)
            emp.estatus = estatus
            emp.save()
            return redirect('list')
        if data.get('check') != None:
            ids = data.getlist('check')
            print(ids)
            for i in ids:
                bks = Employee.objects.get(id=i)
                bks.delete()
            return redirect('list')
    context = {'emps': emps,'tday':tday }
    return render(request, 'listemp.html', context)

# add employee
@login_required(login_url='login')
def addemp(request):
    tday = datetime.date.today()
    if request.method == 'GET':
        bran = Branch.objects.all()
        dep = Department.objects.all()
        context = {'bran': bran, 'dep': dep,'tday':tday}
        return render(request, 'addemployee.html', context)
    if request.method == 'POST':
        data = request.POST
        emp = data['empname']
        detail = data['details']
        branch = data['branch']
        dep = data['dep']
        phone = data['phone']
        email = data['email']

        Employee.objects.create(
            name=emp,
            email=email,
            phone=phone,
            details=detail,
            estatus="Active",
            branch_id=branch,
            department_id=dep
        )
        return redirect('list')


# edit employee table
@login_required(login_url='login')
def edit(request, pk):
    tday = datetime.date.today()
    bks = Employee.objects.get(id=pk)
    bran = Branch.objects.all()
    dep = Department.objects.all()
    if request.method == 'POST':
        data = request.POST
        emp = data['empname']
        detail = data['details']
        phone = data['phone']
        email = data['email']
        bks.name = emp
        bks.email = email
        bks.detail = detail
        bks.phone = phone
        bks.save()
        return redirect('list')

    data = {'bks': bks, 'bran': bran, 'dep': dep,'tday':tday}
    return render(request, 'editemployee.html', data)


@login_required(login_url='login')
def thought(request):
    tday = datetime.date.today()
    th = Thought.objects.all()
    if request.method == 'POST':
        data = request.POST
        button=data['button']
        if button=='add':
            date = data['date']

            # to get date in number 1-365
            leng=len(date)
            ab=[]
            abc=""
            for i in range(leng):
                if date[i]!='-':
                    abc=abc+f"{date[i]}"
                if date[i]=='-':
                    abc=int(abc)
                    ab.append(abc)
                    abc=''
            abc=int(abc)
            ab.append(abc)
            r=len(ab)
            for i in range(r):
                if i==0:
                    yy=ab[i]
                elif i==1:
                    mm=ab[i]
                elif i==2:
                    dd=ab[i]
            da=datetime.datetime(yy,mm,dd)
            da=da.strftime("%j")
            eng = data['english']
            mal = data['malayalam']
            # img=request.FILES.get('image')
            image = request.FILES.get('image')
            typ = data['types']
            Thought.objects.create(
                date=date,
                day=da,
                desce=eng,
                descm=mal,
                img=image,
                typ=typ
            )
            return redirect('thought')
        elif button=='del':
            ids = data.getlist('check')
            for i in ids:
                bks = Thought.objects.get(id=i)
                bks.delete()
            return redirect('thought')

    context = {'th': th,'tday':tday}
    return render(request, 'thoughts.html', context)

# edit thought
@login_required(login_url='login')
def edittho(request, pk):
    tday = datetime.date.today()
    bks=Thought.objects.get(id=pk)
    if request.method == 'POST':
        data = request.POST
        date = data['date']
        if date!="":
            # to get date in number 1-365
            leng=len(date)
            ab=[]
            abc=""
            for i in range(leng):
                if date[i]!='-':
                    abc=abc+f"{date[i]}"
                if date[i]=='-':
                    abc=int(abc)
                    ab.append(abc)
                    abc=''
            abc=int(abc)
            ab.append(abc)
            r=len(ab)
            for i in range(r):
                if i==0:
                    yy=ab[i]
                elif i==1:
                    mm=ab[i]
                elif i==2:
                    dd=ab[i]
            da=datetime.datetime(yy,mm,dd)
            da=da.strftime("%j")

        eng = data['english']
        mal = data['malayalam']
        typ = data['types']
        image = request.FILES.get('image')
        if image!=None:
            im=image
        else:
            im=bks.img
        bks.date = date
        bks.desce = eng
        bks.descm = mal
        bks.img = im
        bks.day=da
        bks.typ = typ
        bks.save()
        return redirect('thought')

    context = {'bks': bks,'tday':tday}
    return render(request, 'edittho.html', context)

# strategy page

@login_required(login_url='login')
def strategy(request):
    tday = datetime.date.today()
    if request.method =='GET':
        stg=Strategy.objects.all()
        ln=len(stg)
        if ln<1:
            print(ln)
            ln=f'S{0}{1}'
            stg=Strategy.objects.all()
            context={'stg':stg,'ln':ln,'tday':tday}
            return render(request,'strategy.html',context)
        else:
            print(ln)
            ln=f'S{0}{ln+1}'
            stg=Strategy.objects.order_by('sdate')
            context={'stg':stg,'ln':ln,'tday':tday}
            return render(request,'strategy.html',context)
    if request.method == 'POST':
        data = request.POST
        button=data['button1']
        # print(button)
        if button=='add':
            sid = data['sid']
            date = data['date']
            stime = data['stime']
            etime = data['etime']
            locat = data['location']
            lasts=Strategy.objects.create(
                sid=sid,
                sdate=date,
                stime=stime,
                etime=etime,
                location=locat,
            )
            last=lasts.id

            return redirect('addstg',last)
        elif button=='del':
            ids = data.getlist('check')
            for i in ids:
                bks = Strategy.objects.get(id=i)
                bks.delete()
            return redirect('strat')


# Add new stg page

@login_required(login_url='login')
def addstg(request,pk):
    tday = datetime.date.today()
    if request.method == 'GET':
        stg=Strategy.objects.get(id=pk)
        emp=Employee.objects.filter(estatus='Active')
        for i in emp:
            task=Strgtask.objects.filter(empid_id=i.id,sid_id=pk)
            total=len(task)
            i.tempc=total
            i.save()
        date = datetime.datetime.now()
        da=date.strftime("%j")
        print(da)
        try:th=Thought.objects.get(day=da)
        except:th=None
        context={'stg':stg,'emp':emp,'th':th,'tday':tday}
        return render(request,'prev.html',context)
    if request.method == 'POST':
        data = request.POST
        ids=data['id']
        sid = data['sid']
        date = data['date']
        stime = data['stime']
        etime = data['etime']
        locat = data['location']
        lasts=Strategy.objects.get(id=ids)
        lasts.sid=sid
        lasts.sdate=date
        lasts.stime=stime
        lasts.etime=etime
        lasts.location=locat
        lasts.save()
        return redirect('addstg',ids)

# add employee strategy progress and details(adding strategy task to employee page)
@login_required(login_url='login')
def emplst(request,pk):
    tday = datetime.date.today()
    sid=request.GET.get('sid')
    if sid==None:
        task=Strgtask.objects.get(id=pk)
        sid=task.sid_id
        pk=task.empid_id
    else:
        emp=Employee.objects.get(id=pk)
        task=Strgtask.objects.filter(empid_id=pk,sid_id=sid)
        total=len(task)
        emp.tempc=total
        emp.save()
        stg=Strategy.objects.get(id=sid)
    if request.method == 'GET':
        emp=Employee.objects.get(id=pk)
        task=Strgtask.objects.filter(empid_id=pk,sid_id=sid)
        total=len(task)
        emp.tempc=total
        emp.save()
        stg=Strategy.objects.get(id=sid)
        context={'emp':emp,'task':task,'stg':stg,'tday':tday,'sid':sid}
        return render(request,'strategytask.html',context)
    elif request.method == 'POST':
        data=request.POST
        button=data['button1']
        deli=data['deli']
        hm=data['hm']
        wgt=data['wgt']
        base=data['base']
        goal=data['goal']
        hilo=data['hilo']
        if button=='add':
            lasts=Strgtask.objects.create(
                deliv=deli,
                howmes=hm,
                wgt=wgt,
                base=base,
                goal=goal,
                hilo=hilo,
                result='',
                empid_id=pk,
                sid_id=sid,
            )

        elif button=='edit':
            ids=data['id']
            rest=data['result']
            lasts=Strgtask.objects.get(id=ids)
            lasts.deliv=deli
            lasts.howmes=hm
            lasts.wgt=wgt
            lasts.base=base
            lasts.goal=goal
            lasts.hilo=hilo
            lasts.result=rest
            lasts.save()

        lid=lasts.id
        print(lid)
        return redirect('emplst',lid)

# operation page
@login_required(login_url='login')
def opera(request):
    tday = datetime.date.today()
    op=Operation.objects.all()
    ln=len(op)
    print(ln)
    if request.method == 'GET':
        if ln<=0:
            ln=f'P{0}{1}'
            op=Operation.objects.all()
            print(ln)
            context={'op':op,'ln':ln,'tday':tday}
        else:
            op=Operation.objects.order_by('sdate')
            print(ln)
            ln=f'P{0}{ln+1}'
            context={'op':op,'ln':ln,'tday':tday}
        return render(request,'operation.html',context)
    if request.method == 'POST':
        data = request.POST
        button=data['button1']
        # print(button)
        if button=='add':
            pid = data['pid']
            date = data['date']
            stime = data['stime']
            etime = data['etime']
            locat = data['location']
            lasts=Operation.objects.create(
                pid=pid,
                sdate=date,
                stime=stime,
                etime=etime,
                location=locat,
            )
            last=lasts.id
            print(last)
            return redirect('addopera',last)
        elif button=='del':
            ids = data.getlist('check')
            for i in ids:
                bks = Operation.objects.get(id=i)
                bks.delete()
            return redirect('opera')

# edit operations detail and add work to employee
@login_required(login_url='login')
def addopera(request,pk):
    tday = datetime.date.today()
    if request.method == 'GET':
        op=Operation.objects.get(id=pk)
        emp=Employee.objects.filter(estatus='Active')
        for i in emp:
            taskln=Job.objects.filter(empid_id=i.id,opsid_id=op.id,status='Not completed')
            progress=len(taskln)
            i.progress=progress
            i.save()
        date = datetime.datetime.now()
        da=date.strftime("%j")
        try:th=Thought.objects.get(day=da)
        except:th=None

        context={'op':op,'emp':emp,'th':th,'tday':tday}
        return render(request,'prev.html',context)
    if request.method == 'POST':
        data = request.POST
        ids=data['id']
        pid = data['pid']
        date = data['date']
        stime = data['stime']
        etime = data['etime']
        locat = data['location']
        lasts=Operation.objects.get(id=ids)
        lasts.pid=pid
        lasts.sdate=date
        lasts.stime=stime
        lasts.etime=etime
        lasts.location=locat
        lasts.save()
        return redirect('addopera',ids)


# add employee strategy progress and details
@login_required(login_url='login')
def emplop(request,pk):
    tday = datetime.datetime.now()
    date=f"{tday.year}-{tday.month}-{tday.strftime('%d')}"
    sid=request.GET.get('pid')
    if sid==None:
        em=Employee.objects.get(id=pk)
        sid=em.tempp
    if request.method == 'GET':
        op=Operation.objects.get(id=sid)
        est=Estatus.objects.all()
        emp=Employee.objects.get(id=pk)
        taskln=Job.objects.filter(empid_id=pk,opsid_id=sid,status='Not completed')
        progress=len(taskln)
        emp.progress=progress
        emp.tempp=sid
        emp.save()
        context={'emp':emp,'op':op,'tday':tday,'est':est,'taskln':taskln}
        print(pk,sid)
        return render(request,'strategytask.html',context)
    if request.method == 'POST':
        data=request.POST
        button=data['button1']
        context={'sid':sid,'pk':pk}
        if button =='status':
            st=data['status']
            emp=Employee.objects.get(id=pk)
            emp.status_id=st
            emp.tempp=sid
            emp.save()
        elif button == 'add':
            job=data['job']
            tas=data['task']
            remark=data['remark']
            quan=data['quan']
            lasts=Job.objects.create(
                job=job,
                status='Not completed',
                tasks=tas,
                quantity=quan,
                remark=remark,
                opsid_id=sid,
                empid_id=pk,
                date=date
            )
        elif button =='edit':
            job=data['job']
            tas=data['task']
            remark=data['remark']
            quan=data['quan']
            status=data['status']
            ids=data['id']
            lasts=Job.objects.get(id=ids)
            lasts.job=job
            lasts.status=status
            lasts.tasks=tas
            lasts.quantity=quan
            lasts.remark=remark
            lasts.save()
        return redirect('emplop',pk)
@login_required(login_url='login')
def report(request,pk):
    pid=request.GET.get('pid')
    emp=Employee.objects.get(id=pk)
    jobs=Job.objects.filter(empid_id=pk,opsid_id=pid)
    jobp=Job.objects.filter(empid_id=pk,opsid_id=pid,status='Not completed')
    progress=len(jobp)
    total=len(jobs)
    completed=total-progress
    emp.task=total
    emp.completed=completed
    emp.save()
    context={'emp':emp,'jobs':jobs,'pid':pid}
    return render(request,'rep.html',context)
# @login_required(login_url='login')
# def manage(request):
#     emps = Employee.objects.filter(estatus='Present').order_by('name')
#     now = datetime.datetime.now()
#     date = f"{now.year}-{now.month}-{now.strftime('%d')}"
#     sdate = f'{now.year}{now.month}{now.strftime("%d")}'
#     # show date and time for user
#     dates = f"{now.strftime('%d')} - {now.strftime('%B')} - {now.strftime('%Y')} - {now.strftime('%I')} : {now.strftime('%M')} {now.strftime('%p')}"
#     if request.method == 'GET':
#         data = request.GET
#         sdat = f'{now.year}{now.month}{now.strftime("%d")}'
#         counts = Count.objects.order_by('-id')[0]
#         print(sdate)
#         print(counts.date)
#         if counts.date == sdat:
#             counts = Count.objects.get(date=sdat)
#         else:
#             counts = None
#         context = {'dates': dates, 'emps': emps, 'counts': counts}
#         return render(request, 'dashboard.html', context)

#     if request.method == 'POST':
#         data = request.POST
#         fro = data['from']
#         to = data['to']
#         if fro == '':
#             pass
#         else:
#             sdate = fro.replace("-", "")
#             date = fro
#         if to == '':
#             pass
#         else:
#             to = to
#         job = data['jobadd']
#         task = data['task']
#         refer = data['refer']
#         user = data['user']
#         print(user)
#         wstatu = data['wstatus']
#         Job.objects.create(
#             jobname=job,
#             task=task,
#             ref=refer,
#             sdate=date,
#             status='Not completed',
#             user_id=user,
#             day=sdate,
#             enddate=to,
#             wstatus=wstatu,
#         )
#         # filter employee details
#         jobs = Job.objects.filter(user_id=user, status='Not completed')
#         notcompleted = len(jobs)
#         jobs = Job.objects.filter(user_id=user)
#         total = len(jobs)
#         completed = total-notcompleted
#         # update table
#         em = Employee.objects.get(id=user)
#         em.progress = notcompleted
#         em.task = total
#         em.completed = completed
#         em.save()
#         return redirect('manage')

# # view and manage one person task


# @login_required(login_url='login')
# def prev(request):
#     now = datetime.datetime.now()
#     dates = f"{now.strftime('%d')} - {now.strftime('%B')} - {now.strftime('%Y')} - {now.strftime('%I')} : {now.strftime('%M')} {now.strftime('%p')}"
#     sdate = f'{now.year}-{now.month}-{now.strftime("%d")}'
#     if request.method == 'GET':
#         data = request.GET
#         empl = data.get('empl')
#         emps = Employee.objects.filter(id=empl)
#         counts = Count.objects.order_by('-id')[0]
#         sdat = f'{now.year}{now.month}{now.strftime("%d")}'
#         if counts.date == sdat:
#             counts = Count.objects.get(date=sdat)
#         else:
#             counts = None
#         jobtds = Job.objects.filter(
#             user_id=empl, sdate=sdate, status='Not completed')
#         jobs = Job.objects.filter(user_id=empl, status='Not completed')
#         jobss = Job.objects.filter(user_id=empl, status='Completed')
#         context = {'jobs': jobs, 'emps': emps, 'dates': dates,'counts': counts,
#                    'jobtds': jobtds, 'sdate': sdate, 'jobss': jobss}
#         return render(request, 'prev.html', context)
#     if request.method == 'POST':
#         data = request.POST
#         empl = request.GET.get('empl')
#         if data.get('old'):
#             job = data['job']
#             task = data['task']
#             remark = data['remark']
#             uid = data['user']
#             status = data['status']
#             # wstatus = data['wstatus']

#             if status == "Completed":
#                 fdate = dates
#             else:
#                 fdate = None
#             jobs = Job.objects.get(id=uid)
#             jobs.jobname = job
#             jobs.task = task
#             jobs.remark = remark
#             jobs.status = status
#             jobs.fdate = fdate
#             # job.wstatus=wstatus
#             jobs.save()
#             jobs = Job.objects.filter(user_id=empl, status='Not completed')
#             notcompleted = len(jobs)
#             jobs = Job.objects.filter(user_id=empl)
#             total = len(jobs)
#             completed = total-notcompleted
#             # update table
#             em = Employee.objects.get(id=empl)
#             em.progress = notcompleted
#             em.task = total
#             em.completed = completed
#             em.save()
#             return redirect('manage')

#         elif data.get('new'):
#             job = data['job']
#             task = data['task']
#             remark = data['remark']
#             uid = data['user']
#             status = data['status']
#             if status == "Completed":
#                 fdate = dates
#             else:
#                 fdate = None

#             jobs = Job.objects.get(id=uid)
#             jobs.jobname = job
#             jobs.task = task
#             jobs.remark = remark
#             jobs.status = status
#             jobs.fdate = dates
#             jobs.save()

#             jobs = Job.objects.filter(user_id=empl, status='Not completed')
#             notcompleted = len(jobs)
#             jobs = Job.objects.filter(user_id=empl)
#             total = len(jobs)
#             completed = total-notcompleted
#             # update table
#             em = Employee.objects.get(id=empl)
#             em.progress = notcompleted
#             em.task = total
#             em.completed = completed
#             em.save()
#             return redirect('manage')


# # add new employee


# # take report of all employee


# @login_required(login_url='login')
# def report(request):
#     emps = Employee.objects.filter(estatus='Present').order_by('name')
#     now = datetime.datetime.now()
#     sdate = f'{now.year}-{now.month}-{now.strftime("%d")}'
#     if request.method == 'GET':
#         context = {'emps': emps}
#         return render(request, 'rep.html', context)
#     # form submit for take report with date range
#     if request.method == 'POST':
#         # if there is no jobs
#         j = Job.objects.all()
#         b = len(j)
#         if b <= 0:
#             # context = {'emps': emps}
#             # return render(request,'rep.html',context)
#             return redirect('rep')
#         data = request.POST
#         fro = data['from']
#         to = data['to']
#         try:
#             uid = data['user']
#             if fro == '':
#                 try:
#                     jobs = Job.objects.order_by('id')[0]
#                     fro = jobs.sdate
#                 except:
#                     fro = sdate
#             else:
#                 fro = fro
#             print(fro)
#             if to == '':
#                 to = sdate
#             else:
#                 to = to
#             print(to)
#             f = int(fro.replace("-", ""))-1
#             t = int(to.replace("-", ""))+1
#             d = int(sdate.replace("-", ""))
#             if f >= d:
#                 response = HttpResponse(
#                     "<h1>Give Date is inavlid or Grater than today<h1>")
#                 return response
#             elif t <= f:
#                 response = HttpResponse("<h1>Give Date is inavlid<h1>")
#                 return response
#             lenj = 0
#             nub = 0
#             jsj = list()
#             jsjn = list()
#             jsjc = list()
#             a = pd.date_range(start=fro, end=to)
#             for da in a:
#                 i = da.date()
#                 print(i)
#                 jobs = Job.objects.filter(sdate=i, user_id=uid)  # total
#                 for job in jobs:
#                     jsj.append(job.id)
#                 lenj = lenj+len(jobs)

#                 jobss = Job.objects.filter(
#                     user_id=uid, sdate=i, status='Not completed')  # not completed
#                 for job in jobss:
#                     jsjn.append(job.id)
#                 nub = nub+len(jobss)

#                 jobst = Job.objects.filter(
#                     user_id=uid, sdate=i, status='Completed')  # completed
#                 for job in jobst:
#                     jsjc.append(job.id)

#                 comp = lenj-nub
#             # for excel report of employee
#             emps = Employee.objects.filter(id=uid)
#             jobs = Job.objects.filter(user_id=uid)
#             emp = Employee.objects.get(id=uid)
#             # Excel work book create
#             wb = Workbook()
#             # wb.create_sheet("sheet_one")
#             ws1 = wb.active
#             ws1['A1'] = 'Employee Name'
#             ws1['B1'] = emp.name
#             ws1['B3'] = 'Start Date'
#             ws1['C3'] = 'Jobname'
#             ws1['D3'] = 'Task'
#             ws1['E3'] = 'Reference'
#             ws1['F3'] = 'Status'
#             ws1['G3'] = 'Actual Complete Date'
#             ws1['H3'] = 'Finish Date'
#             ws1['I3'] = 'Remark'
#             rows = 4
#             cols = 2
#             i = 0
#             # loop and store data in excel
#             for job in jobs:

#                 if job.id in jsj:

#                     ws1.cell(rows+i, cols).value = job.sdate
#                     ws1.cell(rows+i, cols+1).value = job.jobname
#                     ws1.cell(rows+i, cols+2).value = job.task
#                     ws1.cell(rows+i, cols+3).value = job.ref
#                     ws1.cell(rows+i, cols+4).value = job.status
#                     ws1.cell(rows+i, cols+5).value = job.enddate
#                     ws1.cell(rows+i, cols+6).value = job.fdate
#                     ws1.cell(rows+i, cols+7).value = job.remark

#                     i = i+1
#             # save as report.xlsx in base dir
#             # wb.save('mysite/report.xlsx')
#             # save as report.xlsx in base dir
#             # wb.save('mysite/report.xlsx')
#             wb.save('report.xlsx')
#             emp = Employee.objects.get(id=uid)
#             emp.tempt = lenj
#             emp.tempp = nub
#             emp.tempc = comp
#             emp.save()
#             context = {'emps': emps, 'jobs': jobs, 'jsj': jsj,
#                        'jsjn': jsjn, 'jsjc': jsjc, 'uid': uid}
#             return render(request, 'rep.html', context)
#         except:
#             if fro == '':
#                 try:
#                     jobs = Job.objects.order_by('id')[0]
#                     fro = jobs.sdate
#                 except:
#                     fro = sdate
#             else:
#                 fro = fro
#             print("from:", fro)
#             if to == '':
#                 to = sdate
#             else:
#                 to = to
#             print("to:", to)
#             f = int(fro.replace("-", ""))-1
#             t = int(to.replace("-", ""))+1
#             d = int(sdate.replace("-", ""))
#             if f >= d:
#                 response = HttpResponse(
#                     "<h1>Give Date is inavlid or Grater than today<h1>")
#                 return response
#             elif t <= f:
#                 response = HttpResponse("<h1>Give Date is inavlid<h1>")
#                 return response
#             for j in emps:
#                 lenj = 0
#                 nub = 0
#                 a = pd.date_range(start=fro, end=to)
#                 for da in a:
#                     i = da.date()
#                     jobs = Job.objects.filter(sdate=i, user_id=j.id)  # total
#                     lenj = lenj+len(jobs)
#                     jobss = Job.objects.filter(
#                         user_id=j.id, sdate=i, status='Not completed')  # not completed
#                     nub = nub+len(jobss)
#                     comp = lenj-nub
#                  # refresh employee status
#                 emp = Employee.objects.get(id=j.id)
#                 emp.tempt = lenj
#                 emp.tempp = nub
#                 emp.tempc = comp
#                 emp.save()
#             return redirect('rep')

# # list employee


# @login_required(login_url='login')
# def listemp(request):
#     emps = Employee.objects.all()
#     if request.method == 'POST':
#         estatus = request.POST['estatus']
#         empid = request.POST['empid']
#         emp = Employee.objects.get(id=empid)
#         emp.estatus = estatus
#         emp.save()
#     context = {'emps': emps, }
#     return render(request, 'listemp.html', context)

# # Delete employee from table


# @login_required(login_url='login')
# def delb(request, id):
#     bks = Employee.objects.get(id=id)
#     nsj = Job.objects.filter(user_id=id)

#     nsj.delete()
#     bks.delete()

#     return redirect("list")

# # edit employee table


# @login_required(login_url='login')
# def edit(request, pk):
#     bks = Employee.objects.get(id=pk)
#     if request.method == 'POST':
#         data = request.POST
#         emp = data['empname']
#         detail = data['details']
#         phone = data['phone']
#         email = data['email']
#         bks.name = emp
#         bks.email = email
#         bks.detail = detail
#         bks.phone = phone
#         bks.save()

#     data = {'bks': bks}
#     return render(request, 'editemployee.html', data)


# # download xlsx file from base dir
# def download_file(request, filename=''):
#     if filename != '':
#         BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#         # Define the full file path
#         filepath = BASE_DIR + '/' + filename
#         # Open the file for reading content
#         path = open(filepath, 'rb')
#         # Set the mime type
#         mime_type, _ = mimetypes.guess_type(filepath)
#         # Set the return value of the HttpResponse
#         response = HttpResponse(path, content_type=mime_type)
#         # Set the HTTP header for sending to browser
#         response['Content-Disposition'] = "attachment; filename=%s" % filename
#         # Return the response value
#         return response
#     else:
#         # Load the template
#         return render(request, 'reo.html')
