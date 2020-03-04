import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exotic_bay_project.settings')

django.setup()

from exotic_bay.models import Pet


def populate():
    pets = {'Mexican Red Knee':
                {'scientificName': 'Brachypelma hamorii (ex smithi)',
                 'price': 35,
                 'type': 'I',
                 'stock': 1000,
                 'description': 'Mexican Red Knee is a popular choice for beginners and enthusiasts alike.  Like most '
                                'tarantulas, it has a long lifespan.',
                 'careDetails': 'This spider needs to be kept in a terrestial style plastic faunarium or suitable '
                                'glass enclosure. ',
                 'orders': 0,
                 'image': 'pet_images/mexican-red-knee.jpg'}}

    # If you want to add more categories or pages,
    # add them to the dictionaries above.

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    for pet, pet_data in pets.items():
        p = add_pet(pet, pet_data['scientificName'], pet_data['price'], pet_data['type'], pet_data['stock'],
                    pet_data['description'], pet_data['careDetails'], pet_data['orders'], pet_data['image'])

    # Print out the categories we have added.
    for p in Pet.objects.all():
        print(f'- {p}')


def add_pet(name, scientificName, price, petType, stock, description, careDetails, orders=0, image=None):
    pet = Pet.objects.get_or_create(name=name)[0]
    pet.scientificName = scientificName
    pet.price = price
    pet.type = petType
    pet.stock = stock
    pet.description = description
    pet.careDetails = careDetails
    pet.orders = orders
    pet.image = image
    pet.save()
    return pet


# Start execution here!
if __name__ == '__main__':
    print('Starting Exotic-Bay population script...')
    populate()
