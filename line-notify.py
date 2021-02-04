import requests, json
import urllib.parse
import sys

LINE_ACCESS_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
URL_LINE = "https://notify-api.line.me/api/notify" 

def sendMessage(message):	
    msg = urllib.parse.urlencode({"message":message})
    LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
    session = requests.Session()
    session_post = session.post(URL_LINE, headers=LINE_HEADERS, data=msg)
    print(session_post.text)

def sendImage(message, path_file):
    file_img = {'imageFile': open(path_file, 'rb')}
    msg = ({'message': message})
    LINE_HEADERS = {"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
    session = requests.Session()
    session_post = session.post(URL_LINE, headers=LINE_HEADERS, files=file_img, data=msg)
    print(session_post.text)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        # python3 line-notify.py "Hi man"
        sendMessage(sys.argv[1])
    else:
        # python3 line-notify.py "Test Send Image" "/Users/x-c0d3/Desktop/test.png"
        sendImage(sys.argv[1], sys.argv[2])