import pymongo
from Utils.Database import MongoConnection
from bson import ObjectId


# s_account
# a_account
# student
# classroom
# preserve
# seat

Mongo = MongoConnection()
s_account = Mongo.db['s_account']
seat = Mongo.db['seat']
student = Mongo.db['student']
classroom = Mongo.db['classroom']
preserve = Mongo.db['preserve']

print(Mongo.db)


# seat.insert_one(data)
# s_account.insert_one(data)

# s_account.delete_one({'username': 'Gqm'})

# for seats in seat.find():
#     print(seats)


def prepare_data():
    Mongo = MongoConnection()
    s_account = Mongo.db['s_account']
    seat = Mongo.db['seat']
    student = Mongo.db['student']
    preserve = Mongo.db['preserve']
    classroom = Mongo.db['classroom']



    seat.insert_one({
        "_id": ObjectId("646b613606b11a421a63e1dd"),
        "name": "A101-001",
        "is_special": "true",
        "classroom": ObjectId("646b602906b11a421a63e1d1")})

    seat.insert_one({
        "_id": ObjectId("646b614506b11a421a63e1de"),
        "name": "A101-002",
        "is_special": "true",
        "classroom": ObjectId("646b602906b11a421a63e1d1")})

    classroom.insert_one({
        "_id": ObjectId("646b602906b11a421a63e1d1"),
        "name": "A101",
        "start_time": 8,
        "end_time": 22})

# prepare_data()
data = {
    'stu_id': ObjectId('64760d55b6f00d801a5e5499'),
    'seat_id': ObjectId('646b613606b11a421a63e1dd'),
    'start_time': '15',
    'end_time': '16'
}

# content = preserve.delete_one({'start_time': '15'})
# print(content.raw_result)

print("--------------s_account----------------------")
for user in s_account.find():
    print(user)

print("--------------student----------------------")
for s in student.find():
    print(s)

print("--------------seat----------------------")
for seat in seat.find():
    print(seat)


print("--------------classroom----------------------")
for classroom in classroom.find():
    print(classroom)


print("-----------------preserve-------------------")
for pre in preserve.find():
    print(pre)

# --------------s_account----------------------
# {'_id': ObjectId('64760d55b6f00d801a5e5498'), 'username': 'Scy', 'passwd': '123123', 'uid': ObjectId('64760d55b6f00d801a5e5499')}
# {'_id': ObjectId('64760da6b6f00d801a5e54a0'), 'username': 'Gqm', 'passwd': '123123', 'uid': ObjectId('64760da6b6f00d801a5e54a1')}
# {'_id': ObjectId('64783fdcce9d801d75491e69'), 'username': 'Blz', 'passwd': '123123', 'uid': ObjectId('64783fdcce9d801d75491e6a')}
# {'_id': ObjectId('647842ddce9d801d75491e81'), 'username': 'Yzh', 'passwd': '123123', 'uid': ObjectId('647842ddce9d801d75491e82')}
# --------------student----------------------
# {'_id': ObjectId('64760d55b6f00d801a5e5499'), 'name': 'Scy', 'email': '1234567890@163.com', 'preserve': []}
# {'_id': ObjectId('64760da6b6f00d801a5e54a1'), 'name': 'Gqm', 'email': '1234567890@163.com', 'preserve': []}
# {'_id': ObjectId('64783fdcce9d801d75491e6a'), 'name': 'Blz', 'email': '1234567890@163.com', 'preserve': []}
# {'_id': ObjectId('647842ddce9d801d75491e82'), 'name': 'Yzh', 'email': '1234567890@163.com', 'preserve': []}
# --------------seat----------------------
# {'_id': ObjectId('646adf41c5387dbd1f260bc6'), 'id': 100001, 'name': 'A100-001', 'is_used': False, 'pre_list': [], 'is_special': False}
# {'_id': ObjectId('646adf887ef7f3690ce5ee7e'), 'id': 100002, 'name': 'A100-002', 'is_used': False, 'pre_list': [], 'is_special': False}
# {'_id': ObjectId('646b613606b11a421a63e1dd'), 'name': 'A101-001', 'is_special': 'true', 'classroom': ObjectId('646b602906b11a421a63e1d1')}
# {'_id': ObjectId('646b614506b11a421a63e1de'), 'name': 'A101-002', 'is_special': 'true', 'classroom': ObjectId('646b602906b11a421a63e1d1')}
# --------------classroom----------------------
# {'_id': ObjectId('646b602906b11a421a63e1d1'), 'name': 'A101', 'start_time': 8, 'end_time': 22}
# -----------------preserve-------------------
# {'_id': ObjectId('647616e3b6f00d801a5e54a7'), 'stu_id': ObjectId('64760d55b6f00d801a5e5499'), 'seat_id': ObjectId('646b613606b11a421a63e1dd'), 'start_time': '8', 'end_time': '10'}
# {'_id': ObjectId('64761990b6f00d801a5e54a9'), 'stu_id': ObjectId('64760d55b6f00d801a5e5499'), 'seat_id': ObjectId('646b613606b11a421a63e1dd'), 'start_time': '11', 'end_time': '13'}
# {'_id': ObjectId('64761a13b6f00d801a5e54ab'), 'stu_id': ObjectId('64760d55b6f00d801a5e5499'), 'seat_id': ObjectId('646b613606b11a421a63e1dd'), 'start_time': '13', 'end_time': '15'}