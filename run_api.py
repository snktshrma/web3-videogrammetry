import requests, json
import webbrowser, time, os, os.path

headers = {
    'accept': 'text/plain',
}

vidLoc = str(input("Enter video path: "))
tokenAPI = str(input("Enter api token: "))

vid = vidLoc

api = tokenAPI

files = {
    'file': open(vid, 'rb'),
    'scanQuality': (None, 'Full'),
    'featureSensitivity': (None, 'Normal'),
    'sampleOrdering': (None, 'Sequential'),
    'isObjectMaskingEnabled': (None, ''),
}

print("Uploading...")
response = requests.post('https://api2.spectre3d.io/Scan', headers=headers, files=files)

dta = response.text
main = json.loads(dta)
print("Done Uploading")

print("ID: ", main["id"])


mid = str(main["id"])

url = f"https://api2.spectre3d.io/Scan/{mid}"

response = requests.get(url, headers=headers)

dta = response.text
main = json.loads(dta)

stats = main["jobStatus"]

if main["errorMessage"] == "":
	print("Processing...")
	while stats != "Completed":
		response = requests.get(url, headers=headers)
		dta = response.text
		main = json.loads(dta)
		stats = main["jobStatus"]
		time.sleep(10)
else:
	print(main["errorMessage"])
	
print("Done processing")
print(main["glbUrl"])

webbrowser.open(main["glbUrl"])

link = main["glbUrl"]
newLink = link.split("/")[-1]

cmd = f"node ./web3_storage/web3-client.js --token={api} ~/Downloads/{newLink}"

print("Waiting for download..")
while not os.path.exists(f"~/Downloads/{newLink}"):
	time.sleep(5)
	continue

os.system(cmd)




