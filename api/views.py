from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
import json

# import models
from .models import TicketIDTriggered

# Create your views here.
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def trigger_playbook(request):
    try:
        body = json.loads(request.body)
        tiket_id = body.get('tiket_id')
        if tiket_id:
            ticket_id_obj, created = TicketIDTriggered.objects.get_or_create(tiket_id=tiket_id)
            ticket_id_obj.save()

            return JsonResponse({'message': tiket_id}, status=200)
        else:
            return Response({'error': 'tiket_id not found'}, status=400)
    except ValueError:
        return Response({'error': 'Invalid JSON in request body'}, status=400)
