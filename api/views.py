from rest_framework import generics, permissions
from rest_framework.response import Response
import json
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from .models import TicketIDTriggered



class TriggerPlaybookAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]

    def post(self, request, *args, **kwargs):
        try:
            request_body = request.data
            ticket_id = request_body.get('tiket_id')

            if not ticket_id:
                return Response({'error': 'ticket_id not found'}, status=400)

            ticket_id_obj, created = TicketIDTriggered.objects.get_or_create(tiket_id=ticket_id)
            ticket_id_obj.save()

            return Response({'message': ticket_id_obj.tiket_id}, status=201)

        except json.JSONDecodeError as e:
            return Response({'error': f'Invalid JSON in request body: {e}'}, status=400)
