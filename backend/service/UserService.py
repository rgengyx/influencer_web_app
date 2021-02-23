from dao import UserDao

def store_userInfo(userData_dict):
    userData_dict['id'] = userData_dict['id'][0]
    userData_dict['age'] = userData_dict['age'][0]
    
    if userData_dict['gender'][0] == 'on':
        userData_dict['gender'] = 'M'
    else:
        userData_dict['gender'] = 'F'

    if userData_dict['use_amazon'][0] == 'on':
        userData_dict['use_amazon'] = 'Y'
    else:
        userData_dict['use_amazon'] = 'N'

    if userData_dict['read_review'][0] == 'on':
        userData_dict['read_review'] = 'Y'
    else:
        userData_dict['read_review'] = 'N'

    UserDao.store_userInfo(userData_dict)

def store_agreement(agreementData_dict):
    agreementData_dict['id'] = agreementData_dict['id'][0]
    
    if agreementData_dict['agreement'][0] == 'on':
        agreementData_dict['agreement'] = 'M'
    else:
        agreementData_dict['agreement'] = 'F'

    UserDao.store_agreement(agreementData_dict)