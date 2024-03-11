from virtual_assistant_v007.colors import * 


PISKAZKA_SHOW_ALL = f"\nКоманда - {GREEN}show all{YLLOW} - покаже доступні контакти{DEFALUT}"

LIST_COMANDS_BOT = ["hello", "help", "add", "show all", "change", "delete", 'search', "get phone",
                    "email", 'birthday', 'sorted', 'notes', "exit"]

DOSTUPNI_COMANDY = f"{RED}Доступні наступні команди : {GREEN}{LIST_COMANDS_BOT}{DEFALUT}"

PATH_TO_DIR = fr"C:\Users\User\Desktop\Go_IT\Rizne"

BAD_COMMAND_ADD = (f"{YLLOW}Невірні параметри для команди {GREEN}'add'{YLLOW} !!!.\n\
                        {RED}# Приклад {GREEN}add{BIRUZA} Імя_контакту"
                   f"{YLLOW} [phone=1111111111] [email=1111@mai.com] [birthday=1999-01-01] [address=Kyiv] {DEFALUT}")
    
BAD_COMMAND_CHANGE = f"{YLLOW}Невірні параметри для команди {GREEN}'change'{YLLOW} !!!.\n\
                           {RED}# Приклад {GREEN}change{BIRUZA} Імя_контакту {GREEN}name={BIRUZA}Нове ім'я "
    
BAD_COMMAND_PHONE = (f"{YLLOW}Невірні параметри для команди {GREEN}'get phone'{YLLOW} !!!.\n\
                           {RED}# Приклад {GREEN}get phone{BIRUZA} Andrew  "
                     f"{RED}<<{GREEN} get phone {YLLOW}'Імя контакту'{RED} >> ")
    
BAD_COMMAND_SEARCH = f"{YLLOW}Невірні параметри для команди {GREEN}'search'{YLLOW} !!!.\n\
                           {RED}# Приклад {GREEN}search{BIRUZA} пошуковий текст{YLLOW} "

BAD_COMMAND_SORTED = (f"{YLLOW}Невірні параметри для команди {GREEN}'sorted'{YLLOW} !!!.\n\
                        {RED}# Приклад {GREEN}sorted{BIRUZA} {PATH_TO_DIR}  "
                      f"{RED}<<{GREEN} sorted {BIRUZA}'Шлях до папки'{RED} >>")

BAD_COMMAND_NOTES = f"{YLLOW}Невірні параметри для команди {GREEN}'notes'{YLLOW} !!!.\n\
                        {RED}# Приклад {GREEN}notes"

BAD_COMMAND_EMAIL = f"{YLLOW}Невірні параметри для команди {GREEN}'email'{YLLOW} !!!.\n\
                        {RED}# Приклад {GREEN}'email'{BIRUZA}Імя_контакту{YLLOW} "

BAD_COMMAND_BIRTHDAYS = f"{YLLOW}Невірні параметри для команди {GREEN}'birthday'{YLLOW} !!!.\n\
                {RED}# Приклад:  {GREEN}birthday{YLLOW} 50  {RED}<<{GREEN} birthday {YLLOW}'кількість днів'{RED} >>"

BAD_COMMAND_DELETE = f"{YLLOW}Невірні параметри для команди {GREEN}'delete'{YLLOW} !!!.\n\
                           {RED}# Приклад {GREEN}delete{BIRUZA} Імя_контакту{DEFALUT}"

BAD_FORMAT_PHONE = (f"{RED}Невірний формат !!!{YLLOW}<Номер може містити тільки 10 цифри !!!>\n{GREEN}\
                    # Приклад:  0931245891{DEFALUT}")

BAD_FORMAT_EMAIL = f"{YLLOW}Не вірний формат e-mail.\n {RED}Приклад - {BIRUZA}python@gmail.com"

BAD_FORMAT_BIRTHDAY = f"{YLLOW}Не вірний формат дати народження. Використовуйте {RED}YYYY-MM-DD."

NOT_FOUND_NAME = f"{YLLOW}Такого імені не знайдено у вашій телефонній книзі !!!\n {PISKAZKA_SHOW_ALL}"

NOT_FOUND_COMMAND = f'{YLLOW}Tака команда не пітримується наразі\n{DEFALUT}{DOSTUPNI_COMANDY}'

BAD_COMMAND_EMAIL = f"{YLLOW}Невірні параметри для команди {GREEN}email{YLLOW} !!!.\n\
                           {RED}# Приклад {GREEN}email{BIRUZA} Імя_контакту{YLLOW} "

