from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import viewsets
from .models import Habit, HabitEntry
from .serializers import HabitSerializer, HabitEntrySerializer

class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class HabitEntryViewSet(viewsets.ModelViewSet):
    serializer_class = HabitEntrySerializer

    def get_queryset(self):
        return HabitEntry.objects.filter(habit__user=self.request.user)