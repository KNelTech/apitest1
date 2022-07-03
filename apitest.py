import http.client
import config

conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': config.key
    }

conn.request("GET", "/gasPrice/stateUsaPrice?state=IL", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))