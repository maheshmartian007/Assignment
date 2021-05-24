import requests
import json

BASE_URL='http://127.0.0.1:8000/'
END_POINT='api/'



def get_resource(id=None):

	data = {}
	if id is not None:
		data  = {'id':id}

	response=requests.get(BASE_URL+END_POINT,data = json.dumps(data))
	print(response.status_code)
	print(response.json())

# get_resource()

def get_resource(id=None):

	data = {}
	if id is not None:
		data  = {'id':id}

	response=requests.get(BASE_URL+END_POINT,data = json.dumps(data))
	print(response.status_code)
	print(response.json())


# id = input('Enter the ID:\t')
# get_resource(id)



def create_resource():
	jersyno = int(input('Enter the Jersey number:\t'))
	name = input('Enter the Name of the Player:\t')
	age = int(input('Enter the age of the Player:\t'))
	iplteam = input('Enter the iplteam of the Player:\t')
	player_data = {'jersyno':jersyno,'name':name,'age':age,'iplteam':iplteam}

	response = requests.post(BASE_URL+END_POINT,data=json.dumps(player_data))
	print(response.status_code)
	print(response.json())

# create_resource()

def update_resource_completely(id):
	jersyno = int(input('Enter the Jersey number:\t'))
	name = input('Enter the Name of the Player:\t')
	age = int(input('Enter the age of the Player:\t'))
	iplteam = input('Enter the iplteam of the Player:\t')
	player_data = {'id':id,'jersyno':jersyno,'name':name,'age':age,'iplteam':iplteam}
	
	response = requests.put(BASE_URL+END_POINT,data=json.dumps(player_data))
	print(response.json())
	print(response.status_code)

# update_resource(2)
# def update_resourse_partially(id):
# 	num = int(input('How many details need to update:\t'))
# 	player_data = {'id':id,'jersyno':jersyno,'name':name,'age':age,'iplteam':iplteam}
# 	for i in range(num):
# 		fieldname = int(input('Enter the age of the Player:\t'))
# 		update_data={'id':id,'age':age,'iplteam': iplteam, }
	
# 	response = requests.put(BASE_URL+END_POINT,data=json.dumps(update_data))
# 	print(response.json())
# 	print(response.status_code)


def delete_resource(id):
	data={'id':id}
	response = requests.delete(BASE_URL+END_POINT,data=json.dumps(data))
	print(response.json())
	print(response.status_code)

# delete_resource(2)

print('Please select the below operations \n 1. CREATE the data \n 2. SELECT Single data \n 3. SELECT Complete data \n 4. UPDATE completely \n 5. UPDATE Partially \n 6. DELETE the data'
)

option = int(input('Enter the option:\t'))

def select_option():

	if option == 1:
		return create_resource()

	elif option == 2:
		id = input('Enter the ID:\t')
		return get_resource(id)

	elif option == 3:
		return get_resource()

	elif option == 4:
		id = input('Enter the ID to update:\t')
		return update_resource_completely(id)

	elif option == 5:
		return None

	elif option == 6:
		id = input('Enter the ID to delete:\t')
		return delete_resource(id)

select_option()



