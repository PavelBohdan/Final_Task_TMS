from tools.http_steps import add_pet, find_pet, update_name
import allure


@allure.story('Check new pet can be added')
def test_add_pet():
    """Этот тест добавляет нового питомца в магазин"""
    with allure.step('Add new pet'):
        new_pet = {
            'id': 5,
            'name': 'zoro'
        }
        response = add_pet(new_pet)
    with allure.step('Check new pet had been added'):
        assert response.status_code == 200, 'wrong status code'
        assert 'zoro' in response.text, 'no such pet name'


@allure.story('Check added pet can be found')
def test_find_pet():
    """Этот тест проверяет по Name добавлен ли питомец"""
    with allure.step('Add new pet'):
        new_pet = {
            'id': 5,
            'name': 'zoro'
        }
        add_pet(new_pet)
    with allure.step('Find added pet'):
        pet_id = 5
        response = find_pet(pet_id)
    with allure.step('Check pet had been found by name'):
        assert response.status_code == 200, 'wrong status code'
        assert 'zoro' in response.text, 'no such pet name'


@allure.story('Check pet name can be updated')
def test_update_name():
    """С помощью этого теста обновляем данные питомцу (name)"""
    with allure.step('Add new pet'):
        new_pet = {
            'id': 5,
            'name': 'zoro'
        }
        add_pet(new_pet)
    with allure.step('Change name of existing pet'):
        new_name = {
            'pet_id': 5,
            'name': 'morti'
        }
    response = update_name(new_name)
    with allure.step('Check name of existing pet had been updated'):
        assert response.status_code == 200, 'wrong status code'
        assert 'morti' in response.text, 'not found'

@allure.story('Check updated pet name can been found using pet id')
def test_update_check():
    """Этот тест проверяет по Id, что имя (name) обновлено"""
    with allure.step('Add new pet'):
        new_pet = {
             'id': '5',
             'name': 'zoro'
        }
        add_pet(new_pet)
    with allure.step('Change name of existing pet'):
        new_name = {
             'pet_id':'5',
             'name': 'morti'
        }
        update_name(new_name)
    with allure.step('Find updated pet name by pet Id'):
        pet_id='5'
        response=find_pet(pet_id)
    with allure.step('Check updated pet name has been found'):
        assert response.status_code == 200, 'wrong status code'
        assert '5' in response.text, 'no such pet id'