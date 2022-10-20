import requests

headers1 = {'Content-Type': "application/json", 'Accept': "application/json"}
pet_id = '30001201'

add_pet = requests.post('https://petstore.swagger.io/v2/pet', json= {
  "id": 30001201,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "dogster",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
},
                            headers=headers1)

changePet = requests.put('https://petstore.swagger.io/v2/pet', json={
    "id": pet_id,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "LeBron",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}, headers=headers1)
getPet = requests.get('https://petstore.swagger.io/v2/pet/' + pet_id, headers=headers1)
print(getPet.text)
