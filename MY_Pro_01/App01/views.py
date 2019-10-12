from django.shortcuts import render
from .models import FeedBackModels
from .forms import FeedBackForm
from django.http.response import HttpResponse


def feedbackview(request):
    if request.method == "POST":
        fform = FeedBackForm(request.POST)
        if fform.is_valid():
            vname = request.POST.get('Name')
            vMailId = request.POST.get('MailId')
            vProfession = request.POST.get('Profession')
            vSub = request.POST.get('Sub')
            vMsg = request.POST.get('Msg')
            data = FeedBackModels(
                Name=vname,
                MailId=vMailId,
                Profession=vProfession,
                Sub=vSub,
                Msg=vMsg,
            )
            data.save()
            fform = FeedBackForm()
            return render(request, 'feedback.html', {'fform': fform})
        else:
            return HttpResponse("Invalid detail Entered")
    else:
        fform = FeedBackForm()
        return render(request, 'feedback.html', {'fform': fform})