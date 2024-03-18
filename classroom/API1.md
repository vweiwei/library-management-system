#### 1. 自习数据总览

接口地址：[http://url/classrooms/overview](http://url/classrooms/overview) 
支持格式：json
请求方法：GET
请求示例：[http://url/classrooms/overview](http://url/classrooms/overview)

- 响应内容：

| 参数名称       | 类型     | 说明           |
|:----------:|:------:|:------------:|
| id         | int    | classroom id |
| name       | string | 教室名称         |
| is_open    | bool   | 是否开放         |
| start_time | int    | 开放时间         |
| end_time   | int    | 关闭时间         |

- JSON响应示例:

```json
{
     "status" : "0",
     "msg" : "ok",
     "result" :[
         {   
             "id": 101,        //教室id从101开始
             "name" : "A101",  //name为字母+id
             "is_open" : true,
             "start_time": 8,  //随机为8-10
             "end_time": 22    //随机为17-22
         }
     ]  
}
```

#### 2. 根据自习室号查询该自习室座位数据

接口地址：[http://url/classrooms/detail/](http://url/classrooms/detail/)
支持格式：json
请求方法：*GET*
请求示例：[http://url/activities/detail/cid/101](http://url/activities/detail/cid/101)

- 响应内容

| 参数名称       | 类型     | 说明        |
|:----------:|:------:|:---------:|
| id         | int    | 座位id      |
| name       | string | 座位名称（号）   |
| is_used    | bool   | 是否正在占用    |
| start_time | int    | 该自习室的开始时间 |
| end_time   | int    | 该自习室的结束时间 |

- JSON响应示例:

```json
{
 "status" : "0",
 "msg" : "ok",
 "result" :[
     {
         "id": 101001,        //座位id为前三位为教室id，后三位从001开始
         "name": "A101-001",  //name为教室name+座位id后三位
         "is_used" : true,
     }
  ]
  "start_time": 8,
  "end_time": 22
}
```

#### 3. 查询具体座位信息

接口地址：[http://url/seats/](http://url/seats/) 
支持格式：json
请求方法：*GET* 
请求示例：[http://url/seats/sid/101001/](http://url/seats/sid/101001/)

- 响应内容

| 参数名称       | 类型     | 说明            |
|:----------:|:------:|:-------------:|
| id         | int    | 座位id          |
| name       | string | 座位名称          |
| is_used    | bool   | 是否正在使用        |
| pre_list   | list   | 预约的列表         |
| is_special | bool   | 是否是特殊座位（有无插头） |

- JSON响应示例:

```json
{
     "status" : "0",
     "msg" : "ok",
     "result" :[
         {
             "id": 101001,
             "name": "A101-001",
             "is_used": false,
             "pre_list": [
                 [2000(用户编号)， 8（起始时间）， 10（结束时间）]
                 [2001(用户编号)， 8（起始时间）， 14（结束时间）]
             ],
             "is_special": true,
         },
     ]
}
```

#### 4. 学生预约座位

接口地址：[http://url/students/preserve/](http://url/students/preserve/) 
支持格式：json
请求方法：*POST* 
请求示例：[http://url/students/preserve/](http://url/students/preserve/)

- 请求内容

| 参数名称       | 类型  | 说明   |
|:----------:|:---:|:----:|
| uid        | int | 用户id |
| sid        | int | 座位id |
| start_time | int | 开始时间 |
| end_time   | int | 结束时间 |

- 响应内容

| 参数名称     | 类型  | 说明     |
|:--------:|:---:|:------:|
| preserve | int | 是否预约成功 |

- JSON响应示例:

```json
{
     "status" : 0,
     "msg" : "ok",
     "result" :
     {
         "preserve": 1
     }
}
```

#### 5. 学生登录

接口地址：[http://url/login/student](http://url/login/student) 
支持格式：json
请求方法：*POST* 
请求示例：[http://url/login/student](http://url/login/student)

- 请求参数：

| 参数名称     | 类型     | 必填  | 说明  |
|:--------:|:------:|:---:|:---:|
| username | string | Y   | 用户名 |
| passwd   | string | Y   | 密码  |

- 响应内容：

| 参数名称       | 类型     | 说明      |
|:----------:|:------:|:-------:|
| msg_status | int    | 登录状态    |
| login_msg  | string | 登陆的返回信息 |
| data       | dict   | 返回的学生数据 |
| uid        | int    | 用户id    |

- JSON响应示例：

```json
{
    "status" : "0",
    "msg"    : "ok",
    "result" :
    {
        "login_status" : 1
        "login_msg" : "登陆成功"
        "data": 
        {
            "uid": 2000    //用户id从2开始
        }
   }
}
```

#### 6. 根据学生用户ID获取用户信息

接口地址：[http://url/login/student](http://url/login/student) 
支持格式：json
请求方法：*GET*
请求示例：[[http://url/login/student/uid/2000](http://url/login/student/uid/2000)

- 响应内容：

| 参数名称     | 类型     | 说明   |
|:--------:|:------:|:----:|
| uid      | int    | 用户id |
| name     | string | 昵称   |
| email    | string | 邮箱   |
| pre_list | list   | 预约列表 |

- JSON响应示例：

```json
{
    "status": "0",
    "msg" : "ok",
    "result" :{
        "uid" : 2001,
        "name" : "setsuna",
        "email" : "acgn@yyds.com",
        "pre_list" : [
            {
              "pid": "3001",
              "roomName": "自习室101",
              "s_name": "A101",
              "sid": 101001,
              "startTime": "2023-05-22 18:00",
              "endTime": "2023-05-22 20:00",
              "is_check_in": 0,
              "countdownIntervalId": null,
              "remainingTime": null
            },
            {
              "pid": "3002",
              "roomName": "自习室102",
              "s_name": "A102",
              "sid": 102010,
              "startTime": "2023-05-22 20:00",
              "endTime": "2023-05-22 22:00",
              "is_check_in": 1,
              "countdownIntervalId": null,
              "remainingTime": null
            }
        ]
    }
}
```

#### 7. 根据pid请求签到
接口地址：[http://url/preserve/check_in](http://url/login/check_in) 
支持格式：json
请求方法：*POST*
- 请求参数：

| 参数名称     | 类型     | 必填  | 说明  |
|:--------:|:------:|:---:|:---:|
| pid | string | Y   | pid |


```json
{
    "status": "0",
    "msg": "ok",
    "results": {
        "isSignUp": true
    }
}
```


#### 8. 根据pid取消预约
接口地址：[http://url/preserve/check_in](http://url/login/cancel) 
支持格式：json
请求方法：*POST*
- 请求参数：

| 参数名称     | 类型     | 必填  | 说明  |
|:--------:|:------:|:---:|:---:|
| pid | string | Y   | pid |

```json
{
    "status": "0",
    "msg": "ok",
    "results": {
        "isCancel": true
    }
}
```
