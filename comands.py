from colors import * 


LIST_COMANDS_BOT = ["hello", "add", "change","get phone","show all",'search', "exit"]
DOSTUPNI_COMANDY = f"{RED}Доступні наступні команди : {DEFALUT}{GREEN}{LIST_COMANDS_BOT}{DEFALUT}"
PISKAZKA_SHOW_ALL = f"\nКоманда - {GREEN}show all{YLLOW} - покаже доступні контакти{DEFALUT}"

LIST_COMANDS_BOT = ["hello", "add", "change","get phone","show all",'search', "exit"]

DOSTUPNI_COMANDY = f"{RED}Доступні наступні команди : {GREEN}{LIST_COMANDS_BOT}{DEFALUT}"

BAD_COMMAND_ADD = f"{YLLOW}Невірні параметри для команди {GREEN}add{YLLOW} !!!.\n\
                        {RED}# Приклад {GREEN}add{BIRUZA} Імя_контакту{YLLOW} Номер_телефону {DEFALUT}"
    
BAD_COMMAND_CHANGE = f"{YLLOW}Невірні параметри для команди {GREEN}change{YLLOW} !!!.\n\
                           {RED}# Приклад {GREEN}change{BIRUZA} Імя_контакту{YLLOW}{DEFALUT}"
    
BAD_COMMAND_PHONE = f"{YLLOW}Невірні параметри для команди {GREEN}get phone{YLLOW} !!!.\n\
                           {RED}# Приклад {GREEN}get phone{BIRUZA} Імя_контакту{YLLOW}{DEFALUT} "
    
BAD_COMMAND_SEARCH = f"{YLLOW}Невірні параметри для команди {GREEN}search{YLLOW} !!!.\n\
                           {RED}# Приклад {GREEN}search{BIRUZA} Імя_контакту{YLLOW}{DEFALUT} "

BAD_FORMAT_PHONE = (f"{RED}Невірний формат !!!{YLLOW}<Номер може містити тільки 10 цифри !!!>\n{GREEN}\
                    ### Приклад:  0931245891{DEFALUT}")

NOT_FOUND_NAME = f"{YLLOW}Такого імені не знайдено у вашій телефоній книзі !!!"\
                                 f"{DEFALUT}{PISKAZKA_SHOW_ALL}"
NOT_FOUND_COMMAND = f'{YLLOW}Tака команда не пітримується наразі\n{DEFALUT}{DOSTUPNI_COMANDY}'

