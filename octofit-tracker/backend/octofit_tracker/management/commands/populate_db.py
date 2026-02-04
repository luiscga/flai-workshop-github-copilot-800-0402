from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Clearing existing data...')
        
        # Delete existing data using Django ORM
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS('Existing data cleared!'))
        
        # Create Teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Earth\'s Mightiest Heroes'
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League'
        )
        self.stdout.write(self.style.SUCCESS(f'Created teams: {team_marvel.name}, {team_dc.name}'))
        
        # Create Users - Marvel Heroes
        self.stdout.write('Creating Marvel heroes...')
        iron_man = User.objects.create(
            name='Tony Stark (Iron Man)',
            email='tony.stark@avengers.com',
            team_id=str(team_marvel._id)
        )
        captain_america = User.objects.create(
            name='Steve Rogers (Captain America)',
            email='steve.rogers@avengers.com',
            team_id=str(team_marvel._id)
        )
        black_widow = User.objects.create(
            name='Natasha Romanoff (Black Widow)',
            email='natasha.romanoff@avengers.com',
            team_id=str(team_marvel._id)
        )
        hulk = User.objects.create(
            name='Bruce Banner (Hulk)',
            email='bruce.banner@avengers.com',
            team_id=str(team_marvel._id)
        )
        thor = User.objects.create(
            name='Thor Odinson',
            email='thor@asgard.com',
            team_id=str(team_marvel._id)
        )
        
        # Create Users - DC Heroes
        self.stdout.write('Creating DC heroes...')
        batman = User.objects.create(
            name='Bruce Wayne (Batman)',
            email='bruce.wayne@wayneenterprises.com',
            team_id=str(team_dc._id)
        )
        superman = User.objects.create(
            name='Clark Kent (Superman)',
            email='clark.kent@dailyplanet.com',
            team_id=str(team_dc._id)
        )
        wonder_woman = User.objects.create(
            name='Diana Prince (Wonder Woman)',
            email='diana.prince@themyscira.com',
            team_id=str(team_dc._id)
        )
        flash = User.objects.create(
            name='Barry Allen (The Flash)',
            email='barry.allen@starlabs.com',
            team_id=str(team_dc._id)
        )
        aquaman = User.objects.create(
            name='Arthur Curry (Aquaman)',
            email='arthur.curry@atlantis.com',
            team_id=str(team_dc._id)
        )
        
        marvel_users = [iron_man, captain_america, black_widow, hulk, thor]
        dc_users = [batman, superman, wonder_woman, flash, aquaman]
        all_users = marvel_users + dc_users
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(all_users)} superhero users!'))
        
        # Create Activities
        self.stdout.write('Creating activities...')
        activity_types = [
            'Running', 'Cycling', 'Swimming', 'Weight Training', 
            'Boxing', 'Yoga', 'CrossFit', 'HIIT'
        ]
        
        activities_created = 0
        for user in all_users:
            # Create 5-8 activities per user
            import random
            num_activities = random.randint(5, 8)
            for i in range(num_activities):
                activity_type = random.choice(activity_types)
                duration = random.randint(30, 120)
                calories = duration * random.randint(8, 12)
                distance = round(random.uniform(3, 15), 2) if activity_type in ['Running', 'Cycling', 'Swimming'] else None
                
                Activity.objects.create(
                    user_id=str(user._id),
                    activity_type=activity_type,
                    duration=duration,
                    calories=calories,
                    distance=distance,
                    date=timezone.now() - timedelta(days=random.randint(0, 30)),
                    notes=f'{user.name} completed {activity_type}'
                )
                activities_created += 1
        
        self.stdout.write(self.style.SUCCESS(f'Created {activities_created} activities!'))
        
        # Create Leaderboard entries
        self.stdout.write('Creating leaderboard entries...')
        for rank, user in enumerate(all_users, start=1):
            # Calculate total calories and activities
            user_activities = Activity.objects.filter(user_id=str(user._id))
            total_calories = sum(a.calories for a in user_activities)
            total_activities = user_activities.count()
            
            team_name = team_marvel.name if user.team_id == str(team_marvel._id) else team_dc.name
            
            Leaderboard.objects.create(
                user_id=str(user._id),
                user_name=user.name,
                team_id=user.team_id,
                team_name=team_name,
                total_calories=total_calories,
                total_activities=total_activities,
                rank=rank
            )
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(all_users)} leaderboard entries!'))
        
        # Create Workouts
        self.stdout.write('Creating workout suggestions...')
        workouts = [
            {
                'name': 'Super Soldier Training',
                'description': 'Captain America inspired full body workout',
                'difficulty': 'Advanced',
                'duration': 60,
                'category': 'Strength',
                'exercises': [
                    {'name': 'Push-ups', 'sets': 5, 'reps': 20},
                    {'name': 'Pull-ups', 'sets': 4, 'reps': 15},
                    {'name': 'Squats', 'sets': 4, 'reps': 20},
                    {'name': 'Planks', 'sets': 3, 'duration': '60s'}
                ]
            },
            {
                'name': 'Asgardian Power Routine',
                'description': 'Thor\'s legendary strength training',
                'difficulty': 'Advanced',
                'duration': 75,
                'category': 'Power',
                'exercises': [
                    {'name': 'Deadlifts', 'sets': 5, 'reps': 8},
                    {'name': 'Hammer Curls', 'sets': 4, 'reps': 12},
                    {'name': 'Battle Ropes', 'sets': 3, 'duration': '45s'},
                    {'name': 'Box Jumps', 'sets': 4, 'reps': 15}
                ]
            },
            {
                'name': 'Speed Force Training',
                'description': 'Flash inspired cardio and agility workout',
                'difficulty': 'Intermediate',
                'duration': 45,
                'category': 'Cardio',
                'exercises': [
                    {'name': 'Sprint Intervals', 'sets': 8, 'duration': '30s'},
                    {'name': 'Burpees', 'sets': 4, 'reps': 15},
                    {'name': 'Jump Rope', 'sets': 3, 'duration': '2min'},
                    {'name': 'Mountain Climbers', 'sets': 3, 'reps': 30}
                ]
            },
            {
                'name': 'Amazonian Warrior Workout',
                'description': 'Wonder Woman\'s combat training routine',
                'difficulty': 'Advanced',
                'duration': 60,
                'category': 'Combat',
                'exercises': [
                    {'name': 'Sword Swings', 'sets': 4, 'reps': 20},
                    {'name': 'Shield Push-ups', 'sets': 4, 'reps': 15},
                    {'name': 'Lasso Spins', 'sets': 3, 'duration': '45s'},
                    {'name': 'High Kicks', 'sets': 4, 'reps': 20}
                ]
            },
            {
                'name': 'Dark Knight Conditioning',
                'description': 'Batman\'s stealth and strength program',
                'difficulty': 'Advanced',
                'duration': 90,
                'category': 'Mixed',
                'exercises': [
                    {'name': 'Ninja Rolls', 'sets': 3, 'reps': 10},
                    {'name': 'Rope Climbing', 'sets': 4, 'reps': 5},
                    {'name': 'Batarang Throws', 'sets': 3, 'reps': 30},
                    {'name': 'Shadow Boxing', 'sets': 5, 'duration': '3min'}
                ]
            },
            {
                'name': 'Atlantean Swim Training',
                'description': 'Aquaman\'s underwater fitness routine',
                'difficulty': 'Intermediate',
                'duration': 50,
                'category': 'Swimming',
                'exercises': [
                    {'name': 'Freestyle Laps', 'sets': 8, 'reps': 4},
                    {'name': 'Underwater Sprints', 'sets': 5, 'reps': 50},
                    {'name': 'Treading Water', 'sets': 3, 'duration': '5min'},
                    {'name': 'Dolphin Kicks', 'sets': 4, 'reps': 25}
                ]
            },
            {
                'name': 'Arc Reactor Endurance',
                'description': 'Iron Man\'s high-tech cardio routine',
                'difficulty': 'Intermediate',
                'duration': 40,
                'category': 'Endurance',
                'exercises': [
                    {'name': 'Treadmill Intervals', 'sets': 6, 'duration': '5min'},
                    {'name': 'Cycling', 'sets': 1, 'duration': '20min'},
                    {'name': 'Rowing', 'sets': 3, 'duration': '5min'}
                ]
            },
            {
                'name': 'Hulk Smash Circuit',
                'description': 'Bruce Banner\'s anger management through exercise',
                'difficulty': 'Beginner',
                'duration': 30,
                'category': 'Circuit',
                'exercises': [
                    {'name': 'Medicine Ball Slams', 'sets': 4, 'reps': 15},
                    {'name': 'Tire Flips', 'sets': 3, 'reps': 10},
                    {'name': 'Punching Bag', 'sets': 5, 'duration': '2min'},
                    {'name': 'Jump Squats', 'sets': 3, 'reps': 15}
                ]
            }
        ]
        
        for workout_data in workouts:
            Workout.objects.create(**workout_data)
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(workouts)} workout programs!'))
        
        # Summary
        self.stdout.write(self.style.SUCCESS('\n=== Database Population Complete ==='))
        self.stdout.write(f'Teams: {Team.objects.count()}')
        self.stdout.write(f'Users: {User.objects.count()}')
        self.stdout.write(f'Activities: {Activity.objects.count()}')
        self.stdout.write(f'Leaderboard Entries: {Leaderboard.objects.count()}')
        self.stdout.write(f'Workouts: {Workout.objects.count()}')
        self.stdout.write(self.style.SUCCESS('====================================='))
