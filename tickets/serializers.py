from rest_framework import serializers

from .models import Ticket

class TicketSerialzer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ('id','title','description','status','customer','staff','resolved')
