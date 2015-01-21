__author__ = 'tecnoman5000'

from random import randint


first_names = ['Luke','Reva','Orpha','Louann','Cherise','Lai','Hope','Vanessa','Adam','Velda',
		 'Darrell','Michael','Evia','Stanton','Rowena','Lucrecia','Eufemia','Karma','Maire','Eleanore']
last_names = ['Whetzel','Hooley','Ratchford','Ellison','Beaudreau','Dehn','Mathieson','Higginbotham','Mchenry',
			  'Huston','Felch','Authement','Denman','Luckow','Woldt','Milne','Voorhies','Richman','Stenzel','Brizendine']

street_names = ['Leora','Aleen','Ka','Tammera','Lacy','Rachelle','Minerva','Elenora','Martha','Sherryl']
street_sufix = ['st','crescent','rd','ave','dr',]

#payment_types = ['C.O.D','Smile','Veteran']

def cgen_main():
	sql_query = [phone_gen()]
	name = name_gen()
	sql_query.append(name[0])
	sql_query.append(name[1])
	sql_query.append(address_gen())
	defaults = defaults_gen()
	sql_query.append(defaults[0])
	sql_query.append(defaults[1])
	sql_query.append(defaults[2])
	print(sql_query)

	#with open(customer_gen, 'w+') as customer_gen_file:


def phone_gen():
	phone_number = '613'

	for num in range(0,7):
		phone_number += str(randint(0,9))
	return phone_number

def name_gen():
	first_name = first_names[randint(0,19)]
	last_name = last_names[randint(0,19)]
	return first_name,last_name

def address_gen():
	street_name = str(randint(1,500)) + ' ' + street_names[randint(0,9)] + ' ' + street_sufix[randint(0,4)]
	return street_name

def defaults_gen():
	payment_default = randint(1,3)
	if payment_default != 1:
		meal_default = randint(1,7)
		lock_meals = 1
		print('true')
	else:
		meal_default = 7
		lock_meals = 0

	return meal_default,payment_default,lock_meals


if __name__ == "__main__":
	cgen_main()