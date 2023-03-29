from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from parrot import Parrot
import torch
import warnings
warnings.filterwarnings("ignore")

# Create your views here.
@api_view(['GET', 'POST'])
def ParaphraseViewSet(request):
    if request.method == 'GET':
        return Response(request.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5")

        phrases = request.data['paragraphs'].split(",")
        #phrases = request.data['paragraphs']

        result = []

        for phrase in phrases:
            para_phrases = parrot.augment(input_phrase=phrase, use_gpu=False)
            result.append(para_phrases)
            #for para_phrase in para_phrases:
            #    result.append(para_phrase)
        
        return Response(result, status=status.HTTP_200_OK)