HELP = f" {GREEN}Довідка для Контактного Асистента\n{DEFALUT}" \
                f"{YLLOW}======================================================={DEFALUT}\n" \
                f"{GREEN}Вітаємо у Контактному Асистенті! Ця програма допомагає ефективно керувати"\
                f" вашими контактами.{DEFALUT}\n" \
                f"{GREEN}Список доступних команд:\n" \
                f"{BIRUZA}- `hello`: Привітати бота.\n" \
                f"{BIRUZA}- `add name [phone=<номер_телефону>] [email=<адреса_електронної_пошти>]"\
                f"[birthday=<РРРР-ММ-ДД>] [address=<адреса>]`: Додати новий контакт.{DEFALUT}\n" \
                f"{YLLOW}  - Приклад: `add Mykola phone=1234567890 email=mykola@example.com "\
                f"birthday=1990-01-01 address=вул. Головна, 1`{DEFALUT}\n" \
                f"{YLLOW}  - Примітка: Поля `phone`, `email`, `birthday`, та `address` є опціональними"\
                f"і ви можете вказати тільки ті, які необхідно.{DEFALUT}\n" \
                f"{YLLOW}  - Приклад неправильного введення: `add Mykola phone=1234 email=Mykola@example.com "\
                f"birthday=1990-01-01 address=вул. `{DEFALUT}\n" \
                f"{YLLOW}    Головна, 1` (невірний номер телефону).{DEFALUT}\n" \
                f"{BIRUZA}- `change name <ім'я_контакту> <поле_для_зміни>=<нове_значення>`: Змінити деталі контакту.{DEFALUT}\n" \
                f"{YLLOW}  - Приклад: `change Іван Петров email=newemail@example.com`{DEFALUT}\n" \
                f"{BIRUZA}- `delete <ім'я_контакту>: Видалити контакт.{DEFALUT}\n" \
                f"{YLLOW}  - Приклад: `delete Mykola`{DEFALUT}\n" \
                f"{BIRUZA}- `phone name <ім'я_контакту>`: Отримати номер телефону контакту.{DEFALUT}\n" \
                f"{YLLOW}  - Приклад: `phone Іван Петров`{DEFALUT}\n" \
                f"{BIRUZA}- `search <запит>`: Пошук контактів за ім'ям, номером телефону, електронною поштою чи адресою.{DEFALUT}\n" \
                f"{YLLOW}  - Приклад: `search Іван`{DEFALUT}\n" \
                f"{BIRUZA}- `email <ім'я_контакту або email>`: Отримати адресу електронної пошти контакту.{DEFALUT}\n" \
                f"{YLLOW}  - Приклад: `email ivan@example.com`{DEFALUT}\n" \
                f"{BIRUZA}- `show`: Показати всі контакти в телефонній книзі.{DEFALUT}\n" \
                f"{YLLOW}  - Приклад: `show`{DEFALUT}\n" \
                f"{BIRUZA}- `birthday <дні>`: Показати найближчі дні народження протягом вказаної кількості днів.{DEFALUT}\n" \
                f"{YLLOW}  - Приклад: `birthday 7`{DEFALUT}\n" \
                f"{BIRUZA}- `close`, `exit`, `good bye`: Вийти з програми.{DEFALUT}\n" \
                f"{YLLOW}  - Приклад: `close`, `exit`, `good bye`{DEFALUT}\n" \
                f"{BIRUZA}- `sorted <шлях_до_папки>`: Впорядкувати файли у вказаній папці.{DEFALUT}\n" \
                f"{YLLOW}  - Приклад: `sorted /шлях/до/папки`{DEFALUT}\n" \
                f"{BIRUZA}- `notes`: Відкрити функціонал заміток.{DEFALUT}\n" \
                f"{YLLOW}  - Приклад: `notes`{DEFALUT}\n" \
                f"{GREEN}    Вітаємо у Контактному Асистенті! Асистент допомагає ефективно керувати вашими нотатками.{DEFALUT}\n" \
                f"{GREEN}    Список доступних команд:{DEFALUT}\n" \
                f"{BIRUZA}    - `1`: Додати нову нотатку.{DEFALUT}\n" \
                f"{YLLOW}       - Приклад: Введіть `1` для додавання нової нотатки та слідуйте інструкціям.{DEFALUT}\n" \
                f"{BIRUZA}    - `2`: Пошук нотаток за заголовком чи змістом.{DEFALUT}\n" \
                f"{YLLOW}       - Приклад: Введіть `2` та введіть запит для пошуку (заголовок чи зміст).{DEFALUT}\n" \
                f"{BIRUZA}    - `3`: Редагувати існуючу нотатку.{DEFALUT}\n" \
                f"{YLLOW}       - Приклад: Введіть `3` для редагування існуючої нотатки та слідуйте інструкціям.{DEFALUT}\n" \
                f"{BIRUZA}    - `4`: Видалити нотатку.{DEFALUT}\n" \
                f"{YLLOW}      - Приклад: Введіть `4` для видалення нотатки та слідуйте інструкціям.{DEFALUT}\n" \
                f"{BIRUZA}    - `5`: Вивести всі нотатки в консоль.{DEFALUT}\n" \
                f"{YLLOW}       - Приклад: Введіть `5` для виведення всіх нотаток в консоль.{DEFALUT}\n" \
                f"{BIRUZA}    - `6`: Вивести нотатку за заголовком.{DEFALUT}\n" \
                f"{YLLOW}       - Приклад: Введіть `6` для виведення конкретної нотатки за заголовком.{DEFALUT}\n" \
                f"{BIRUZA}    - `7`: Вивести нотатку(-и) за тегом.{DEFALUT}\n" \
                f"{YLLOW}       - Приклад: Введіть `7` для виведення нотаток за певним тегом.{DEFALUT}\n" \
                f"{BIRUZA}    - `8`: Вивести нотатки за певними тегами у вигляді таблиці.{DEFALUT}\n" \
                f"{YLLOW}       - Приклад: Введіть `8` для виведення нотаток за певними тегами у вигляді таблиці.{DEFALUT}\n" \
                f"{BIRUZA}    - `9`: Вийти з програми.{DEFALUT}\n" \
                f"{YLLOW}       - Приклад: Введіть `9` для виходу з програми.  {DEFALUT}\n" \
                f"{GREEN}Примітка: Використовуйте подвійні лапки для значень, що містять пробіли.{DEFALUT}\n" \
                f"{GREEN}Бажаємо вам приємного користування Контактним Асистентом!{DEFALUT}\n" 
