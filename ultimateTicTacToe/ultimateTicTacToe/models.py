from django.db import models
import uuid
from django.urls import reverse

class Game(models.Model):
    IN_PROGRESS = 'PROGRESS'
    X_WON = 'Winner X'
    O_WON = 'Winner O'
    DRAW = "Draw"  
    STATE_CHOICES = [
        (IN_PROGRESS, 'In Progress'),
        (X_WON, 'X Won'),
        (O_WON, 'Winner O')
        (DRAW, 'Draw')
    ]

    
    state = models.CharField(
        max_length=5,
        choices=STATE_CHOICES,
        default=IN_PROGRESS,
    )
