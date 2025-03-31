basket=['apple','guava','cherry','banana']
my_fruits =['apple','kiwi','grapes','banana']


#ass new list from my_fruits and items if the fruits exists in basket and also starts with 'a'.

print([fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')])