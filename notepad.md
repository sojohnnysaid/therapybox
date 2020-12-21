from simplecrypt import encrypt, decrypt
import json
password = 'secret-password'
user_dict = {'email':'john@gmail.com','first_name':'John'}
json_str = json.dumps(user_dict)
ciphertext = encrypt(password, json_str)
user_dict_returned = json.loads(decrypt(password, ciphertext))