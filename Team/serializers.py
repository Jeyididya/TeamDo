from rest_framework import serializers
from .models import Team
from Invitation.models import Invitation


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class InvitationSerializer(serializers.ModelSerializer):
    reciver = serializers.ListField(child=serializers.IntegerField())

    class Meta:
        model = Invitation
        fields = ['reciver']

    def create(self, validated_data):
        # Get the sender from the request user
        sender = self.context['request'].user
        print("--\\>", validated_data)
        # Get the recipients from the validated data
        # recipients = validated_data['reciver']

        # # Create the invitation objects for each recipient
        # invitations = []
        # for recipient in recipients:
        #     invitation = Invitation.objects.create(
        #         sender=sender,
        #         reciver=recipient,
        #         team=validated_data['team'],
        #         status='pending',
        #         expiration_date=validated_data['expiration_date']
        #     )
        #     invitations.append(invitation)

        return validated_data
