from django.db import models

# Create your models here.
# тут создаем модели которые будут в базе данных, которые можно будет потом создавать из админки
class Project(models.Model):
    # ставим ограничение на ввод текста в виде 100 символов
    title = models.CharField(max_length=100) # заголовок
    description = models.CharField(max_length=250) # содержание
    image = models.ImageField(upload_to='portfolio/images') # картинка
    url = models.URLField(blank=True) # адрес (может быть пустым)

    # эта функция позволит отображать своим имена в панеле администратора, а не имена project 1, project 2
    def __str__(self):
        return self.title