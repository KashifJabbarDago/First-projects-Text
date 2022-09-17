
from django.shortcuts import render,HttpResponse,redirect
import string 
from text.models import ContactUs
from django.contrib import messages
# Create your views here.

def HomePage(request):
    return render(request,'text/Home.html')

def Result(request):
    textarea_text = request.POST.get('textarea')
    capital_switch = request.POST.get('capital')
    title_switch = request.POST.get('title')
    small_switch = request.POST.get('small')
    punctuation_switch = request.POST.get('punctution')
    character_switch = request.POST.get('Character')

    if capital_switch == 'on' and title_switch == 'on' and small_switch == 'on':
        return HttpResponse("<center><h2>You've opened all button</h2><p>Cannot open all button same time <br> Capitalize <br> Title <br> Small <br> These can't be all open same time , Try again! </p></center> ")
    
    if capital_switch == 'on' and small_switch == 'on':
        return HttpResponse("<center><h2>You've opened buttons </h2> <p> Capitalize <br> Small <br> at same time try again by disable one of them! </p> </center>")
    
    if capital_switch == 'on' and title_switch == 'on':
        return HttpResponse("<center><h2>You've opened buttons </h2> <p> Capitalize <br> Title <br> at same time try again by disable one of them! </p> </center>")

    if small_switch == 'on' and title_switch == 'on':
        return HttpResponse("<center><h2>You've opened buttons </h2> <p> Title <br> Small <br> at same time try again by disable one of them! </p> </center>")
    
    if capital_switch == 'on' and punctuation_switch == 'on':
        capitalized = textarea_text.upper()
        text=capitalized.translate(str.maketrans('', '', string.punctuation))
        params = {'text':text,'title':'Punctuations removed'}
        return render(request,'text/Result.html',params)

    if title_switch == 'on' and punctuation_switch == 'on':
        titled = textarea_text.title()
        text=titled.translate(str.maketrans('', '', string.punctuation))
        params = {'text':text,'title':'Punctuations removed'}
        return render(request,'text/Result.html',params)  

    if small_switch == 'on' and punctuation_switch == 'on':
        smalled = textarea_text.lower()
        text = smalled.translate(str.maketrans('', '', string.punctuation))
        params = {'text':text,'title':'Punctuations removed'}
        return render(request,'text/Result.html',params)  

    if character_switch == 'on' and punctuation_switch == 'on':
        punctuate_removed = textarea_text.translate(str.maketrans('', '', string.punctuation))
        count = 1
        for i in range(1,len(punctuate_removed)):
            if punctuate_removed[i] != ' ':
                count = count + 1 
            text = count 
        params ={'text':text,'title':'Total character with punctuation remove'}
        return render(request,'text/Result.html',params)    

    if punctuation_switch == 'on':
        # punctuations = '''!()-[]{ };:'"\,<>./?@#$%^&*_~'''
        text=textarea_text.translate(str.maketrans('', '', string.punctuation))
        params = {'text':text,'title':'Punctuations removed'}
        return render(request,'text/Result.html',params)
    
    if character_switch == 'on':
        count = 1
        for i in range(1,len(textarea_text)):
            if textarea_text[i] !=' ':
                count = count + 1
            text = count  
        params = {'text':text,'title':'Total number of character'}
        return render(request,'text/Result.html',params)


    if capital_switch == 'on':
        text =textarea_text.upper()
        params = {'text':text,'title':'Capital'}
        return render(request,'text/Result.html',params)
    
    if title_switch == 'on':
        text = textarea_text.title()
        params = {'text':text,'title':'Title'}
        return render(request,'text/Result.html',params)
    
    if small_switch == 'on':
        text = textarea_text.lower()
        params = {'text':text,'title':'lower'}
        return render(request,'text/Result.html',params)
    
    return HttpResponse("<h4><center>You did not submit any response try again </center></h4>")

def About(request):
    return render(request,'text/About.html')

def Contact(request):
    if request.method  == 'POST':
        name1 = request.POST['name']
        email1 = request.POST['email']
        phone1 = request.POST['phone']
        msg1 = request.POST['content']
        if len(name1) <2 or len(email1)< 5 or len(phone1) < 5:
            return HttpResponse('<center><h2>Form is not submitted try again!</h2></center>')
        else:
             contact = ContactUs(name=name1,email=email1,phone=phone1,msg=msg1)
             contact.save()
             return HttpResponse("<center><h2>form has been submitted!</h2></center>")
     
    return render(request,'text/Contact.html')
    