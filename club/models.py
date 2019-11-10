from django.db import models
import datetime
# class Data1(models.Model):
#     date1 = models.DateField()
#     place = models.CharField(max_length=100)
#     worker = models.CharField(max_length=100)
#     thing = models.CharField(max_length=100)
class Club(models.Model):
   
    name = models.CharField(max_length=32,unique = True)
    def __str__(self):
        return self.name


class ClubDate(models.Model):
    club = models.ForeignKey(
        Club, on_delete=models.CASCADE, verbose_name="Club")
 
    date1 = models.DateField('Date', default=datetime.date.today)
   
    def __str__(self):
        return self.club.name +" "+ str(self.date1)

    class Meta:
        unique_together = ('club', 'date1')
    
class ClubMember(models.Model):
    club = models.ForeignKey(
        Club, on_delete=models.CASCADE, verbose_name="Club")
 
    member = models.CharField('Member Nickname',max_length=32)
    # fullname = models.CharField('Member Fullname',max_length=32)
    is_member = models.BooleanField('Is Member',default=True)
    # member_since = models.DateField('Member Since', default=datetime.date.today)
    class Meta:
        unique_together = ('club', 'member')
    
    def __str__(self):
        return "["+self.club.name +"] "+ self.member

    
class Attd(models.Model):
    clubdate = models.ForeignKey(
        ClubDate, on_delete=models.CASCADE, verbose_name="Club Date")
    clubmember = models.ForeignKey(
        ClubMember, on_delete=models.CASCADE, verbose_name="Club Member")
    class Meta:
        unique_together = ('clubdate', 'clubmember')
        verbose_name ="Attd"
        verbose_name_plural ="Attd"
    def __str__(self):
        return "["+str(self.clubdate.date1) +"] "+ self.clubmember.member

class Role(models.Model):
    name = models.CharField(max_length=32,unique = True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name ="Roles"
        verbose_name_plural ="Roles"

class AttdRole(models.Model):
    attd = models.ForeignKey(
        Attd, on_delete=models.CASCADE)
    role = models.ForeignKey(
        Role, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('attd', 'role')
        verbose_name ="Attd Role"
        verbose_name_plural ="Attd Role"


# https://www.toastmasters.org/membership/club%20meeting%20roles.aspx


class Data2(models.Model):
    ROLE_CHOICES = [
        ('Attendance', 'Attendance'),
        ('Ah-counter', 'Ah-counter'),
        ('GE', 'GE'),
        ('Grammarian', 'Grammarian'),
        ('IE', 'IE'),
        ('Speaker', 'Speaker'),
        ('TME', 'TME'),
        ('TT Speaker', 'TT Speaker'),
        ('TT Evaluator', 'TT Evaluator'),
        ('TT-master', 'TT-master'),
        ('Timer', 'Timer'),
    ]

    MEMBER_CHOICES = [
        ('Member', 'Member'),
        ('Guest', 'Guest'),
    ]

    name = models.CharField(max_length=32)
    member =  models.CharField( 'Member',choices=MEMBER_CHOICES,max_length=6)
    date1 = models.DateField('Date', default=datetime.date.today)
    role = models.CharField( 'Role', choices=ROLE_CHOICES,max_length=32)
    points = models.IntegerField(default=0)
    class Meta:
        unique_together = ('name', 'date1','role')
       
        verbose_name ="Meeting"
        verbose_name_plural ="Meeting"



class Best(models.Model):
    BEST_CHOICES = [
        ('tt', 'tt'),
        # ('Guest', 'Guest'),
    ]
    date1 = models.DateField()
    title = models.CharField(choices=BEST_CHOICES,default='tt',max_length=32)
    name = models.CharField(max_length=32)
    class Meta:
        unique_together = ( 'date1','title')
       
        verbose_name ="Meeting Best"
        verbose_name_plural ="Meeting Best"
