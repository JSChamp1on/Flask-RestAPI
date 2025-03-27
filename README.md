

## Flask RestAPI Server

### Installation

Install Flask libs

```bash
  $ pip install -r requirements.txt
```
    
### ENV

The variable environment settings are located __/.env__ or __/app/env.py__ file.


### Database migration 

To run, run the following command

```bash
  $ flask db upgrade
```

### Run server 

```bash
  $ python main.py
```

## API Reference

#### Register user

```http
  POST /api/register_user
```

Content Type `application/json`

| Parameter | Type      | Description                       |
| :-------- | :-------  | :-------------------------        |
| `username` | `string` | Length from 3 to 20 symbol        |
| `password` | `string` |                                   |
| `gender`   | `string` | Only __male__ or __female__ value |
| `birthday` | `string` | YYYY-MM-DD                        |
| `email`    | `string` | You@mail.ru or __Undefined__      |


#### Login user

```http
  POST /api/login_user
```

Content Type `application/json`

| Parameter  | Type     |
| :--------  | :------- |
| `username` | `string` |
| `password` | `string` |


#### Get users

```http
  POST /api/get_users
```

Depending on whether the user has authenticated or not, there are several possible responses. 

AUAUTHORIZED
```code
{
  users: [
    {
      username: string,
      gender: string,
      birthday: string,
      last_name: string,
      first_name: string
    }
  ]
}
```

Not AUAUTHORIZED
```code
{
  users: [
    {
      username: string
    }
  ]
}
```


