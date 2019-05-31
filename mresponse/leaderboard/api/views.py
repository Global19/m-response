from rest_framework import exceptions, generics

from mresponse.leaderboard.api.serializers import LeaderboardSerializer
from mresponse.leaderboard.models import Leaderboard


class LeaderboardView(generics.RetrieveAPIView):
    serializer_class = LeaderboardSerializer
    queryset = Leaderboard.objects.all()

    def get_object(self):
        try:
            return self.get_queryset().current_week()
        except Leaderboard.DoesNotExist:
            # If the leaderboard does not exist, generate a new one.
            return self.get_queryset().generate_weekly_leaderboard()
