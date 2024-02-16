from colors import * 
LIST_COMANDS_BOT = ["hello", "add", "change","phone","show all",'search',"good bye", "close", "exit"]
DOSTUPNI_COMANDY = f"{RED}Доступні наступні команди : {GREEN}{LIST_COMANDS_BOT}{DEFALUT}"
PISKAZKA_SHOW_ALL = f"\nКоманда - {GREEN}show all{YLLOW} - покаже доступні контакти{DEFALUT}"

LIST_COMANDS_BOT = ["hello", "add", "change","phone","show all",'search',"good bye", "close", "exit"]
DOSTUPNI_COMANDY = f"{RED}Доступні наступні команди : {GREEN}{LIST_COMANDS_BOT}{DEFALUT}"
BAD_COMMAND_ADD = f"{YLLOW}Невірні параметри для команди {GREEN}add{YLLOW} !!!.\n\
                        {RED}# Приклад {GREEN}add{BIRUZA} Імя_контакту{YLLOW} Номер_телефону {DEFALUT}"
    
BAD_COMMAND_CHANGE = f"{YLLOW}Невірні параметри для команди {GREEN}change{YLLOW} !!!.\n\
                           {RED}# Приклад {GREEN}change{BIRUZA} Імя_контакту{YLLOW} "
    
BAD_COMMAND_PHONE = f"{YLLOW}Невірні параметри для команди {GREEN}phone{YLLOW} !!!.\n\
                           {RED}# Приклад {GREEN}phone{BIRUZA} Імя_контакту{YLLOW} "
    
BAD_COMMAND_SEARCH = f"{YLLOW}Невірні параметри для команди {GREEN}search{YLLOW} !!!.\n\
                           {RED}# Приклад {GREEN}search{BIRUZA} Імя_контакту{YLLOW} "