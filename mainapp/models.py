from django.db import models

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 120)
    postdate = models.DateTimeField(auto_now_add = True)
    upddate = models.DateTimeField(auto_now=True)
    text = models.TextField()
    image = models.ImageField(upload_to='posts/images/', null=True, blank=True)
    def get_absolute_url(self):
        return f"/blog/{self.id}/"

class livechat(models.Model):
    id = models.AutoField(primary_key=True)

class message(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length = 20) 
    date =  models.DateTimeField(auto_now_add = True, null=True, blank=True)
    text = models.TextField()
    class meta: 
        ordering = ['date']
    #chat = models.ForeignKey(livechat, verbose_name = "чат", on_delete = models.CASCADE)
    #модель чат не нужна на данный момент, можно удалять в будущем
