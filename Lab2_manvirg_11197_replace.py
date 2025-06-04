'''Lab2_manvirg_11197_replace by Manvir Goraya on 05/02/25.
The purpose of this program is to take the modified list from Lab2_manvirg_11197_add and replace one of the strings with Binoculars'''

import Lab2_manvirg_11197_add

supplies = Lab2_manvirg_11197_add.supplies
index = supplies.index('Pot')
supplies[index] = 'Binoculars'

print (supplies)