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
a_account = Mongo.db['a_account']
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
    a_account = Mongo.db['a_account']
    seat = Mongo.db['seat']
    student = Mongo.db['student']
    preserve = Mongo.db['preserve']
    classroom = Mongo.db['classroom']

    # s_account.insert_one({
    #     'username': 'Scy',
    #     'passwd': '123123',
    #     'uid': ObjectId('64760d55b6f00d801a5e5499')
    # })
    #
    # s_account.insert_one({
    #     'username': 'Gqm',
    #     'passwd': '123123',
    #     'uid': ObjectId('64760d55b6f00d801a5e5491')
    # })
    #
    # a_account.insert_one({
    #     'username': 'admin',
    #     'passwd': '123123',
    #     'uid': ObjectId('64783fdcce9d801d75491e6a')
    # })
    #
    student.insert_one({
        '_id': ObjectId('64760d55b6f00d801a5e5499'),
        'name': 'Scy',
        'email': '3043642553@qq.com',
        'violate': False,
        'preserve': []
    })

    student.insert_one({
        '_id': ObjectId('64760d55b6f00d801a5e5491'),
        'name': 'Gqm',
        'email': '3043642553@qq.com',
        'violate': False,
        'preserve': []
    })
    #
    seat.insert_one({
        "_id": ObjectId("646b613606b11a421a63e1dd"),
        "name": "A101-001",
        "is_special": "true",
        "classroom": ObjectId("646b602906b11a421a63e1d1"),
        'pre_list': [{'idx': ObjectId('64902a5e44b7657c00685170'), 'start_time': '2023-06-23 13:00',
                      'end_time': '2023-06-23 15:00'}]
    })

    seat.insert_one({
        "_id": ObjectId("646b614506b11a421a63e1de"),
        "name": "A101-002",
        "is_special": "true",
        "classroom": ObjectId("646b602906b11a421a63e1d1"),
        'pre_list': []

    })

    seat.insert_one({
        "_id": ObjectId("646b613606b11a421a63e1da"),
        "name": "A102-001",
        "is_special": "true",
        "classroom": ObjectId("646b602906b11a421a63e1d2"),
        'pre_list': []
    })

    seat.insert_one({
        "_id": ObjectId("646b614506b11a421a63e1db"),
        "name": "A102-002",
        "is_special": "true",
        "classroom": ObjectId("646b602906b11a421a63e1d2"),
        'pre_list': [{'idx': '64902a5e44b7657c00685171', 'start_time': '2023-06-23 13:00', 'end_time': '2023-06-23 15:00'}]
    })

    # classroom.insert_one({
    #     "_id": ObjectId("646b602906b11a421a63e1d1"),
    #     "name": "A101",
    #     "start_time": 8,
    #     "end_time": 22})
    #
    # classroom.insert_one({
    #     "_id": ObjectId("646b602906b11a421a63e1d2"),
    #     "name": "A102",
    #     "start_time": 8,
    #     "end_time": 22})
    #
    # preserve.insert_one({'_id': ObjectId('64902a5e44b7657c00685170'),
    #                      'stu_id': ObjectId('64760d55b6f00d801a5e5499'),
    #                      'seat_id': ObjectId('646b613606b11a421a63e1dd'),
    #                      'start_time': '2023-06-23 13:00',
    #                      'end_time': '2023-06-23 15:00',
    #                      'is_check_in': 0})
    #
    # preserve.insert_one({'_id': ObjectId('64902a5e44b7657c00685171'),
    #                      'stu_id': ObjectId('64760d55b6f00d801a5e5491'),
    #                      'seat_id': ObjectId('646b614506b11a421a63e1db'),
    #                      'start_time': '2023-06-23 13:00',
    #                      'end_time': '2023-06-23 15:00',
    #                      'is_check_in': 0})



# prepare_data()

# student.delete_one({'name': 'Scy'})
# student.delete_one({'name': 'Gqm'})
print("--------------s_account----------------------")
for user in s_account.find():
    print(user)


