from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # enviamos el correo y redireccionamos
            email = EmailMessage(
                #Asunto
                "El Buque Page: Nuevo mensaje de contacto",
                #Cuerpo
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                #Email de Origem
                "no-contestar@inbox.mailtrap.io",
                #Email de Destino
                ["elbuquemarinero@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                #Todo a salido bien
                return redirect(reverse('contact')+"?ok")
            except:
                #Algo a salido mal
                return redirect(reverse('contact')+"?Fail")    
    return render(request, "contact/contact.html", {'form':contact_form})