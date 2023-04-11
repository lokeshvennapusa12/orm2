from django.db import models

class Dept(models.Model):
    dept_no=models.IntegerField(primary_key=True)
    dept_name=models.CharField(max_length=100,unique=True)
    loc=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.dept_name



class EMP(models.Model):
    E_num=models.CharField(max_length=100)
    Ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    sal=models.IntegerField()
    dept_no=models.ForeignKey(Dept,on_delete=models.CASCADE)




