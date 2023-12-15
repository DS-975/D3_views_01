# from django.db import models
# from django.core.validatores import MinValueValidator
#
#
# # region todo: Модель представляет собой товар с полями такими как имя, количество, описание и так далее
# class Products(models.Model): # todo: Товары для нашей витрины
#     name = models.CharField(
#         max_length=50,
#         unique=True, # todo: <- название товаров не должно повторяться
#     )
#     description = models.TextField()
#     quantity = models.IntegerField(
#         validators=[MinValueValidator(0)],
#     )
#
#     # todo: Поле категории будет ссылаться на модель категории
#     category = models.ForeingnKey(
#         to='Category',
#         on_delete=models.CASCADE,
#         related_name='products', # todo: все продукты в категории будут доступны через поле products
#     )
#
#     def __str__(self):
#         return f'{self.name.title()}:{self.description[:20]}'
# # endregion
#
# # region todo: Модель представляет собой категорию товара, которая является первичным ключом к полю category у товара.
# class Category(models.Model): # todo: Категория, к которой будет привязываться товар
#
#     # todo: название категорий тоже не должны повторяться
#     name = models.CharField(max_length=100, unique=True)
#
#     def __str__(self):
#         return self.name.title()
# # endregion