print("--------------a_account----------------------")
for user in a_account.find():
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

# preserve.delete_one({'_id': ObjectId('64902a5e44b7657c00685170')})
# preserve.insert_one({'_id': ObjectId('64902a5e44b7657c00685170'),
#                     'stu_id': ObjectId('64760d55b6f00d801a5e5499'),
#                     'seat_id': ObjectId('646b613606b11a421a63e1dd'),
#                     'start_time': '2023-06-23 13:00',
#                     'end_time': '2023-06-23 15:00',
#                     'is_check_in': 0})
# preserve.insert_one({'_id': ObjectId('64902a5e44b7657c00685171'),
#                     'stu_id': ObjectId('64760d55b6f00d801a5e5491'),
#                     'seat_id': ObjectId('646b614506b11a421a63e1db'),
#                     'start_time': '2023-06-23 13:00', 'end_time':
#                     '2023-06-23 15:00', 'is_check_in': 0})
print("-----------------preserve-------------------")
for pre in preserve.find():
    print(pre)

# Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'ClassroomManager')
# --------------s_account----------------------
# {'_id': ObjectId('64904a8df49b50fabe57d4cf'), 'username': 'Scy', 'passwd': '123123', 'uid': ObjectId('64760d55b6f00d801a5e5499')}
# {'_id': ObjectId('64904a8df49b50fabe57d4d0'), 'username': 'Gqm', 'passwd': '123123', 'uid': ObjectId('64760d55b6f00d801a5e5491')}
# --------------a_account----------------------
# {'_id': ObjectId('64904a8df49b50fabe57d4d1'), 'username': 'admin', 'passwd': '123123', 'uid': ObjectId('64783fdcce9d801d75491e6a')}
# --------------student----------------------
# {'_id': ObjectId('64760d55b6f00d801a5e5499'), 'name': 'Scy', 'email': '3043642553@qq.com', 'violate': False, 'preserve': []}
# {'_id': ObjectId('64760d55b6f00d801a5e5491'), 'name': 'Gqm', 'email': '3043642553@qq.com', 'violate': False, 'preserve': []}
# --------------seat----------------------
# {'_id': ObjectId('646b613606b11a421a63e1dd'), 'name': 'A101-001', 'is_special': 'true', 'classroom': ObjectId('646b602906b11a421a63e1d1')}
# {'_id': ObjectId('646b614506b11a421a63e1de'), 'name': 'A101-002', 'is_special': 'true', 'classroom': ObjectId('646b602906b11a421a63e1d1')}
# {'_id': ObjectId('646b613606b11a421a63e1da'), 'name': 'A102-001', 'is_special': 'true', 'classroom': ObjectId('646b602906b11a421a63e1d2')}
# {'_id': ObjectId('646b614506b11a421a63e1db'), 'name': 'A102-002', 'is_special': 'true', 'classroom': ObjectId('646b602906b11a421a63e1d2')}
# --------------classroom----------------------
# {'_id': ObjectId('646b602906b11a421a63e1d1'), 'name': 'A101', 'start_time': '8', 'end_time': '22'}
# {'_id': ObjectId('646b602906b11a421a63e1d2'), 'name': 'A102', 'start_time': 8, 'end_time': 22}
# -----------------preserve-------------------
# {'_id': ObjectId('64902a5e44b7657c00685171'), 'stu_id': ObjectId('64760d55b6f00d801a5e5491'), 'seat_id': ObjectId('646b614506b11a421a63e1db'), 'start_time': '2023-06-23 13:00', 'end_time': '2023-06-23 15:00', 'is_check_in': 0}
# {'_id': ObjectId('64902a5e44b7657c00685170'), 'stu_id': ObjectId('64760d55b6f00d801a5e5499'), 'seat_id': ObjectId('646b613606b11a421a63e1dd'), 'start_time': '2023-06-23 13:00', 'end_time': '2023-06-23 15:00', 'is_check_in': 0}
