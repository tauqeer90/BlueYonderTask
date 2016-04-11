import urllib
import thread

"""
Function for downloading images and save in local drive.
"""
def download_image(url, save_path):
    url_string = ''.join(url)
    filename = get_filename_from_url(url)
    save_path += filename
    urllib.urlretrieve(url, save_path)

"""
Function for extracting file name from url.
"""
def get_filename_from_url(url):
	url_components = url.split("/")
	url_length = len(url_components)
	filename = url_components[url_length - 1:url_length]
	return(filename[0].strip())

# Absolute Location of text file in disk, containing urls.
textfile = "E:/blueyonder/links.txt"

# list containing urls of images to be downloaded.
url_list = None
with open(textfile) as urls:
	url_list = urls.readlines()

# Location where the downloaded images are to be saved.
save_path_image = "E:/blueyonder/"
for url in url_list:
    
    # Downloading each image in a background thread.
    try:
        thread.start_new_thread(download_image, (url, save_path_image))
    except:
        print "Error: unable to download image from url " + url
