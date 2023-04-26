from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from main.models import deviceData
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from .models import MyUser
from django.contrib.auth.decorators import login_required
import random
from main.helper import empty_check,password_check


# Create your views here.
def login_page(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(username=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('mainPage')
        else:
            return render(request, 'log.html',{'text':'wrong userid and password'})
    return render(request, 'log.html')


@login_required(login_url='login')
def mainPage(request):
    user_username=request.user.first_name
    id=request.user.deviceID
    return render(request,'index.html',{'text':'Hello '+user_username,'id':id})

@login_required(login_url='login')
def user_edit(request):
    
    if request.method=='POST':
        your_name=request.POST.get('name')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        address=request.POST.get('address')
        area=request.POST.get('area')
        mobile=request.POST.get('phone_number')
        plant_name=request.POST.get('plant_name')
        old_password=request.POST.get('oldpassword')
        try:
            if password_check(password1, password2) and empty_check(your_name) and empty_check(email) and empty_check(address) and empty_check(area) and empty_check(plant_name) and empty_check(old_password):
                euser = authenticate(email=request.user.email, password=old_password)        #work
                euser.email=email
                euser.first_name=your_name
                euser.address=address
                euser.mobileNumber=mobile
                euser.fieldArea=area
                euser.plantName=plant_name
                euser.set_password(password1)
                euser.save()
                return redirect('logout')
            else :
                return render(request, 'userEdit.html',{'text':'Invalid Input'})
        except Exception as e:
            return render(request, 'userEdit.html',{'text':'Something going wrong'})
    else:
        user_username=request.user.first_name
        user_deviceid=request.user.deviceID
        user_email=request.user.email
        user_address=request.user.address
        user_area=request.user.fieldArea
        user_plantname=request.user.plantName
        user_mobile=request.user.mobileNumber
        return render(request, 'userEdit.html',{'username':user_username,'email':user_email,'deviceid':user_deviceid,'address':user_address,'area':user_area,'plantname':user_plantname,'mobilenumber':user_mobile})

@login_required(login_url='login')
def userProfileData(request):
        user_username=request.user.first_name
        user_deviceid=request.user.deviceID
        user_email=request.user.email
        user_address=request.user.address
        user_area=request.user.fieldArea
        user_plantname=request.user.plantName
        user_mobile=request.user.mobileNumber
        return render(request, 'userPData.html',{'username':user_username,'email':user_email,'deviceid':user_deviceid,'address':user_address,'area':user_area,'plantname':user_plantname,'mobilenumber':user_mobile})

def createAccount(request):
    if request.method=='POST':
        your_name=request.POST.get('name')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        address=request.POST.get('address')
        area=request.POST.get('area')
        mobile=request.POST.get('phone_number')
        plant_name=request.POST.get('plant_name')
        print(your_name,email,password1,password2,address,area,mobile,plant_name)
        try:
            if password_check(password1, password2) and empty_check(your_name) and empty_check(email) and empty_check(address) and empty_check(area) and empty_check(plant_name):
                number = random.randint(1000,9999)
                numstr=str(number)
                result=MyUser.objects.create_user(email=email,password=password1,first_name=your_name,address=address,mobileNumber=mobile,fieldArea=area,plantName=plant_name,deviceID=email+numstr)
                result.save()
                print("all good")
                return render(request, 'log.html',{'text':'Log in now'})
            else:
                print("type your password")
                return render(request, 'cr.html',{'text':'Type input currently.'})
        except Exception as e:
                print(e)
                return render(request, 'cr.html',{'text':e})
        return HttpResponse(usercheck)
    return render(request,'cr.html')


@csrf_exempt
def updateDeviceData(request):
    if request.method=='POST':
        try :
            print(request.body)
            data=json.loads(request.body)
            if MyUser.objects.filter(deviceID=data.get("deviceid")).exists():
                deviceid=data.get("deviceid")
                soiln=float(data.get("soiln"))
                soilp=float(data.get("soilp"))
                soilk=float(data.get("soilk"))
                light=float(data.get("light"))
                lightr=float(data.get("lightr"))
                lightg=float(data.get("lightg"))
                lightb=float(data.get("lightb"))
                soilmos=float(data.get("soilmos"))
                hum=float(data.get("hum"))
                tem=float(data.get("tem"))
                bs=int(data.get("bs"))
                print(deviceid,soiln,soilp,soilk,soilmos,light,lightr,lightg,lightb,tem,hum)
                result=deviceData(deviceId=deviceid,soilN=soiln,soilP=soilp,soilK=soilk,soilMos=soilmos,light=light,lightR=lightr,lightG=lightg,lightB=lightb,tem=tem,hum=hum,bstatus=bs,utime=datetime.now())
                result.save()
                return JsonResponse({'success':'True'})
            else:
                return JsonResponse({'error':'The deviceid is not exists.'})
        except Exception as e:
            print(e)
            return JsonResponse({"error":"not a valid data"})
        
        return JsonResponse({'error':'Device is not exist.'})
    else :
        return HttpResponse("bad request")


def getdevicedata(request):
    if request.method=='GET':
        uid=request.GET.get('id')
        soiln=[]
        soilp=[]
        soilk=[]
        light=[]
        lightr=[]
        lightg=[]
        lightb=[]
        soilmos=[]
        tem=[]
        hum=[]
        bs=[]
        timet=[]

        number_of_data=10
        count=1
        a=deviceData.objects.filter(deviceId=uid).order_by('utime') #[:2]  #[::-1]
        for rdata in reversed(a):
            if count>number_of_data:
                break
            else :
                temm=rdata.utime
                t=temm.time()
                ts=t.strftime('%H:%M:%S')
                time_data=ts
                timet.append(time_data)
                soiln.append(float(rdata.soilN))
                soilp.append(float(rdata.soilP))
                soilk.append(float(rdata.soilK))
                light.append(float(rdata.light))
                lightr.append(float(rdata.lightR))
                lightg.append(float(rdata.lightG))
                lightb.append(float(rdata.lightB))
                soilmos.append(float(rdata.soilMos))
                tem.append(float(rdata.tem))
                hum.append(float(rdata.hum))
                bs.append(float(rdata.bstatus))
                count+=1

        data={"time":timet,"soiln":soiln,"soilp":soilp,"soilk":soilk,"light":light,"lightr":lightr,"lightg":lightg,"lightb":lightb,"soilmos":soilmos,"tem":tem,"hum":hum,"bs":bs}
        return JsonResponse(data)
    else:
        return JsonResponse({'error':'not a get request'})


# def test(request):
#     count=0
#     a=deviceData.objects.filter(deviceId="1234").order_by('utime') #[:2]  #[::-1]
#     for rdata in reversed(a):
#         if count>7:
#             break
#         print(rdata.soilN,rdata.soilP)
#     return HttpResponse(a)

def logout_page(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def get_all_data(request):
    
    uid=request.user.deviceID
    soiln=[]
    soilp=[]
    soilk=[]
    light=[]
    lightr=[]
    lightg=[]
    lightb=[]
    soilmos=[]
    tem=[]
    hum=[]
    bs=[]
    timet=[]

    a=deviceData.objects.filter(deviceId=uid).order_by('utime') #[:2]  #[::-1]
    for rdata in reversed(a):
            temm=rdata.utime
            t=temm.time()
            d=temm.date()
            ts=t.strftime('%H:%M:%S')
            ds=d.strftime('%Y-%m-%d')
            time_data=ts+" "+ds
            timet.append(time_data)
            soiln.append(float(rdata.soilN))
            soilp.append(float(rdata.soilP))
            soilk.append(float(rdata.soilK))
            light.append(float(rdata.light))
            lightr.append(float(rdata.lightR))
            lightg.append(float(rdata.lightG))
            lightb.append(float(rdata.lightB))
            soilmos.append(float(rdata.soilMos))
            tem.append(float(rdata.tem))
            hum.append(float(rdata.hum))
            bs.append(float(rdata.bstatus))

    return render(request, 'alldata.html',{'soiln':soiln,'soilp':soilp,'soilk':soilk,'light':light,'lightr':lightr,'lightg':lightg,'lightb':lightb,'soilmos':soilmos,'tem':tem,'hum':hum,'bs':bs,'time':timet})

login_required(login_url='login')
def seg(request):
    return render(request, 'seg.html')
    #email=rahul2002@gmail.com
    #password=rahul12345
    #deviceid=rahul2002@gmail.com8683