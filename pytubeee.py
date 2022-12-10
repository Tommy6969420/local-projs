import requests

url = "https://video-downloader4.p.rapidapi.com/grab"

payload = {"link": "https://www.tiktok.com/@fasishahphotography/video/7111361223219858714"}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "video-downloader4.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)