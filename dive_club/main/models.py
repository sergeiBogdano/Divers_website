from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone_number = models.CharField(
        max_length=15,
        verbose_name='Номер телефона'
    )
    email = models.EmailField(verbose_name='Электронная почта')
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return f"{self.name} - {self.phone_number}"

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class HomePageContent(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контент главной страницы'
        verbose_name_plural = 'Контент главной страницы'


class HomePageImage(models.Model):
    content = models.ForeignKey(
        HomePageContent,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name='Контент'
    )
    image = models.ImageField(
        upload_to='home_images/',
        verbose_name='Изображение'
    )
    caption = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Подпись'
    )

    def __str__(self):
        return self.caption or "Без подписи"

    class Meta:
        verbose_name = 'Изображение главной страницы'
        verbose_name_plural = 'Изображения главной страницы'


class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(
        upload_to='service_images/',
        blank=True,
        null=True,
        verbose_name='Изображение'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class AboutPageContent(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контент страницы "О нас"'
        verbose_name_plural = 'Контент страницы "О нас"'


class AboutPageImage(models.Model):
    content = models.ForeignKey(
        AboutPageContent,
        related_name='aboutpage_images',
        on_delete=models.CASCADE,
        verbose_name='Контент'
    )
    image = models.ImageField(
        upload_to='about_images/',
        verbose_name='Изображение'
    )
    caption = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Подпись'
    )

    def __str__(self):
        return self.caption or "Без подписи"

    class Meta:
        verbose_name = 'Изображение страницы "О нас"'
        verbose_name_plural = 'Изображения страницы "О нас"'


class Image(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    caption = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Подпись'
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата загрузки'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
