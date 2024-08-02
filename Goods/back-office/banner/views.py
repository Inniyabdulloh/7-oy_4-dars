from django.shortcuts import render, redirect
from django.views import View

from Goods.models import Banner


class BannerListView(View):
    def get(self, request):
        banners = Banner.objects.all()
        context = {'banners': banners}
        return render(request, 'back-office/banner/banner-list.html', context)


class BannerDetailView(View):
    def get(self, request, code):
        banner = Banner.objects.get(generate_code=code)
        context = {'banner': banner}
        return render(request, 'back-office/banner/banner-detail.html', context)


class BannerDeleteView(View):
    def get(self, request, code):
        banner = Banner.objects.get(generate_code=code)
        banner.delete()
        return redirect('banner-list')


class BannerUpdateView(View):
    def get(self, request, code):
        banner = Banner.objects.get(generate_code=code)
        context = {'banner': banner}
        return render(request, 'back-office/banner/banner-update.html', context)


    def post(self, request, code):
        title = request.POST.get('title')
        sub_title = request.POST.get('sub_title')
        image = request.POST.get('image')
        is_active = request.POST.get('active')

        print(f"{is_active} active")

        banner = Banner.objects.get(generate_code=code)
        banner.title = title
        banner.sub_title = sub_title
        banner.image = image
        if is_active == 'on':
            banner.is_active = True
        else:
            banner.is_active = False
        banner.save()
        return redirect('banner-detail', code=code)
