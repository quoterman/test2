from django.db import models

class D_PROJECT(models.Model):
    LINK = models.CharField(max_length=50)
    LOGIN = models.CharField(max_length=32)
    PASSWORD = models.CharField(max_length=32)

    def __unicode__(self):
        return self.LINK

class D_TEAM(models.Model):
    NAME = models.CharField(max_length=30)
    PORJECT = models.ForeignKey(D_PROJECT)

    def __unicode__(self):
        return self.NAME

class D_PROGRAMMER(models.Model):
    NAME = models.CharField(max_length=30)
    TEAM = models.ForeignKey(D_TEAM)

    def __unicode__(self):
        return self.NAME

class D_COMMIT(models.Model):
    PROGRAMMER = models.ForeignKey(D_PROGRAMMER)
    DATE = models.DateTimeField()
    NEW = models.IntegerField()
    DEL = models.IntegerField()

    def __unicode__(self):
        return self.id
