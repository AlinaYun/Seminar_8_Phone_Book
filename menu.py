def menu():
    print('**************************')
    print('            MENU          ')
    print('**************************')
    menu_options = ['добавить контакт', 'редактировать контакт', 'экспортировать контакт', 'импортировать контакт', 'удалить контакт']
    for i in range (len(menu_options)):
        print(f'{i+1}. {menu_options[i].upper()}')
    print()
    
#menu()