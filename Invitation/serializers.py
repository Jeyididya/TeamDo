import os
from datetime import datetime, timedelta
from rest_framework import serializers
from .models import Invitation
from dotenv import load_dotenv
load_dotenv()


class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = '__all__'
        extra_kwargs = {
            'status': {'required': False},
            'expiration_date': {'required': False},
            'sender': {'required': False},
        }

    def create(self, validated_data):
        current_date = datetime.now().date()
        validated_data['sender'] = self.context['request'].user
        validated_data['expiration_date'] = current_date + \
            timedelta(days=int(os.getenv('EXPIRATION_DATE')))
        return super().create(validated_data)
