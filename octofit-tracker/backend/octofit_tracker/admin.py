from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin interface for User model"""
    list_display = ('name', 'email', 'team_id', 'created_at')
    list_filter = ('team_id', 'created_at')
    search_fields = ('name', 'email')
    ordering = ('-created_at',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Admin interface for Team model"""
    list_display = ('name', 'description', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    ordering = ('-created_at',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    """Admin interface for Activity model"""
    list_display = ('user_id', 'activity_type', 'duration', 'calories', 'distance', 'date')
    list_filter = ('activity_type', 'date')
    search_fields = ('user_id', 'activity_type', 'notes')
    ordering = ('-date',)
    date_hierarchy = 'date'


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    """Admin interface for Leaderboard model"""
    list_display = ('user_name', 'team_name', 'total_calories', 'total_activities', 'rank', 'updated_at')
    list_filter = ('rank', 'team_name', 'updated_at')
    search_fields = ('user_name', 'team_name')
    ordering = ('rank',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    """Admin interface for Workout model"""
    list_display = ('name', 'difficulty', 'duration', 'category')
    list_filter = ('difficulty', 'category')
    search_fields = ('name', 'description', 'category')
    ordering = ('name',)
