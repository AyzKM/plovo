from modeltranslation.translator import translator, TranslationOptions
from .models import Order, AdditionDish

class OrderTranslationOptions(TranslationOptions):
    fields = ('dish', 'status',)

class AdditionDishTranslationOptions(TranslationOptions):
    fields = ('dish',)

translator.register(Order, OrderTranslationOptions)
translator.register(AdditionDish, AdditionDishTranslationOptions)
