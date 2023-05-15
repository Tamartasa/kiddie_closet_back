import os
import django
from django.db import IntegrityError
os.environ['DJANGO_SETTINGS_MODULE'] = 'kiddie_closet.settings'
django.setup()

from kiddie_closet_app.models import Category


def get_categories():
    # Open the text file containing the list of categories
    with open('categories.txt', 'r') as f:
        categories = f.readlines()

    # Loop over the categories and save each one to the database
    for category_name in categories:
        # Remove any whitespace characters (newline)
        category_name = category_name.strip()

        # Extract the category image URL from the category name
        category_parts = category_name.split(',')
        category_name = category_parts[0].strip()
        category_image_url = category_parts[1].strip() if len(category_parts) > 1 else None

        # get_or_create to avoid adding duplicate categories
        category, created = Category.objects.get_or_create(
            category_name=category_name,
            defaults={'category_image_url': category_image_url}
        )
        if created:
            print(f"Category {category_name} saved to database.")
        else:
            if category.category_image_url != category_image_url:
                category.category_image_url = category_image_url
                category.save()
                print(f"Category {category_name} updated in database.")
            else:
                print(f"Category {category_name} already exists in the database.")


print("Categories saved to database successfully")

if __name__ == '__main__':
    get_categories()


# import os
#
# import django
# from django.db import IntegrityError
# os.environ['DJANGO_SETTINGS_MODULE'] = 'kiddie_closet.settings'
#
# django.setup()
#
# from kiddie_closet_app.models import Category
#
#
# def get_categories():
#     # Open the text file containing the list of categories
#     with open('categories.txt', 'r') as f:
#         categories = f.readlines()
#
#     # Loop over the categories and save each one to the database
#     for category_name in categories:
#         # Remove any whitespace characters (newline)
#         category_name = category_name.strip()
#
#         # Use get_or_create to avoid adding duplicate categories
#         category, created = Category.objects.get_or_create(category_name=category_name)
#         if created:
#             print(f"Category {category_name} saved to database.")
#         else:
#             print(f"Category {category_name} already exists in the database.")
#
#     print("Categories saved to database successfully")
#
# if __name__ == '__main__':
#
#     get_categories()
