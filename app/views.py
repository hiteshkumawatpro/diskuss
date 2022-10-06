from django.http.response import HttpResponse
from django.urls.resolvers import URLPattern
import psycopg2
from django.http import request
from django.shortcuts import render

import os
from app.models import img
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
import re
from PIL import Image
from django.template.defaultfilters import slugify


def insertData():
    conn = psycopg2.connect("dbname='school' user='postgres' password='postgresql' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("insert into data(Name,Id,Marks) values('ete',10001,99),('nehaet',10002,98),('priyaete',10003,75),('krishert',10004,57),('shyamet',10005,54),('ramreyrehb',10006,45)")
    conn.commit()
    conn.close()




# Create your views here.
def index(request):
  
    return render(request,"Home.html")




def page2(request):
    
    return render(request,"Page-2.html")

def solutions(request,question,id):
    a = question
    b  = id
    a = str(a).replace("-"," ")
    
    conn = psycopg2.connect("dbname='school' user='postgres' password='postgresql' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute(f"select * from user_upload_details where question_id = {id}")
    t = cur.fetchall()
    cur.execute(f"select question from question_database where id = {id}")
    f = cur.fetchall()
   
    conn.commit()
    conn.close()

    return render(request,"Page-2.html",{"question":f[0][0],"chapter":b,"image_id":t[0][1],"answered_by":t[0][2],"remark":t[0][3]})






list_search_itr = []
def search_Algo_list_add(temp1_txt):
    le = len(temp1_txt)
    global list_search_itr
    list_search_itr.clear()
    acc_fac = 10
  
    remain_str  = (le%acc_fac)
    itr = 0
    while(True):
        st = 10*itr
        if (le - st) < 10:
            break
        else:
            st = temp1_txt[st:st+10]
            list_search_itr.append(st)
            itr = itr + 1


def displaydata():
    conn = psycopg2.connect("dbname='school' user='postgres' password='postgresql' port='5432' host='localhost'")
    cur = conn.cursor()

    cur.execute('''select * from question_database''')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    results_found = [[], []]
    for t in rows:
        counter = 0
       
        print(t)
    
        for txt_it in list_search_itr:
       
            
            patt = re.compile(r"{t}".format(t=txt_it))
            matches = patt.finditer(t[0])
            for match_i in matches:
                counter = counter + 1
        print("counter",counter)
        print("accuracy : ",counter / len(list_search_itr))
        if counter / len(list_search_itr) >= .5:
            results_found[0].append(counter / len(list_search_itr))
            results_found[1].append(t)
       

    return results_found






class s:
    question = str
    id = int
    chapter = int
    urlm = str



def search_str(request):
    list_emp = []

    if request.method == 'POST':
        tex = request.POST.get('name_text')
        print("---------------- ",tex,"----------------------")
        tex = tex.replace("(","")
        tex = tex.replace(")","")
        search_Algo_list_add(tex)
        lis = displaydata()
    
        lis = lis[1]   # lis[0] === accuracy , lis[1] === result question
        leng = str(len(lis))
        for i in lis:
            print(i)
            obj = s()
            name = i[0]
            obj.question = i[0]
            obj.id = i[1]
            obj.chapter = i[2]
            obj.urlm = slugify(name)
            list_emp.append(obj)
    return render(request,"Page-1.html",{"obje":list_emp,"total_le":leng})    

 



def imagesfn(request):
    list_emp = []
    if request.method == 'POST':
        obj = img()
        image = request.FILES['name_img']
        imgot = Image.open(image)
        tex = tess.image_to_string(imgot)
       
        obj.img_cus = image
        obj.save()

    tex = tex.replace("(","")
    tex = tex.replace(")","")
    search_Algo_list_add(tex)

    lis = displaydata()
    
    lis = lis[1]   # lis[0] === accuracy , lis[1] === result question
    leng = str(len(lis))
  
    for i in lis:
   
        print(i)
        obj = s()
        name = i[0]
        obj.question = i[0]
        obj.id = i[1]
        obj.chapter = i[2]
        obj.urlm = slugify(name)
        list_emp.append(obj)
    return render(request,"Page-1.html",{"obje":list_emp,"total_le":leng})    



       
    
    

def search_str(request):
    list_emp = []

    if request.method == 'POST':
        tex = request.POST.get('name_text')
        print("---------------- ",tex,"----------------------")
        tex = tex.replace("(","")
        tex = tex.replace(")","")
        search_Algo_list_add(tex)
        lis = displaydata()
    
        lis = lis[1]   # lis[0] === accuracy , lis[1] === result question
        leng = str(len(lis))
        for i in lis:
            print(i)
            obj = s()
            name = i[0]
            obj.question = i[0]
            obj.id = i[1]
            obj.chapter = i[2]
            obj.urlm = slugify(name)
            list_emp.append(obj)
    return render(request,"Page-1.html",{"obje":list_emp,"total_le":leng})    
