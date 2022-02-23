import requests


def add_pet(new_pet):
    return requests.post('https://petstore.swagger.io/v2/pet', json=new_pet)


def find_pet(pet_id):
    return requests.get(f'https://petstore.swagger.io/v2/pet/{pet_id}')


def update_name(new_name):
    return requests.put(f'https://petstore.swagger.io/v2/pet/', json=new_name)

