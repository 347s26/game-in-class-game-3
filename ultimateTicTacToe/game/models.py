from django.db import models

import uuid


class Game(models.Model):
    IN_PROGRESS = 'PROGRESS'
    X_WON = 'X_WON'
    O_WON = 'O_WON'
    DRAW = 'DRAW'

    STATE_CHOICES = [
        (IN_PROGRESS, 'In Progress'),
        (X_WON, 'X Won'),
        (O_WON, 'O Won'),
        (DRAW, 'Draw')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    state = models.CharField(max_length=10, choices=STATE_CHOICES,
                             default=IN_PROGRESS)

    def __str__(self):
        return f"Game {self.id} - {self.state}"


class Square(models.Model):
    """One of the 9 main squares in the ultimate tic-tac-toe board"""
    game = models.ForeignKey(Game, on_delete=models.CASCADE,
                             related_name='squares')
    position = models.IntegerField()  # 0-8, which main square this is
    claimed_by = models.CharField(max_length=1, blank=True)

    class Meta:
        unique_together = ['game', 'position']
        ordering = ['position']

    def __str__(self):
        return f"S{self.position} - Claim: {self.claimed_by or 'None'}"


class SubSquare(models.Model):
    """One of the 9 tiny squares inside each main Square"""
    square = models.ForeignKey(Square, on_delete=models.CASCADE,
                               related_name='sub_squares')
    position = models.IntegerField()
    claimed_by = models.CharField(max_length=1, blank=True)

    class Meta:
        unique_together = ['square', 'position']
        ordering = ['position']

    def __str__(self):
        return f"SS {self.position} - Claimed: {self.claimed_by or 'None'}"

