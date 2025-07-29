# status_code = int(input('请输入HTTP响应状态码:'))
# if status_code == 400:
#     description = 'Bad Request'
# elif status_code == 401:
#     description = 'Unauthorized'
# elif status_code == 403:
#     description = 'Forbidden'
# elif status_code == 404:
#     description = 'Not Found'
# elif status_code == 405:
#     description = 'Method Not Allowed'
# elif status_code == 406:
#     description = 'Not Acceptable'
# elif status_code == 408:
#     description = 'Request Timeout' 
# elif status_code == 410:
#     description = 'Gone'
# elif status_code == 411:
#     description = 'Length Required'
# else:
#     description = 'Unknown'
# print('状态码:',status_code)
# print('状态描述:',description)


# 使用`match-case`语法实现
# status_code = int(input('请输入HTTP响应状态码:'))
# match status_code:
#     case 400:
#         description = 'Bad Request'
#     case 401:
#         description = 'Unauthorized'
#     case 403:
#         description = 'Forbidden'
#     case 404:
#         description = 'Not Found'
#     case 405:
#         description = 'Method Not Allowed'
#     case 406:
#         description = 'Not Acceptable'
#     case 408:
#         description = 'Request Timeout'
#     case 410:
#         description = 'Gone'
#     case 411:
#         description = 'Length Required'
#     case _:
#         description = 'Unknown'
# # print('状态码:',status_code)
# print('状态描述:',description)

# 合并
status_code = int(input('响应状态码:'))
match status_code:
  case 400 |405:description = "Invalid Request"
  case 401 | 403 | 404:description = "Unauthorized"
  case 406:description = "Not Acceptable"
  case 408:description = "Request Timeout"
  case 410:description = "Gone"
  case 411:description = "Length Required"
  case _:description = "Unknown"
print('状态码:',status_code)
print('状态描述:',description)