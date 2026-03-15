from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


JOB_TYPE =(
('full time','full time'),
('part time','part time'),

)

def image_upload(instance,filename):
    imagename,extension = filename.split(".")
    return "jobs/%s/%s.%s "%(instance.id,instance.id,extension)
    
    
    # Create your models here.
class job(models.Model):   #table
    owner = models.ForeignKey(User,related_name='job_owner',on_delete=models.CASCADE) # type: ignore
    title = models.CharField(max_length=100)  #colum
    #loction
    job_type = models.CharField(max_length=15 , choices=JOB_TYPE)
    description = models.TextField(max_length= 1000)
    puplished_at = models.DateField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experirnce = models.IntegerField(default=1)
    category = models.ForeignKey('category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)

    slug = models.SlugField(blank=True, null=True)
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(job,self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    



class category(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name


     

class Apply(models.Model):
     job = models.ForeignKey(job, related_name='apply_job', on_delete=models.CASCADE)
     name = models.CharField(max_length=50)
     email = models.EmailField(max_length=100)
     website = models.URLField()
     cv = models.FileField(upload_to='apply/')
     cover_letter = models.TextField(max_length=500)
   


     def __str__(self):
         return self.name    

    