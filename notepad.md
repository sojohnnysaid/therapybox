import base64
import json
user_dict_start = {'email':'john@gmail.com','first_name':'John'}
json_bytearray = str.encode(json.dumps(user_dict_start))
encoded_json_bytearray = base64.b64encode(json_bytearray)
# append this to the url in the account activation email etc...
# user clicks the link in their email and a view handles...
decoded_json_bytearray = base64.b64decode(encoded_json_bytearray)
json_string = decoded_json_bytearray.decode()
user_dict_end = json.loads(json_string)

