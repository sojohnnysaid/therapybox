import requests, json
from download import download


body =  {
  "carrier": "COURIERPOST",
  "sender_reference_1": "Order Number 56452",
  "sender_reference_2": "Sales",
  "sender_details": {
    "company_name": "XYZ Widget Company",
    "name": "Bob",
    "phone": "+6425555916",
    "email": "bob@xyzwidgets.com",
    "site_code": 96118,
  },
  "receiver_details": {
    "name": "Alice",
    "phone": "+6424555105",
    "email": "example@example.co.nz"
  },
  "pickup_address": {
    "street": "4 Ransom Smyth Drive",
    "suburb": "Goodwood Heights",
    "city": "Auckland",
    "postcode": "2105",
    "country_code": "NZ"
  },
  "delivery_address": {
    "street": "105 Woodberry Drive",
    "suburb": "Flat Bush",
    "city": "Auckland",
    "postcode": "2016",
    "country_code": "NZ"
  },
  "parcel_details": [{
    "service_code": "CPOLP",
    "add_ons": [],
    "return_indicator": "OUTBOUND",
    "description": "Medium Box",
    "dimensions": {
      "length_cm": 30,
      "width_cm": 30,
      "height_cm": 30,
      "weight_kg": 2
    }
  }]
}

body = json.dumps(body)

headers = {
	"client_id": "5fb5486e9d4748b4b8855fed42aca064",
	"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IlRFU1QiLCJwaS5hdG0iOiIxIn0.eyJzY29wZSI6W10sImNsaWVudF9pZCI6IjVmYjU0ODZlOWQ0NzQ4YjRiODg1NWZlZDQyYWNhMDY0IiwiZXhwIjoxNjEwNjc0MDYxfQ.NlM74HfUF7eRhYSqrvNM5le7KYYg9tQ8D9pbsCAKMac",
	"Content-Type": "application/json"
}






# url = 'https://api.nzpost.co.nz/parcellabel/v3/labels'
# res = requests.post(url, headers=headers, data=body).json()
# print(res)
# consignment_id = res['consignment_id']



# url = f'https://api.nzpost.co.nz/parcellabel/v3/labels/T3BF5Z/status'
# res = requests.get(url, headers=headers).json()
# print(res)




# url = f'https://api.nzpost.co.nz/ParcelLabel/v3/labels/T3BF5Z?format=PDF'
# res = requests.get(url, headers=headers).json()
# print(res)


download('https://api.nzpost.co.nz/parcellabel/v3/labels/T3BF5Z?format=PDF', 'shippinglabel.pdf', headers=headers)