from django.db import models
# Create your models here.


# 问题
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question_text  # 这里也能返回其他的字段，就是在使用该模型查询的时候返回的字段的值


# 选项
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    """
    在创建多对一关系的时候,需要在ForeignKey方法的第二个参数中加入            
    on_delete=models.CASCADE。这个参数的作用是主外关系键中的级联删除，也就是当删除主表数据的时候，从表中的数据也随着一起删除
    """
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text
