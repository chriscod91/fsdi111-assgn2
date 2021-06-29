import requests

test_user = {
    "first_name": "john",
    "last_name": "doe",
    "hobbies": "skiing",
    "active": 1
 }

 def test_user_creation():
     out = requests.post("", json=TEST_USER)
    if out.status_code == 201:
        print(out.json())
    else:
        print("something went wrong.")

def test_user_deactivate():
    out = requests.delete("")
    if out.status_code == 200:
        print(out.json())
    else:
        print("something went wrong with delete.")

if __name__=="__main__":
    test_user_creation()
