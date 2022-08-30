from django.shortcuts import render
from .models import Familiares
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context



def familiares(request):
    mama=Familiares(nombre="Hebe", dni=18145622, fecha_nacimiento=datetime(1966, 9, 8))
    papa=Familiares(nombre="Carlos", dni=17163902, fecha_nacimiento=datetime(1963, 3, 2))
    hermano=Familiares(nombre="Tomas", dni=40166504, fecha_nacimiento=datetime(1994, 6, 7))
    texto_mama=f"Mi mama se llama {mama.nombre}, su dni es {mama.dni} y nació el {mama.fecha_nacimiento}."
    texto_papa=f" Mi papa se llama {papa.nombre}, su dni es {papa.dni} y nació el {papa.fecha_nacimiento}."
    texto_hermano=f" Mi hermano se llama {hermano.nombre}, su dni es {hermano.dni} y nació el {hermano.fecha_nacimiento}."
    texto_final=[texto_mama, texto_papa, texto_hermano]
    diccionario={"familiar_uno": mama, "familiar_dos": papa, "familiar_tres": hermano, "texto_final": texto_final}
    mama.save()
    papa.save()
    hermano.save()
    archivo=open("C:/Users/Nicolás/Desktop/Mi primer MVT/MVT_NicolasVilla/Plantillas/template1.html")
    contenido=archivo.read()
    archivo.close()
    plantilla=Template(contenido)
    contexto=Context(diccionario)
    documento=plantilla.render(contexto)    
    return HttpResponse(documento)
    