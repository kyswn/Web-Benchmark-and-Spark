import sys, random
from locust import HttpLocust, TaskSet

def readNode(locust):
	postid = random.randint(1, 500)
	url_prefix = '/blog/cs144/'
	name = '/blog/cs144'
	locust.client.get(url_prefix+str(postid),name = name )


class MyTaskSet(TaskSet):
	""" the class MyTaskSet inherits from the class TaskSet, defining the behavior of the user """
	tasks = {readNode}
	def on_start(locust):
		""" on_start is called when a Locust start before any task is scheduled """


class MyLocust(HttpLocust):
	""" the class MyLocust inherits from the class HttpLocust, representing an HTTP user """
	task_set = MyTaskSet
	min_wait = 1000
	max_wait = 2000