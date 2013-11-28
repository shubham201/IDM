import threading
class Download_object:
	download_id = 0 
	def __init__(self, url, noOfThreads):
		if(Download_object.download_id<2999):
			self.download_id += 1
		else:
			self.download_id = 0
		self.url = url
		self.current_size = 0
		self.size = 0
		self.paused = 0
		self.noOfThreads = noOfThreads
		self.data = []
		self.pausedFileName = 'none'
		for i in range(self.noOfThreads):
			self.data.append(None)
		self.thread_list = []

		'''
			d_obsect_fields : [url, size, current_size, paused, noOfThreads, data, pausedFileName, fileName, thread_list]
		'''

