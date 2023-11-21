from django.shortcuts import render, get_object_or_404
from .models import PokeModel, Slider

#не полное отображение
def poke_list_view(request):
    if request.method == 'GET':
        poke_list = PokeModel.objects.all()
        slider_list = Slider.objects.all()
        return render(request, template_name='pokemons/index.html', context={
            'poke_list': poke_list,
            'slider_list': slider_list
        })

#detail
def poke_detail_view(request, id):
    if request.method == 'GET':
        poke_id = get_object_or_404(PokeModel, id=id)
        return render(request, template_name='pokemons/poke_detail.html', context={'poke_id': poke_id})