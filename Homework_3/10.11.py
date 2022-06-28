# 1792816 Anthony Flores 10.11


class FoodItem:
    def __init__(self, name='None', fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == '__main__':
    name = input()
    fat = float(input())
    carbs = float(input())
    protein = float(input())
    num_servings = float(input())

    food1 = FoodItem()
    food1.print_info()
    print('Number of calories for', "{:.2f}".format(num_servings), 'serving(s):',
          "{:.2f}".format(food1.get_calories(num_servings)))
    print()

    food2 = FoodItem(name, fat, carbs, protein)
    food2.print_info()
    print('Number of calories for', "{:.2f}".format(num_servings), 'serving(s):',
          "{:.2f}".format(food2.get_calories(num_servings)))
