# import requests

# # API endpoint (replace with your actual backend URL)
# url = "http://203.174.22.14:8000/api/event/"

# # Path to the image you want to send
# image_path = "group_photo_1.jpg"

# # Optional extra data (device code, timestamp, etc.)
# payload = {
#     "device":"XYZ"
# }

# # Open the file in binary mode
# with open(image_path, "rb") as img:
#     files = {"image": img}
#     response = requests.post(url, data=payload, files=files)

# # Check response
# if response.status_code == 200 or response.status_code == 201:
#     print("✅ Upload successful")
#     print("Response:", response.json())
# else:
#     print("❌ Upload failed:", response.status_code)
#     print("Response:", response.text)


import requests

endpoint = "http://203.174.22.14:8000/api/"

data = requests.post(endpoint+"token/", data={"email":"piyush@gmail.com","password":"yogesh@bsdka"})

data = data.json()
access_token = data['access']
# # files = [
# #     ("images", ("img1.jpg", open("C:\\Users\\piyus\\Downloads\\Photoz\\23EBUCS067\\IMG_20250915_111046.jpg", "rb"), "image/jpeg")),
# #     ("images", ("img2.jpg", open("C:\\Users\\piyus\\Downloads\\Photoz\\23EBUCS067\\IMG_20250915_111050.jpg", "rb"), "image/jpeg")),
# #     ("images", ("img3.jpg", open("C:\\Users\\piyus\\Downloads\\Photoz\\23EBUCS067\\IMG_20250915_111057.jpg", "rb"), "image/jpeg")),
# #     ("images", ("img4.jpg", open("C:\\Users\\piyus\\Downloads\\Photoz\\23EBUCS067\\IMG_20250915_111058.jpg", "rb"), "image/jpeg")),
# #     ("images", ("img5.jpg", open("C:\\Users\\piyus\\Downloads\\Photoz\\23EBUCS067\\IMG_20250915_111109.jpg", "rb"), "image/jpeg")),
# # ]

payload = {
    "email":"p@gmail.com",
    "name":"P",
    "password":"p@123",
    "role":"HOD"
}
headers = {
    "Authorization": f"Bearer {access_token}"
}
response = requests.post(endpoint+"professor/",data=payload,headers=headers)
# # # response = requests.get(endpoint+"professor/subjects/",headers=headers)

print(response.status_code)
print(response.json())
