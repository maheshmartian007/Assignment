from django.shortcuts import render
from django.views.generic import View
from testapp.models import Player
from django.http import HttpResponse
import json
from django.core.serializers import serialize
from testapp.mixins import *

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from testapp.utils import is_valid_json_data
from testapp.forms import PlayerForm


@method_decorator(csrf_exempt,name='dispatch')
class PlayerCRUDCbv(View,SerializeMixin,HttpMixinResponse):
	'''
		This class extends View and HttpMixinResponse

		It is developed by Mr Sandesh to Perform CRUD operation by satisfying Single End Point
	
	'''

	def get_object_data_by_id(self,id):
		'''
		This function will fetch the record[data] present within DB using id
		'''
		try:
			player = Player.objects.get(id=id)
		except Player.DoesNotExist:
			player = None
		return player


	def get(self,request,*args,**kwargs):
		'''
		This function is used to fetch the data from the DB
		'''
		data = request.body
		#checking whether the data is Json or not
		valid_json_data = is_valid_json_data(data)

		if not valid_json_data:
			json_data = json.dumps({'msg':'Please send the valid json data'})
			return self.render_to_http_response(json_data,status=400)

		#converting Json data into Dictionary
		provided_data = json.loads(data)

		id = provided_data.get('id',None)
		if id is not None:
			player= self.get_object_data_by_id(id)
			if player is None:
				json_data = json.dumps({'msg':'The required Player data is not available'})
				return self.render_to_http_response(json_data,status=404)
			json_data = self.serialize([player,])
			return self.render_to_http_response(json_data)

		#if the id is None
		query_string = Player.objects.all()
		json_data = self.serialize(query_string)
		return self.render_to_http_response(json_data)

	def post(self,request,*args,**kwargs):
		'''
		This function is used to inster the data into the DB
		'''
		data = request.body
		valid_json_data = is_valid_json_data(data)
		if not valid_json_data: 
			json_data = json.dumps({'msg':'Please Provide the Valid Json Data'})
			return self.render_to_http_response(json_data,status=400)

		provided_data = json.loads(data)
		print(provided_data)
		print(type(provided_data))

		form = PlayerForm(provided_data)
		print(form)
		print(type(form))

		if form.is_valid():
			form.save(commit=True)
			json_data = json.dumps({'msg' : 'The data is Valid ,Player Data got created'})
			return self.render_to_http_response(json_data)

		if form.errors:
			json_data = json.dumps(form.errors)
			return self.render_to_http_response(json_data,status=400)


	def put(self,request,*args,**kwargs):
		'''
		This function is used to update the data in the DB
		'''

		data = request.body
		valid_json_data = is_valid_json_data(data)
		if not valid_json_data: 
			json_data = json.dumps({'msg':'Please Provide the Valid Json Data'})
			return self.render_to_http_response(json_data,status=400)

		#This is the data coming from Python application inorder to update
		provided_data = json.loads(data)

		id=provided_data.get('id',None)

		if id is None:
			json_data=json.dumps({'msg':'To perform Updation id is mandatory....Please Provide the id'})
			return self.render_to_http_response(json_data,status=400)

		player=self.get_object_data_by_id(id)

		if player is None:
			json_data = json.dumps({'msg':'The required player data is not available'})
			return self.render_to_http_response(json_data,status=404)

		#this is the data which is been stored within the database
		original_data = {'jersyno':player.jersyno,'name':player.name,'age':player.age,'iplteam':player.iplteam}
		
		print('Data before Updation')
		print(original_data)

		print('Data After updation')
		#Performing updation on the existing original data
		original_data.update(provided_data)
		print(original_data)

		form = PlayerForm(original_data,instance=player)
		if form.is_valid():
			form.save(commit=True)
			json_data = json.dumps({'msg':'PlayerData Updated successfully'})
			return self.render_to_http_response(json_data)

		if form.errors:
			json_data = json.dumps(form.errors)
			return self.render_to_http_response(json_data,status=400)


	def delete(self,request,*args,**kwargs):
		'''
		This function is used to delete the data from the DB
		'''
		data = request.body
		valid_json_data = is_valid_json_data(data)
		if not valid_json_data:
			json_data=json.dumps({'msg':'Please send the valid json data'})
			return self.render_to_http_response(json_data,status=400)

		#This is the data coming from Python application inorder to delete
		provided_data = json.loads(data)

		id = provided_data.get('id',None)

		if id is not None:
			player = self.get_object_data_by_id(id)
			if player is None:
				json_data = json.dumps({'msg':'No matched player data found, updation not possible'})
				return self.render_to_http_response(json_data,status=404)
			
			(status,deleted_item) = player.delete()

			if status == 1:
				json_data=json.dumps({'msg':'Player data deleted successfully'})
				return self.render_to_http_response(json_data)

			json_data=json.dumps({'msg':'Player data not deleted successfully'})
			return self.render_to_http_response(json_data)

		json_data=json.dumps({'msg':'To perform Deletion id is mandatory....Please Provide the id'})
		return self.render_to_http_response(json_data,status=400)


		