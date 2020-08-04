from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    usersEnrolled = models.ManyToManyField('Meetups', related_name="signUp")
    #following = models.ManyToManyField('User', related_name="follower")

    def serialize(self):
            return {
                "id": self.id,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "email": self.email,
    }

class Meetups(models.Model):
    meetupCreator = models.ForeignKey("User", on_delete=models.CASCADE, related_name="createdMeetups")
    subjType = models.ForeignKey("SubjectTypes", on_delete=models.PROTECT, related_name="subjMeetups")
    subjCode = models.CharField(max_length=25)
    meetupType = models.ForeignKey("MeetupTypes", on_delete=models.SET_NULL, null=True, related_name="options")
    description = models.TextField(blank=True)
    buildingNames = models.ForeignKey("Buildings", on_delete=models.PROTECT, related_name="events")
    meetupRoom = models.CharField(max_length=20)
    meetupStart = models.DateTimeField()
    meetupEnd = models.DateTimeField()

    isActive = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Meetups"

    def serialize(self):
            return {
                "id": self.id,
                "meetupCreator": self.meetupCreator.email,
                "subjType": self.subjType.subject,
                "subjCode": self.subjCode,
                "meetupType": self.meetupType.type,
                "description": self.description,
                "buildingNames": self.buildingNames.building,
                "meetupRoom": self.meetupRoom,
                "meetupStart": str(self.meetupStart),
                "meetupEnd": str(self.meetupEnd),
                "isActive": self.isActive,
        }



class MeetupTypes(models.Model):
    type = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = "MeetupTypes"

    def __str__(self):
        return self.type

class SubjectTypes(models.Model):
    subject = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "SubjectTypes"

    def __str__(self):
        return self.subject

class Buildings(models.Model):
    building = models.CharField(max_length=40)
     
   
    class Meta:
        verbose_name_plural = "Buildings"

    def __str__(self):
        return self.building


   