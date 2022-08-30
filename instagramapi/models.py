from django.db import models
from user.models import User

# Create your models here.


class InstaPost(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="post")
    caption = models.CharField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.caption

    @property
    def num_of_like(self):
        return LikePost.objects.filter(post=self).count()

    @property
    def num_of_comment(self):
        return Comment.objects.filter(post=self).count()


def upload_to(instance, filename):
    return 'image/{filename}'.format(filename=filename)

class ImageModel(models.Model):
    post = models.ForeignKey(InstaPost,on_delete=models.CASCADE,related_name="post_image")
    image_post= models.ImageField(upload_to=upload_to,default='image/default.jpg')
    created_at = models.DateTimeField(auto_now=True)



class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="post_comment")
    post = models.ForeignKey(InstaPost,on_delete=models.CASCADE,related_name="post_comment")
    comment = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment


class LikePost(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="like_post")
    post = models.ForeignKey(InstaPost,on_delete=models.CASCADE,related_name="like_post")
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user