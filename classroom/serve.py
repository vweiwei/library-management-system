from flask import Flask, request
from flask_cors import CORS, cross_origin

from Controller.AccountController import AccountController
from Controller.ClassroomController import ClassroomController
from Controller.StudentController import StudentController
from Controller.PreserveController import PreserveController
from Controller.SeatController import SeatController

app = Flask(__name__)
cors = CORS(app)

from Utils.scheduler import start_email_scheduler


@app.route('/')
def init():
    return "haha"


@app.route('/login/student', methods=['POST'])
def student_login():
    assert request.method == 'POST'
    username = request.form['username']
    passwd = request.form['passwd']
    return AccountController().student_login(username, passwd)


@app.route('/login/admin', methods=['POST'])
def admin_login():
    assert request.method == 'POST'
    username = request.form['username']
    passwd = request.form['passwd']
    return AccountController().admin_login(username, passwd)


@app.route('/sign_up/student', methods=['POST'])
def student_sign_up():
    assert request.method == 'POST'
    username = request.form['username']
    passwd = request.form['passwd']
    name = request.form['name']
    email = request.form['email']
    return AccountController().sign_up(username, passwd, name, email)


@app.route('/students/preserve', methods=['POST'])
def student_preserve():
    assert request.method == 'POST'
    uid = request.form['uid']
    sid = request.form['sid']
    start_time = request.form['start_time']
    end_time = request.form['end_time']
    return PreserveController().preserve(uid, sid, start_time, end_time)


@app.route('/classrooms/overview', methods=['GET'])
def get_classroom_overview():
    assert request.method == 'GET'
    return ClassroomController().get_classroom_overview()


@app.route('/classrooms/detail/', methods=['GET'])
def get_classroom_detail():
    assert request.method == 'GET'
    classroom_id = request.args.get('cid')
    return ClassroomController().get_classroom_detail(classroom_id)


@app.route('/seats/detail/', methods=['GET'])
def get_seats_detail():
    assert request.method == 'GET'
    seat_id = request.args.get('sid')
    return SeatController().get_seat_detail(seat_id)


@app.route('/students/detail/', methods=['GET'])
def get_students_detail():
    assert request.method == 'GET'
    student_id = request.args.get('uid')
    return StudentController().get_student_detail(student_id)


@app.route('/preserve/cancel', methods=['POST'])
def cancel_preserve():
    assert request.method == 'POST'
    pid = request.form['pid']
    return PreserveController().cancel_preserve(pid)


@app.route('/preserve/check_in', methods=['POST'])
def check_in():
    assert request.method == 'POST'
    pid = request.form['pid']
    return PreserveController().check_in(pid)


@app.route('/classrooms/modify_time', methods=['POST'])
def modify_time():
    assert request.method == 'POST'
    cid = request.form['cid']
    start_time = request.form['start_time']
    end_time = request.form['end_time']
    print(start_time)
    return ClassroomController().modify_time(cid, start_time, end_time)


if __name__ == '__main__':
    app.run("0.0.0.0")
    start_email_scheduler(timezone='Asia/Shanghai')
