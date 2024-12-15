from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


# Step 3: Notification System
class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user)
        unread_notifications = notifications.filter(read=False)
        notifications_data = [
            {
                "actor": n.actor.username,
                "verb": n.verb,
                "timestamp": n.timestamp,
                "read": n.read,
            } for n in notifications
        ]
        return Response({
            "unread_count": unread_notifications.count(),
            "notifications": notifications_data
        })
