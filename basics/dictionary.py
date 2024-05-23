
#empty dictionary
alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

del alien_0['points']
print(alien_0)

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

for k, v in favorite_languages.items():
	print(v)

for name in favorite_languages.keys():  #also works with .values()
	print(name.title())


#use get
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)


