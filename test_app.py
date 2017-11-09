import requests

url = 'http://localhost:5002/profile/'

# GET profiles 展示所有資料
profiles = requests.get(url)
print("GET profiles: " + profiles.text)

# GET profile/id 讀取使用者資料
get_id = 1
get_profile = requests.get(url + str(get_id))
print("GET profile/%s: " % get_id , get_profile.text)

# POST profile/id 新增一筆資料
post_id = 9
post_data = {"name": "XYZ", "age": 123}
post_profile = requests.post(url + str(post_id), json=post_data)
print("POST profile/%s: " % post_id, post_profile.text)

# PUT proffile/id 修改/新增一筆資料
put_id = 2
put_data = {"name": "Ben", "age": 21}
put_profile = requests.put(url + str(put_id), json=put_data)
print("PUT profile/%s: " % put_id, put_profile.text)

# DELETE proffile/id 修改/新增一筆資料
delete_id = 999
delete_profile = requests.delete(url + str(delete_id))
print(delete_profile.text)

