#  pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  

def upload_drive(name_file_path):

	file_name = [name_file_path]
	for upload_file in file_name:
		gfile = drive.CreateFile({'parents': [{'id': '1MRn4ji-tJcob4Wz8G1iVP6mb6kvyaIso'}]})
		# Read file and set it as the content of this instance.
		gfile.SetContentFile(upload_file)
		gfile.Upload() # Upload the file.

	return name_file_path	

def upload_drive_excel(name_file_path):
    
	file_name = [name_file_path]
	for upload_file in file_name:
		gfile = drive.CreateFile({'parents': [{'id': '1iJh3cx4pup_bT2qNXVksosMdXe_lCJlx'}]})
		# Read file and set it as the content of this instance.
		gfile.SetContentFile(upload_file)
		gfile.Upload() # Upload the file.

	return name_file_path	

def delete_file(name_file_path):
    	
	fileList = drive.ListFile({'q': "'1iJh3cx4pup_bT2qNXVksosMdXe_lCJlx' in parents and trashed=false"}).GetList()
	for file in fileList:
		print('Title: %s, ID: %s' % (file['title'], file['id']))

		# Get the folder ID that you want
		if(file['title'] == name_file_path):
			fileID = file['id']
	
	# Initialize GoogleDriveFile instance with file id.
	file2 = drive.CreateFile({'id': fileID})
	#file2.Trash()  # Move file to trash.
	#file2.UnTrash()  # Move file out of trash.
	file2.Delete()  # Permanently delete the file.   

def upload_and_delete(name_file_path):

	try: #if yes run
		fileList = drive.ListFile({'q': "'1iJh3cx4pup_bT2qNXVksosMdXe_lCJlx' in parents and trashed=false"}).GetList()
		for file in fileList:
			print('Title: %s, ID: %s' % (file['title'], file['id']))

			# Get the folder ID that you want
			if(file['title'] == name_file_path):
				fileID = file['id']
		
		# Initialize GoogleDriveFile instance with file id.
		file2 = drive.CreateFile({'id': fileID})
		#file2.Trash()  # Move file to trash.
		#file2.UnTrash()  # Move file out of trash.  	
		file2.Delete()

		x = 2/0 #next error

	except: #if error run
		#upload_drive(name_file_path)
		file_name = [name_file_path]
		for upload_file in file_name:
			gfile = drive.CreateFile({'parents': [{'id': '1iJh3cx4pup_bT2qNXVksosMdXe_lCJlx'}]})
			# Read file and set it as the content of this instance.
			gfile.SetContentFile(upload_file)
			gfile.Upload() # Upload the file.		
		#print(2)	

#upload_drive('Golfkub.jpg')
#upload_and_delete('data_mask.xlsx')
