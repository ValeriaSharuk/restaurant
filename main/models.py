from django.db import models


class AboutInfo(models.Model):
    title = models.CharField('Название компании', max_length=50)
    full_text = models.TextField('Информация о компании')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'О компании'


class Dish(models.Model):
    title = models.CharField("Название", max_length=50)
    description = models.TextField("Описание")
    price = models.CharField("Цена", max_length=10, default='')
    image = models.ImageField("Изображение", upload_to="dishes/")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'{self.id}'

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"


class ContactsInfo(models.Model):
    num_tel = models.CharField('Номер телефона', max_length=30)
    email_comp = models.CharField('email компании', max_length=30)
    address_comp = models.CharField('Адрес компании', max_length=250)

    def __str__(self):
        return self.num_tel

    def get_absolute_url(self):
        return f'/comp_about/{self.id}'

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class FeedbackInfo(models.Model):
    full_name = models.CharField('Имя человека, оставившего отзыв', max_length=30)
    full_text = models.TextField('Содержание отзыва')
    image = models.ImageField("Изображение", upload_to="people/")

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
