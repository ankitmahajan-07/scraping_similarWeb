import requests

response = requests.get("https://proxy.webshare.io/api/proxy/list/?page=1&countries=US-FR", headers={"Authorization": "39dc234f0ea58b0488a390a948d0bb222e6d8025"})
# response.json()

print(response.json())

# import requests
#
# requests.get("https://proxy.webshare.io/api/", headers={"Authorization": "39dc234f0ea58b0488a390a948d0bb222e6d8025"})
# # print(res.json())