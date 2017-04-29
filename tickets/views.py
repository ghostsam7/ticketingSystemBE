from django.shortcuts import render
from rest_framework import viewsets

from .models import Ticket
from .serializers import TicketSerialzer

# Create your views here.

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerialzer
    filter_fields = ('id','status','resolved')
