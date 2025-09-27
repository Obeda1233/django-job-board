from django.db import models



JOB_TYPE =(
('full time','full time'),
('part time','part time'),

)

# Create your models here.
class job(models.Model):   #table
    title = models.CharField(max_length=100)  #colum
    #loction
    job_type = models.CharField(max_length=15 , choices=JOB_TYPE)
    description = models.TextField(max_length= 1000)
    puplished_at = models.DateField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experirnce = models.IntegerField(default=1)


    def __str__(self):
        return self.title
     


    

    