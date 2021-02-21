from dao import UserDao

def store_userInfo(userData_dict):

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