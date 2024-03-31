import json
from django.core.management import BaseCommand
from django.db import connection
from catalog.models import Product, Category, Contact
from config.settings import BASE_DIR


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        """Получение данных категорий из фикстуры"""
        with open(f'{BASE_DIR}/fixtures/catalog_data.json', encoding='UTF-8') as file:
            data = json.load(file)
        list_category = []
        for category in data:
            if 'category' in category['model']:
                list_category.append(category)
        return list_category

    @staticmethod
    def json_read_products():
        """Получение данных продуктов из фикстуры"""
        with open(f'{BASE_DIR}/fixtures/catalog_data.json', encoding='UTF-8') as file:
            data = json.load(file)
        list_product = []
        for product in data:
            if 'product' in product['model']:
                list_product.append(product)
        return list_product

    @staticmethod
    def json_read_contacts():
        """Получение контактов из фикстуры"""
        with open(f'{BASE_DIR}/fixtures/catalog_data.json', encoding='UTF-8') as file:
            data = json.load(file)
        list_contact = []
        for contact in data:
            if 'contact' in contact['model']:
                list_contact.append(contact)
        return list_contact

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        Contact.objects.all().delete()

        with connection.cursor() as cursor:
            cursor.execute(
                "TRUNCATE TABLE catalog_category, catalog_product, catalog_contact RESTART IDENTITY CASCADE;")

        category_for_create = []
        product_for_create = []
        contact_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(Category(pk=category['pk'],
                                                name=category['fields']['name'],
                                                description=category['fields']['description']))

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(Product(pk=product['pk'],
                                              name=product['fields']['name'],
                                              description=product['fields']['description'],
                                              image=product['fields']['image'],
                                              category=Category.objects.get(pk=product['fields']['category']),
                                              price=product['fields']['price'],
                                              created_at=product['fields']['created_at'],
                                              updated_at=product['fields']['updated_at']))

        Product.objects.bulk_create(product_for_create)

        for contact in Command.json_read_contacts():
            contact_for_create.append(Contact(pk=contact['pk'],
                                              country=contact['fields']['country'],
                                              city=contact['fields']['city'],
                                              address=contact['fields']['address'],
                                              ein=contact['fields']['ein']))

        Contact.objects.bulk_create(contact_for_create)
