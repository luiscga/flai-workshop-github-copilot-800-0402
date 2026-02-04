from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import (
    UserSerializer,
    TeamSerializer,
    ActivitySerializer,
    LeaderboardSerializer,
    WorkoutSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing User instances.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'])
    def by_team(self, request):
        """Get all users in a specific team"""
        team_id = request.query_params.get('team_id')
        if team_id:
            users = self.queryset.filter(team_id=team_id)
            serializer = self.get_serializer(users, many=True)
            return Response(serializer.data)
        return Response(
            {"error": "team_id parameter is required"},
            status=status.HTTP_400_BAD_REQUEST
        )


class TeamViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Team instances.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Activity instances.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    @action(detail=False, methods=['get'])
    def by_user(self, request):
        """Get all activities for a specific user"""
        user_id = request.query_params.get('user_id')
        if user_id:
            activities = self.queryset.filter(user_id=user_id).order_by('-date')
            serializer = self.get_serializer(activities, many=True)
            return Response(serializer.data)
        return Response(
            {"error": "user_id parameter is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    @action(detail=False, methods=['get'])
    def by_type(self, request):
        """Get all activities of a specific type"""
        activity_type = request.query_params.get('activity_type')
        if activity_type:
            activities = self.queryset.filter(activity_type=activity_type).order_by('-date')
            serializer = self.get_serializer(activities, many=True)
            return Response(serializer.data)
        return Response(
            {"error": "activity_type parameter is required"},
            status=status.HTTP_400_BAD_REQUEST
        )


class LeaderboardViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Leaderboard instances.
    """
    queryset = Leaderboard.objects.all().order_by('rank')
    serializer_class = LeaderboardSerializer

    @action(detail=False, methods=['get'])
    def top_users(self, request):
        """Get top N users from leaderboard"""
        limit = int(request.query_params.get('limit', 10))
        top_users = self.queryset[:limit]
        serializer = self.get_serializer(top_users, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_team(self, request):
        """Get leaderboard entries for a specific team"""
        team_id = request.query_params.get('team_id')
        if team_id:
            entries = self.queryset.filter(team_id=team_id)
            serializer = self.get_serializer(entries, many=True)
            return Response(serializer.data)
        return Response(
            {"error": "team_id parameter is required"},
            status=status.HTTP_400_BAD_REQUEST
        )


class WorkoutViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Workout instances.
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    @action(detail=False, methods=['get'])
    def by_difficulty(self, request):
        """Get workouts filtered by difficulty"""
        difficulty = request.query_params.get('difficulty')
        if difficulty:
            workouts = self.queryset.filter(difficulty=difficulty)
            serializer = self.get_serializer(workouts, many=True)
            return Response(serializer.data)
        return Response(
            {"error": "difficulty parameter is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """Get workouts filtered by category"""
        category = request.query_params.get('category')
        if category:
            workouts = self.queryset.filter(category=category)
            serializer = self.get_serializer(workouts, many=True)
            return Response(serializer.data)
        return Response(
            {"error": "category parameter is required"},
            status=status.HTTP_400_BAD_REQUEST
        )
