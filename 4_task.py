my_family = ['Кристина', 'Вася', 'Тедди', 'Свят']

kris = my_family[0]
dfcz = my_family[1]
teddy = my_family[2]
svyat777 = my_family[3]

my_family_height = [
    [kris, 170],
    [dfcz, 50],
    [teddy, 100],
    [svyat777, 175]
]

print('Рост', kris, my_family_height[0][1], 'см')
print('Рост', dfcz, my_family_height[1][1], 'см')
print('Рост', teddy, my_family_height[2][1], 'см')
print('Рост', svyat777, my_family_height[3][1], 'см')

kris_tall = my_family_height[0][1]
dfcz_tall = my_family_height[1][1]
teddy_tall = my_family_height[2][1]
svyat777_tall = my_family_height[3][1]

print('Общий рост моей семьи', kris_tall + dfcz_tall + teddy_tall + svyat777_tall, 'см')
