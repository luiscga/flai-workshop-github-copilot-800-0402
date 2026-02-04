from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timezone


class UserModelTest(TestCase):
    """Test cases for User model"""

    def setUp(self):
        self.user = User.objects.create(
            name="Test User",
            email="test@example.com"
        )

    def test_user_creation(self):
        """Test that a user can be created"""
        self.assertEqual(self.user.name, "Test User")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertIsNotNone(self.user.created_at)

    def test_user_str(self):
        """Test user string representation"""
        self.assertEqual(str(self.user), "Test User")


class TeamModelTest(TestCase):
    """Test cases for Team model"""

    def setUp(self):
        self.team = Team.objects.create(
            name="Test Team",
            description="A test team"
        )

    def test_team_creation(self):
        """Test that a team can be created"""
        self.assertEqual(self.team.name, "Test Team")
        self.assertEqual(self.team.description, "A test team")
        self.assertIsNotNone(self.team.created_at)

    def test_team_str(self):
        """Test team string representation"""
        self.assertEqual(str(self.team), "Test Team")


class ActivityModelTest(TestCase):
    """Test cases for Activity model"""

    def setUp(self):
        self.user = User.objects.create(
            name="Test User",
            email="test@example.com"
        )
        self.activity = Activity.objects.create(
            user_id=str(self.user._id),
            activity_type="Running",
            duration=30,
            calories=300,
            distance=5.0,
            date=datetime.now(timezone.utc)
        )

    def test_activity_creation(self):
        """Test that an activity can be created"""
        self.assertEqual(self.activity.activity_type, "Running")
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.calories, 300)


class UserAPITest(APITestCase):
    """Test cases for User API endpoints"""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            name="Test User",
            email="test@example.com"
        )

    def test_get_users_list(self):
        """Test retrieving list of users"""
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        """Test creating a new user"""
        url = reverse('user-list')
        data = {
            'name': 'New User',
            'email': 'newuser@example.com'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)


class TeamAPITest(APITestCase):
    """Test cases for Team API endpoints"""

    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(
            name="Test Team",
            description="A test team"
        )

    def test_get_teams_list(self):
        """Test retrieving list of teams"""
        url = reverse('team-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_team(self):
        """Test creating a new team"""
        url = reverse('team-list')
        data = {
            'name': 'New Team',
            'description': 'A new test team'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ActivityAPITest(APITestCase):
    """Test cases for Activity API endpoints"""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            name="Test User",
            email="test@example.com"
        )
        self.activity = Activity.objects.create(
            user_id=str(self.user._id),
            activity_type="Running",
            duration=30,
            calories=300,
            distance=5.0,
            date=datetime.now(timezone.utc)
        )

    def test_get_activities_list(self):
        """Test retrieving list of activities"""
        url = reverse('activity-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_activities_by_user(self):
        """Test filtering activities by user"""
        url = reverse('activity-by-user')
        response = self.client.get(url, {'user_id': str(self.user._id)})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LeaderboardAPITest(APITestCase):
    """Test cases for Leaderboard API endpoints"""

    def setUp(self):
        self.client = APIClient()
        self.leaderboard_entry = Leaderboard.objects.create(
            user_id="123",
            user_name="Test User",
            total_calories=1000,
            total_activities=10,
            rank=1
        )

    def test_get_leaderboard(self):
        """Test retrieving leaderboard"""
        url = reverse('leaderboard-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_top_users(self):
        """Test retrieving top users from leaderboard"""
        url = reverse('leaderboard-top-users')
        response = self.client.get(url, {'limit': 5})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WorkoutAPITest(APITestCase):
    """Test cases for Workout API endpoints"""

    def setUp(self):
        self.client = APIClient()
        self.workout = Workout.objects.create(
            name="Morning Cardio",
            description="A cardio workout for beginners",
            difficulty="beginner",
            duration=30,
            category="cardio",
            exercises=["running", "jumping jacks"]
        )

    def test_get_workouts_list(self):
        """Test retrieving list of workouts"""
        url = reverse('workout-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_workouts_by_difficulty(self):
        """Test filtering workouts by difficulty"""
        url = reverse('workout-by-difficulty')
        response = self.client.get(url, {'difficulty': 'beginner'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
