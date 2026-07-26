from rest_framework import serializers
from .models import Habit, HabitEntry

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['id', 'user', 'name', 'description', 'frequency', 'is_active', 'created_at']
        read_only_fields = ['id', 'created_at']

class HabitEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitEntry
        fields = ['id', 'habit', 'date', 'completed', 'notes', 'created_at']
        read_only_fields = ['id', 'created_at']