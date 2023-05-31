import view
import model
import text

def start():
    pb = model.get_contact_list()
    while True:
       value =  view.main_menu()
       match value:
           case 1:
               view.print_contact_list(pb)
               view.print_message(text.succsesful_message)
           case 2:
               model.add_contact()
               model.save_contact()
               view.print_message(text.succsesful_message)
           case 3:
               search_list, index_for_change = model.search_contact()
               if len(search_list) !=0:
                   view.print_contact_list(search_list)
               else:
                   view.print_message(text.search_fall)
           case 4:
                search_list, index_for_change = model.search_contact()
                flag = 1
                while flag:
                    if len(search_list) > 1: 
                        view.print_message(text.search_message)
                        search_list, index_for_change = model.search_contact()
                    elif len(search_list) == 0: 
                        view.print_message(text.search_fall)
                        search_list, index_for_change = model.search_contact()
                    else:
                        while flag:
                            input_value =  view.change_contact_menu()
                            match input_value:
                                case 1:
                                    ch_contact = model.change_contact(search_list, index_for_change, input_value)
                                    model.save_contact()
                                    view.print_message(text.succsesful_message)
                                    search_list[0] = ch_contact
                                case 2:
                                    ch_contact = model.change_contact(search_list, index_for_change, input_value)
                                    model.save_contact()
                                    view.print_message(text.succsesful_message)
                                    search_list[0] = ch_contact
                                case 3:
                                    view.print_message(text.succsesful_message)
                                    flag = 0               
           case 5:
                search_list, index_for_change = model.search_contact()
                flag = 1
                while flag:
                    if len(search_list) > 1: 
                        view.print_message(text.search_message)
                        search_list, index_for_change = model.search_contact()
                    elif len(search_list) == 0: 
                        view.print_message(text.search_fall)
                        search_list, index_for_change = model.search_contact()
                    else:
                        model.del_contact(index_for_change[0])
                        model.save_contact()
                        view.print_message(text.succsesful_message)
                        
                        flag = 0
           case 6:
               view.print_message(text.bye_message)
               exit()