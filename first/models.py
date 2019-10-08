from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=15, blank=True, null=True)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=15, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               related_name="Author")
    upvoted_by = models.ManyToManyField(Author)

    def __str__(self):
        return self.title


class Score(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.author.name
