from django.shortcuts import render
from django.views import View
class EBuy(View):
    def get(self, request):
        return render(request, 'EBuy.html')