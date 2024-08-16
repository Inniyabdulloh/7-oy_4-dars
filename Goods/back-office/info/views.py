from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from Goods.models import Info, InfoInstaPhoto



class InfoListView(View):
    def get(self, request):
        infos = Info.objects.all()
        context = {'infos': infos}
        return render(request, 'back-office/info/info-list.html', context)


class InfoDetailView(View):
    def get(self, request, code):
        info = Info.objects.get(generate_code=code)
        context = {'info': info}
        return render(request, 'back-office/info/info-detail.html', context)


class InfoCreateView(View):
    def get(self, request):
        return render(request, 'back-office/info/info-add.html')

    def post(self, request):
        phone = request.POST['phone']
        address = request.POST['address']
        is_active = bool(request.POST.get('active'))
        facebook = request.POST['facebook']
        twitter = request.POST['twitter']
        linkedin = request.POST['linkedin']


        info = Info.objects.create(
            phone=phone,
            address=address,
            is_active=is_active,
            facebook=facebook,
            twitter=twitter,
            linkedin=linkedin,
        )

        photos = request.FILES.getlist('photos')
        for photo in photos:
            InfoInstaPhoto.objects.create(
                photo=photo,
                info=info,
            )

        return redirect('info-list')


class InfoUpdateView(View):
    def get(self, request, code):
        info = Info.objects.get(generate_code=code)
        context = {'info': info}
        return render(request, 'back-office/info/info-update.html', context)

    def post(self, request, code):
        info = Info.objects.get(generate_code=code)
        info_photos = InfoInstaPhoto.objects.filter(info=info)


        info.phone = request.POST['phone']
        info.address = request.POST['address']
        is_active = request.POST.get('active')
        if is_active == 'on':
            info.is_active = True
        else:
            info.is_active = False

        photos = request.FILES.getlist('photos')
        if photos:
            for photo in photos:
                InfoInstaPhoto.objects.create(info=info, photo=photo)

            info_photos.delete()


        info.facebook = request.POST['facebook']
        info.twitter = request.POST['twitter']
        info.linkedin = request.POST['linkedin']

        info.save()

        return redirect('info-detail', code=info.generate_code)


class InfoDeleteView(View):
    def get(self, request, code):
        info = Info.objects.get(generate_code=code)
        info.delete()
        return redirect('info-list')