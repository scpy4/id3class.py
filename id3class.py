#Class script for checking mp3 tags
#call the mp3 file, for now we are specifing the file path

from mutagen.mp3 import MP3

class id3val():
	
	'''
	Class to link the different ID3 tags to a file path that will
	then extract the metadata and print out the song title, album,
	artist, length and bitrate.
	'''
	
	def __init__(self, song):
		try:
			self.song = song
			self.old_file_name = self.song["TIT2"]
			print(self.old_file_name)
		except:
			print ("Sorry Cannot find song title")
			
		try:
			self.artist = self.song["TPE1"]
			print(self.artist)
		except:
			print ("Sorry cannot find Artist")
			
		try:
			self.album = self.song["TALB"]
			print(self.album)
		except:
			print ("Sorry cannnot find Album name")
			
			
		#get the length of the track, divide by 60 to get minutes
		length = path.info.length/ 60
		print length, "minutes"
		
		
		#get the bitrate, divide by 1000 to get kbps
		bitrate = path.info.bitrate / 1000
		print bitrate, "kbps"

	
path = MP3("/home/davidlee/Music/Chase & Status - Blind Faith.mp3")
val = id3val(path)
