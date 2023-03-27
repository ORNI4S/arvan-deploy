from django.shortcuts import render
from django.http import JsonResponse
from django.views import View



class SayHello(View) : 
    def get(self, request) : 
        return JsonResponse({'status' : 'HELLO USER . MY NAME IS MIOMIO'})