from django.contrib import admin
from .models import Habit, HabitEntry

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'frequency', 'is_active', 'created_at']
    list_filter = ['frequency', 'is_active']
    search_fields = ['name', 'user__username']

@admin.register(HabitEntry)
class HabitEntryAdmin(admin.ModelAdmin):
    list_display = ['habit', 'date', 'completed', 'created_at']
    list_filter = ['completed', 'date']
    search_fields = ['habit__name']
    date_hierarchy = 'date'