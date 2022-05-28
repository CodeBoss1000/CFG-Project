
import requests


def recipe_search(ingredient, health):
    app_id = ''
    app_key = ''
    result = requests.get(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}&health={}'.format(ingredient, app_id, app_key, health))
    data = result.json()
    return data['hits']


def run():

    ingredient = input('Enter an ingredient: ')
    health = input('Optional dietary requirement: vegan, vegetarian, pescatarian, paleo: ')
    results = recipe_search(ingredient, health)

    # file name  data_file located here
    file = 'data_file.txt'

    # file will open here
    userfile = open(file,'w+')

    for result in results:
        recipe = result['recipe']
        print('____________________________________________________________________________________')
        print(recipe['label'])
        print(recipe['shareAs'])
        print(recipe['ingredientLines'])

        userfile.write(recipe['label']+'\n')
        userfile.write(recipe['shareAs'] + '\n')
    userfile.close()

# ask the user if they would like to continue using the program yes/no. Based on the users choice, the if statement will
# print an appropriate statement based on their input.

    ingredient = input('Would you like to continue your search yes or no? ')
    if ingredient == 'yes':
        print('please refresh to continue your search.')
        print('We will save your results should you wish to keep it')
    else:
        print('Thank you for using this program!')
        print('Your results will be saved by default, please feel to delete if you do not require it')


run()
