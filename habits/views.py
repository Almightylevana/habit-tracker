from django.shortcuts import render
from rest_framework import viewsets
from .models import Habit, HabitEntry
from .serializers import HabitSerializer, HabitEntrySerializer

class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

class HabitEntryViewSet(viewsets.ModelViewSet):
    queryset = HabitEntry.objects.all()
    serializer_class = HabitEntrySerializer