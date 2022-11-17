while True:    
    menu()
    menu_item = menu_input()
    if not correct_menu_item(menu_item):
        pass
    print('Обработать далее...')
