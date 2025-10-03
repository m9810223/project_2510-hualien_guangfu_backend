#!/usr/bin/env hurl --continue-on-error --test --repeat 1 --variables-file .env --variable backend_host=https://hualien_guangfu_backend.m9h8.com


POST {{backend_host}}/auth/register
{
  "email": "user@example.com",
  "password": "string",
  "is_active": true,
  "is_superuser": false,
  "is_verified": false
}
HTTP *
[Asserts]
status >= 200
status <= 400



POST {{backend_host}}/auth/jwt/login
content-type: application/x-www-form-urlencoded
`grant_type=password&username=user%40example.com&password=string`
HTTP 200
[Asserts]
jsonpath "$.token_type" == "bearer"
jsonpath "$.access_token" exists
[Captures]
access_token: jsonpath "$.access_token"

GET {{backend_host}}/users/me
authorization: Bearer {{access_token}}
HTTP 200
[Asserts]
jsonpath "$.id" exists
jsonpath "$.email" exists
jsonpath "$.is_active" == true
jsonpath "$.is_superuser" == false
jsonpath "$.is_verified" == false



POST {{backend_host}}/task
authorization: Bearer {{access_token}}
{
  "title": "string"
}
HTTP 200
[Asserts]
jsonpath "$.id" exists
jsonpath "$.created_at" exists
jsonpath "$.creator_id" exists
jsonpath "$.title" == "string"
jsonpath "$.is_deleted" == false
jsonpath "$.registration_location" == null
jsonpath "$.type" == null
jsonpath "$.work_location" == null
jsonpath "$.updated_at" == null
jsonpath "$.required_number_of_people" == null
jsonpath "$.maximum_number_of_people" == null
jsonpath "$.description" == null
jsonpath "$.deadline" == null
jsonpath "$.urgency" == null
jsonpath "$.status" == null
jsonpath "$.contact_number" == null
jsonpath "$.danger_level" == null
jsonpath "$.deleted_at" == null
jsonpath "$.starttime" == null
[Captures]
task_id: jsonpath "$.id"


GET {{backend_host}}/task/{{task_id}}
HTTP 200
[Asserts]
jsonpath "$.id" exists
jsonpath "$.created_at" exists
jsonpath "$.creator_id" exists
jsonpath "$.title" == "string"
jsonpath "$.is_deleted" == false
jsonpath "$.registration_location" == null
jsonpath "$.type" == null
jsonpath "$.work_location" == null
jsonpath "$.updated_at" == null
jsonpath "$.required_number_of_people" == null
jsonpath "$.maximum_number_of_people" == null
jsonpath "$.description" == null
jsonpath "$.deadline" == null
jsonpath "$.urgency" == null
jsonpath "$.status" == null
jsonpath "$.contact_number" == null
jsonpath "$.danger_level" == null
jsonpath "$.deleted_at" == null
jsonpath "$.starttime" == null


PATCH {{backend_host}}/task/{{task_id}}
HTTP 401


PATCH {{backend_host}}/task/{{task_id}}
authorization: Bearer {{access_token}}
{
  "type": "鏟土",
  "title": "string",
  "description": "string",
  "status": "準備中",
  "starttime": "2025-10-03T17:44:16.940Z",
  "deadline": "2025-10-03T17:44:16.940Z",
  "contact_number": "string",
  "registration_location": "string",
  "work_location": "string",
  "required_number_of_people": 0,
  "maximum_number_of_people": 0,
  "urgency": 10,
  "danger_level": 10
}
HTTP 200


DELETE {{backend_host}}/task/{{task_id}}
HTTP 401

DELETE {{backend_host}}/task/{{task_id}}
authorization: Bearer {{access_token}}
HTTP 200
