from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ApplicationForm
from .models import AboutPageContent, HomePageContent, Image, Service


def home(request):
    content = HomePageContent.objects.prefetch_related(
        'images'
    ).order_by('-id').all()
    images = Image.objects.all()
    return render(request, 'main/home.html',
                  {'content': content, 'images': images})


def application_form(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            messages.success(
                request,
                f"Спасибо,"
                f" {application.name}! Ваша заявка успешно отправлена!"
            )
            return redirect('thank_you')
        else:
            messages.error(
                request,
                "Пожалуйста, исправьте ошибки в форме."
            )
    else:
        form = ApplicationForm()

    # Возвращаем шаблон с формой в любом случае
    return render(
        request,
        'main/application_form.html',
        {'form': form}
    )


def about(request):
    content = AboutPageContent.objects.prefetch_related(
        'aboutpage_images'
    ).all()
    return render(
        request,
        'main/about.html',
        {'content': content}
    )


def services(request):
    services = Service.objects.all()
    return render(
        request,
        'main/services.html',
        {'services': services}
    )


def thank_you(request):
    return render(request, 'main/thank_you.html')


def gallery(request):
    images = Image.objects.order_by(
        '-uploaded_at'
    ).all()
    return render(
        request,
        'main/gallery.html',
        {'images': images}
    )
