GeekTech = {
    "adress": 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
del GeekTech['bag']

GeekTech['adress'] = 'Ibraimova 123'
GeekTech['Instagram'] = 'geektech_edu'
GeekTech['Phone number'] = '0507-052-018'
GeekTech['courses'].append('UX/UI')
GeekTech['courses'].append('Project Manager')
GeekTech['courses'].append('IOS')
GeekTech['courses'].append('Fundamentals of programming')
# GeekTech = set(GeekTech)
for i in GeekTech:
    print(f'{i} : {GeekTech[i]}')
