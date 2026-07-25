from django.db import models
from django.contrib.auth.models import User

class Habit(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', "Weekly")
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='habits'
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    frequency = models.CharField(
        max_length=10,
        choices=FREQUENCY_CHOICES,
        default='daily',
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return f"{self.name}({self.user.username})"

class HabitEntry(models.Model):
    habit = models.ForeignKey(
        Habit,
        on_delete=models.CASCADE,
        related_name='entries'
    )

    date = models.DateField()
    completed = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['habit', 'date']
        ordering = ['-date']

    def __str__(self):
        status = 'done' if self.completed else 'pending'
        return f"{self.habit.name} on {self.date} ({status})"
