from db import *
User.drop_collection()
print(addUser(7476))
print(json.dumps(json.loads(User.objects().to_json()), sort_keys=True, indent=4))
