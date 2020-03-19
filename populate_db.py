import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exotic_bay_project.settings')

django.setup()

from exotic_bay.models import Pet
import datetime


def populate():
    pets = {'Mexican Red Knee':
                {'scientificName': 'Brachypelma hamorii (ex smithi)',
                 'price': 35,
                 'type': 'Inverts',
                 'stock': 1000,
                 'description': 'Mexican Red Knee is a popular choice for beginners and enthusiasts alike.  Like most '
                                'tarantulas, it has a long lifespan.',
                 'careDetails': 'This spider needs to be kept in a terrestial style plastic faunarium or suitable '
                                'glass enclosure.',
                 'orders': 0,
                 'dateAdded': datetime.date(2020, 2, 4),
                 'image': 'pet_images/mexican-red-knee.jpg'},

            'Panther Chameleon':
                {'scientificName': 'Furcifer pardalis',
                 'price': '40',
                 'type': 'Reptiles',
                 'stock': 439,
                 'description': 'The Panther Chameleon, being one of the easiest species of Chameleon to own makes '
                                'them a favourite among lizard owners.',
                 'careDetails': 'This breed of Chameleon is incredibly territorial and usually should be housed '
                                'individually in a mesh enclosure. ',
                 'orders': 0,
                 'dateAdded': datetime.date(2020, 3, 9),
                 'image': 'pet_images/panther-chameleon.jpg'},

            'Bearded Dragon':
                {'scientificName': 'Pogona vitticeps',
                 'price': '50',
                 'type': 'Reptiles',
                 'stock': 6000,
                 'description': 'Bearded Dragons are the most popular pet lizard, naturally found only throughout '
                                'Australia. They are a large species growing to a total length of 15-24 inches when '
                                'adult.',
                 'careDetails': 'As a native of Australia, bearded dragon lizards need to be kept in a hot, '
                                'dry environment. Bearded dragons like to spend part of their day '
                                'basking'' at high temperatures to warm their body. Once up to temperature, they will '
                                'often move to '
                                'cooler areas. Whilst basking, bearded dragons also absorb strong UVB from the sun '
                                'which enables them to produce vitamin D in their body which is essential for '
                                'utilising calcium. '
                                '\nThe bearded dragon diet is omnivorous which means that they eat both animals and '
                                'vegetation. Bearded dragons are particularly fond of insects and worms, '
                                'but can tackle larger prey if they wish! As adults, bearded dragons are 80% '
                                'vegetarian.',
                 'orders': 0,
                 'dateAdded': datetime.date(2020, 3, 19),
                 'image': 'pet_images/bearded-dragon.jpg'},

            'Axolotl':
                {'scientificName': 'Ambystoma mexicanum',
                 'price': '40',
                 'type': 'Amphibians',
                 'stock': 50,
                 'description': 'Axolotls are large aquatic salamanders only found in parts of Mexico. They are easy '
                                'to keep and grow to an impressive 30cm, making the Axolotl a popular exotic pet.',
                 'careDetails': 'A good set up for one Axolotl would consist of an aquarium of 60 x38 x30cm (24 x 15 '
                                'x 12in). The water should be around 10-20 C (50-68 F) and shallow, as deep as the '
                                'Axolotl is long. Decorate the aquarium with a mixture of plastic plants and '
                                'oxygenating plant, with maybe a couple of large pebbles. \n\nHowever, do not over crowd '
                                'your set up - make sure your Axolotl has plenty of space. Keep your set-up out of '
                                'direct light as Axolotls do not have eyelids and are sensitive to too much light. ',
                 'orders': 0,
                 'dateAdded': datetime.date(2020, 1, 5),
                 'image': 'pet_images/axolotl.jpg'},

            'Sugar Glider':
                {'scientificName': 'Petaurus breviceps',
                 'price': '150',
                 'type': 'Marsupials',
                 'stock': 150,
                 'description': 'Sugar Gliders are small marsupials in the same general family as a Kangaroo or '
                                'Koala Bear. They are originally from the rainforests of Australia and Indonesia, '
                                'and have been domestically bred as household pets for the last 12-15 years.',
                 'careDetails': 'Sugar gliders should be housed in as large a cage as possible to enable them to '
                                'jump, leap, and glide around. Minimum size cage requirements for a single glider are '
                                '3’ x 2’ x 3’. Securely locked, metal cages with bar spacing no more than 0.5” apart '
                                'are best, as sugar gliders are notorious escape artists. They should be allowed out '
                                'of their cages daily for exercise but only when closely supervised, as their curious '
                                'nature tends to get them into trouble.',
                 'orders': 0,
                 'dateAdded': datetime.date(2020, 3, 16),
                 'image': 'pet_images/sugar-glider.jpg'},

            'Fennec Fox':
                {'scientificName': 'Vulpes zerda',
                 'price': '1500',
                 'type': 'Canidae',
                 'stock': 10,
                 'description': 'The fennec fox, also called fennec or desert fox, is a small crepuscular fox native '
                                'to the Sahara Desert, the Sinai Peninsula, Arava desert and the Arabian desert. Its '
                                'most distinctive feature is its unusually large ears, which also serve to dissipate '
                                'heat.',
                 'careDetails': 'Fennecs are very active and need an outlet for their energy. They are curious and '
                                'will get into anything and everything. They are also known for their digging. '
                                'Outdoor enclosures must be designed to prevent them from digging under or climbing '
                                'over the fence, both of which they will do quite readily. '
                                '\n\nBurying a significant portion of the fence and turning the fence in at the top (or '
                                'completely covering the enclosure) should prevent escape. Don''t skimp on materials, '
                                'though, because these foxes can dig holes up to (or down to) 20 feet deep if they''re feeling motivated.',
                 'orders': 0,
                 'dateAdded': datetime.date(2020, 1, 1),
                 'image': 'pet_images/fennec-fox.jpg'},

            'Blue Poison Dart Frog':
                {'scientificName': 'Dendrobates tinctorius azureus',
                 'price': '95',
                 'type': 'Amphibians',
                 'stock': 420,
                 'description': 'Bright blue animals are a rarity in nature and this species is unquestionably one of '
                                'the most spectacular. Few dart frog collections exist without Blue Poison Dart Frogs '
                                'being present; a must for any serious keeper.',
                 'careDetails': 'House this species singularly, in sexed pairs or sexed trios of (2.1). Upon '
                                'maturity, females can be aggressive towards one another, so it usually best to house '
                                'one female per enclosure. However, if enough space is provided they will often form '
                                'their own territories. Provide a glass terrarium of at least 45 x 45 x 45cm (18 x 18 '
                                'x 18”) to house an adult sexed pair, and larger, if there are more of them. Young '
                                'frogs can be reared in plastic terrariums or smaller glass enclosures.',
                 'orders': 0,
                 'dateAdded': datetime.date(2020, 3, 20),
                 'image': 'pet_images/blue-poison-dart-frog.jpg'},
            }

    # If you want to add more categories or pages,
    # add them to the dictionaries above.

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    for pet, pet_data in pets.items():
        p = add_pet(pet, pet_data['scientificName'], pet_data['price'], pet_data['type'], pet_data['stock'],
                    pet_data['description'], pet_data['careDetails'], pet_data['dateAdded'], pet_data['orders'],
                    pet_data['image'])

    # Print out the categories we have added.
    for p in Pet.objects.all():
        print(f'- {p}')


def add_pet(name, scientificName, price, petType, stock, description, careDetails, dateAdded, orders=0, image=None):
    pet = Pet.objects.get_or_create(name=name)[0]
    pet.scientificName = scientificName
    pet.price = price
    pet.type = petType
    pet.stock = stock
    pet.description = description
    pet.careDetails = careDetails
    pet.orders = orders
    pet.date_added = dateAdded
    pet.image = image
    pet.save()
    return pet


# Start execution here!
if __name__ == '__main__':
    print('Starting Exotic-Bay population script...')
    populate()
