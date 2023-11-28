from django.shortcuts import render
from datetime import datetime
current_day = datetime.today().strftime('%A')
from Info.models import RazzakModel,ParthoModel,RiadulModel,TariqulModel,ShaonModel,MasudModel,ShahinModel,MuntasirModel,RafiModel,ZahidModel,NoticeModel

# Create your views here.
def home(request):
    razzak_n = RazzakModel.objects.last()
    let_razzak = razzak_n.razzak_not
    partho_n = ParthoModel.objects.last()
    print(partho_n.partho_not)
    riadul_n = RiadulModel.objects.last()
    tariqul_n = TariqulModel.objects.last()
    shaon_n = ShaonModel.objects.last()
    masud_n = MasudModel.objects.last()
    shahin_n = ShahinModel.objects.last()
    muntasir_n = MuntasirModel.objects.last()
    rafi_n = RafiModel.objects.last()
    zahid_n = ZahidModel.objects.last()


    nott = NoticeModel.objects.last()


    razzak = 'green'
    partho = 'green'
    tariqul = 'green'
    riadul = 'green'
    shaon = 'green'
    masud = 'green'
    shahin = 'green'
    rafi = 'green'
    zahid = 'green'
    muntasir = 'green'
    
    if current_day == 'Sunday' or current_day == 'Monday':
        razzak = 'red'
        shaon = 'red'
        shahin = 'red'
        rafi = 'red'
        masud = 'red'

    if current_day == 'Tuesday' or current_day == 'Monday':
        partho = 'red'
        riadul = 'red'
        tariqul = 'red'
        muntasir = 'red'
        zahid = 'red'

    data = {
        'teachers' : [
            {'name' : "Md Abdur Razzak",'des':'Senior Lecturer & Chariman','signal':razzak, 'notice_t': let_razzak},
            {'name' : "Partho Sarathi Sarker",'des':'Asst. Professor & Co-Chairman ','signal':partho, 'notice_t': partho_n.partho_not},
            {'name' : "Md. Riadul Islam",'des':'Asst. Professor','signal':riadul, 'notice_t': riadul_n.riadul_not},
            {'name' : "Md. Tariqul Islam",'des':'Lecturer','signal':tariqul, 'notice_t': tariqul_n.tariqul_not},
            {'name' : "Md. Mahadi Hasan Shaon",'des':'Lecturer','signal':shaon, 'notice_t': shaon_n.shaon_not},
            {'name' : "Md Shahin Hossen",'des':'Lecturer','signal':shahin, 'notice_t': shahin_n.shahin_not},
            {'name' : "Md. Masudur Rahman",'des':'Lecturer','signal':masud, 'notice_t': masud_n.masud_not},
            {'name' : "Md. Muntasir Rahman",'des':'Lecturer','signal':muntasir, 'notice_t': muntasir_n.muntasir_not},
            {'name' : "Md. Jubayar Alam Rafi",'des':'Lecturer','signal':rafi, 'notice_t': rafi_n.rafi_not},
            {'name' : "Md. Zahid Akon",'des':'Teaching Assistant','signal':zahid, 'notice_t': zahid_n.zahid_not},          
        ],
        'notice': [
          {'not': nott.notice}
        ]
    }

    return render(request, 'homepage.html',data)

def teacher(request):
    if request.method == "POST":
        razzak_not = request.POST.get('razzak_not')     
        ra_inf = RazzakModel(razzak_not=razzak_not,)
        if razzak_not != None:
         ra_inf.save()
  
        partho_not = request.POST.get('partho_not')     
        pa_inf = ParthoModel(partho_not=partho_not,)
        if partho_not != None:
         pa_inf.save()

 
        riadul_not = request.POST.get('riadul_not')     
        ri_inf = RiadulModel(riadul_not=riadul_not,)
        if riadul_not != None:
         ri_inf.save()


        tariqul_not = request.POST.get('tariqul_not')     
        ta_inf = TariqulModel(tariqul_not=tariqul_not,)
        if tariqul_not != None:
         ta_inf.save()


        shaon_not = request.POST.get('shaon_not')     
        sa_inf = ShaonModel(shaon_not=shaon_not,)
        if shaon_not != None:
         sa_inf.save()
    

        masud_not = request.POST.get('masud_not')     
        ma_inf = MasudModel(masud_not=masud_not,)
        if masud_not != None:
         ma_inf.save()


        shahin_not = request.POST.get('shahin_not')     
        sha_inf = ShahinModel(shahin_not=shahin_not,)
        if shahin_not != None:
         sha_inf.save()

 
        muntasir_not = request.POST.get('muntasir_not')     
        mu_inf = MuntasirModel(muntasir_not=muntasir_not,)
        if muntasir_not != None:
         mu_inf.save()

  
        rafi_not = request.POST.get('rafi_not')     
        raf_inf = RafiModel(rafi_not=rafi_not,)
        if rafi_not != None:
         raf_inf.save()

 
        zahid_not = request.POST.get('zahid_not')     
        za_inf = ZahidModel(zahid_not=zahid_not,)
        if zahid_not != None:
         za_inf.save()


        notice = request.POST.get('notice')     
        n_inf = NoticeModel(notice=notice,)
        if notice != None:
         n_inf.save()

    return render(request, 'admin.html')

    