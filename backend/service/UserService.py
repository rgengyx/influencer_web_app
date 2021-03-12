from dao import UserDao

def store_userInfo(userData_dict):
    for k, v in userData_dict.items():
        userData_dict[k] = v[0]

    print(userData_dict.keys())
    UserDao.store_userInfo(userData_dict)

def store_agreement(agreementData_dict):
    agreementData_dict['id'] = agreementData_dict['id'][0]
    
    if agreementData_dict['agreement'][0] == 'on':
        agreementData_dict['agreement'] = 'Y'
    else:
        agreementData_dict['agreement'] = 'N'

    UserDao.store_agreement(agreementData_dict)