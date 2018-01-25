# pyofo
A Python library to interface with ofo bike API.

## Usage
### Authentication
**You should create an ofo account before authentication.**

#### Request a sms code
```python
import pyofo

login_handler = pyofo.LoginHandler(tel='612345678', ccc='33', lat='48.23', lng='2.3')
r = login_handler.request_sms_code()
r.text
```

```json
{
    "errorCode": 200,
    "msg": "Success",
    "values": {}
}
```

You will receive a sms with a 4-digit OTP code on your mobile phone.

#### Login and get user token
```python
r = login_handler.login_with_code(otp_code='1234')
r.text
```

```json
{
    "errorCode": 200,
    "msg": "登陆成功",
    "values": {
        "token": "xxxxxxxxxxxxxxxxxx",
        "isNewuser": false,
        "needDeposit": false,
        "depositToPay": 0,
        "depositCurrency": "€",
        "paymentMethod": {}
    }
}
```

### Get nearby bikes
```python
import pyofo

pyofo.set_token('your_token')
ofo = pyofo.Ofo()

r = ofo.nearby_ofo_car(lat='48.23', lng='2.3')
r.text
```

```json
{
	"errorCode": 200,
	"msg": "附近车辆位置",
	"values": {
		"cars": [
			{
				"userIdLast": "1",
				"lng": 2.3796870561551,
				"lat": 48.839922829334
			}
    ]
  }
}
```

### Use behind a proxy server
```python
import pyofo
pyofo.set_proxies(https='yourproxy')  # if necessary
pyofo.set_auth('username', 'password')
```

## Dependency
- requests

For more information, see [this document](https://github.com/ubahnverleih/WoBike/blob/master/Ofo.md).
