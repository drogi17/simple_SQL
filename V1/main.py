from modules.sqlite_inquiries import DataBase
db = DataBase('data/data.db')

def print_select():
    columns = ['f_name', 'age']
    for user in db.simple_select('users', columns):
        print('%2s      %3s' % user)
    print('----------------------------------------')

#                   simple_select
for usr in db.simple_select('users', '*'):
    print('%2s      %2s      %2s      %2s' % usr)
print('----------------------------------------')



#                   insert
f_name  = input('f_name: ')
l_name  = input('l_name: ')
age     = int(input('age: '))
insert_data = {
    'f_name':   f_name,
    'l_name':   l_name,
    'age':      age
}
db.insert('users', insert_data)
print_select()


#                   set
id_user_to_edit = input('id: ')
f_name_edit     = input('f_name_edit: ')
l_name_edit     = input('l_name_edit: ')
age_edit        = int(input('age_edit: '))


set_data = {
    'f_name':   f_name_edit,
    'l_name':   l_name_edit,
    'age':      age_edit
}
filter_list = ['id = ' + id_user_to_edit]
db.set('users', set_data, filter_list)
print_select()

#                   delete
do = input('Delete someone?(y/n): ')
if do == 'y':
    id_user_to_delete = input('id: ')
    db.delete('users', id_user_to_delete)
    print_select()
    print('Deleted...')
else:
    print('Ok...')
