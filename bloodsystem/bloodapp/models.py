from django.db import models

from django.db import models

# Create your models here.

class user(models.Model):

    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    uname=models.CharField(max_length=30)
    pwd=models.CharField(max_length=10)
    email=models.EmailField()
    contact=models.IntegerField()
    dob=models.DateField()
    add=models.CharField(max_length=80)
    bloodgroup=models.CharField(max_length=5)

    def __str__(self):
        return self.uname
    
    
    class Meta:
        db_table="user"


class Profile(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    class Meta:
        db_table="profile"        


    


class BloodRequest(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=5)
    quantity = models.IntegerField()
    date_requested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.uname} - {self.blood_group} ({self.quantity} units)"

    class Meta:
        db_table="order" 



from django.db import models

class BloodDonation(models.Model):
    user = models.ForeignKey('user', on_delete=models.CASCADE)
    health_issues = models.TextField()
    blood_level = models.CharField(max_length=10)
    place = models.CharField(max_length=100, null=True, blank=True)

    blood_group = models.CharField(max_length=3)
    donation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.uname} - {self.blood_group} - {self.donation_date}"

    class Meta:
        db_table="donator" 