
from pathlib import Path
import os, shutil, sys, re
from virtual_assistant_v007.colors import *


TRANS = {
        1072: 'a', 1040: 'A', 1073: 'b', 1041: 'B', 1074: 'v', 1042: 'V', 1075: 'g', 1043: 'G', 1076: 'd', 1044: 'D',
        1077: 'e', 1045: 'E', 1105: 'e', 1025: 'E', 1078: 'j', 1046: 'J', 1079: 'z', 1047: 'Z', 1080: 'y', 1048: 'Y',
        1081: 'j', 1049: 'J', 1082: 'k', 1050: 'K', 1083: 'l', 1051: 'L', 1084: 'm', 1052: 'M', 1085: 'n', 1053: 'N', 
        1086: 'o', 1054: 'O', 1087: 'p', 1055: 'P', 1088: 'r', 1056: 'R', 1089: 's', 1057: 'S', 1090: 't', 1058: 'T', 
        1091: 'u', 1059: 'U', 1092: 'f', 1060: 'F', 1093: 'h', 1061: 'H', 1094: 'ts', 1062: 'TS', 
        1095: 'ch', 1063: 'CH', 1096: 'sh', 1064: 'SH', 1097: 'sch', 1065: 'SCH', 1098: '', 1066: '', 1099: 'y', 1067: 'Y', 
        1100: '', 1068: '', 1101: 'e', 1069: 'E', 1102: 'yu', 1070: 'YU', 1103: 'ya', 1071: 'YA', 1108: 'je', 1028: 'JE', 
        1110: 'i', 1030: 'I', 1111: 'ji', 1031: 'JI', 1169: 'g', 1168: 'G'
        } # Словник для транслітерації букв з кирилиці на латиницю

DICT_SUFIXES = {
    '.ZIP': 'archives', '.GZ': 'archives', '.TAR': 'archives', 
    '.AVI': 'video', '.MP4': 'video', '.MOV': 'video', '.MKV': 'video', 
    '.MP3': 'audio', '.OGG': 'audio', '.WAV': 'audio', '.AMR': 'audio', 
    '.DOC': 'documents', '.DOCX': 'documents', '.TXT': 'documents', '.PDF': 'documents', '.XLSX': 'documents', '.PPTX': 'documents', 
    '.JPEG': 'images', '.PNG': 'images', '.JPG': 'images', '.SVG': 'images', 
    'others': 'others'
    }  # Словник в якому в нас записанні як ключі всі наші розширення які потрібно перевірити за умовами завдання а значення якій категорії ці розширення належать. 

SORT_CATEORY = ( 'archives', 'video','audio', 'documents','images', 'others' ) # Список папок в який розсортується наша папка яку сортуємо.

list_name_all_file = [] # Список в який будемо зберігати назвиз розширенням  наших файлів які будуть попадатись в папці яку сортуємо.


def normalize ( file_name ) : # Функція транслітерації .Приймає рядок , повертає новий рядок з заміненими буквами кирилиці на відповідник з словника латиниці. 

    patern = r"\W"
    replace = "_"

    normalize_file_name = re.sub ( patern, replace , file_name )
        
    new_file_name = normalize_file_name.translate(TRANS)

    return  new_file_name


def unpack_archive ( new_path_file_arhive, extract_arhive_dir_name, format_unpack_arhive ) : # Функція розпаковки архівів. Приймає 3 аргумента. Перший -вказівник на файл який треба розархівувати, Другий-папку в яку розархівувати наш файл , Третії - формат розархіватора.
                                                                                             # Якщо архів неможливо розархівувати виводить повідомлення про помилку і видаляє даний архів.
    try : 

        shutil.unpack_archive ( new_path_file_arhive, extract_arhive_dir_name , f'{format_unpack_arhive}' )

    except:
        print(f'Bad arhive was delete <{ new_path_file_arhive }>')

        os.remove( new_path_file_arhive )


def replace_files ( root_path , path_file ) :   # Функція переносить файли з папки де вони є в папку з відповідною категорією. 
                                                # також в ній ми нормалізуємо  назви файлів відповідно до завдання 
                                                # Створюємо папки з відповідними назвами в які будемо преносити наші файли.
                                                # Розархівовуємо архіви з гідно вимог завдання.
                                                # Формуємо список (з нормалізованими назвами ) всіх файлів які нам зустрілись в папці яку сортуємо і повертаємо його з функції.
                                                

    name_file = normalize ( path_file.stem )

    suf_file =  path_file.suffix  

    category = DICT_SUFIXES.get ( suf_file.upper(), 'others' ) 

    new_path_dir = Path ( f'{root_path}/{category}' ) 
    
    

    if not new_path_dir.exists() : 

        new_path_dir.mkdir()    
    

    file_name_curent = f'{name_file}{suf_file}'
    
    list_name_all_file.append( file_name_curent )
                                    
    path_file.replace ( new_path_dir/f"{name_file}{suf_file}" ) #Перенесення файлів в папки з відповідними категоріями.

    if suf_file.upper() in ('.ZIP', '.GZ', '.TAR') :

        new_path_file_arhive = Path ( f'{ new_path_dir }/{ name_file }{ suf_file.lower() }' )
        
        extract_arhive_dir_name = Path (f'{ new_path_dir }/{ name_file }')

        format_unpack_arhive = re.sub (r'\.', '', suf_file.lower() )

        unpack_archive ( new_path_file_arhive, extract_arhive_dir_name, format_unpack_arhive )
    
    return list_name_all_file

def  lists_file_sort ( list_name_all_file , root_path ) :  # Функція отримує Два аргументи . Перший - список всі файлів які потрібно відсортувати відповідно до вимого завдання. Другий - шлях на папку яку сортуємо.
                                                           # Функція за розширенням файла заносить файл з списку в відповдний підсписок .
                                                           # Також формує два Підсписка в одному список всіх розширень які відомі скрипту і список всіх розширень які невідомі скрипту.
                                                           # В кінці створює файл "file_info_in_dir.txt" в папці яку сортує і туди записує всі інормацію згідно вимого завдання.
    list_all_known_sufix = []
    list_all_unknown_sufix = []
    list_file_archives = []
    list_file_video = []
    list_file_audio = []
    list_file_documents = []
    list_file_images = []
    list_file_others = []

    suff_images = ( 'JPEG', 'PNG', 'JPG', 'SVG' )
    suff_video =  ( 'AVI', 'MP4', 'MOV', 'MKV' )
    suff_documents = ( 'DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX' )
    suff_audio = ( 'MP3', 'OGG', 'WAV', 'AMR' )
    suff_arhives = ( 'ZIP', 'GZ', 'TAR' )
  
    

    for name in list_name_all_file :

            suff = name.split('.')
            
            if suff[1].upper() in suff_audio :
            
                list_file_audio.append ( name )
                list_all_known_sufix.append ( suff[1] )

            elif suff[1].upper() in suff_video :
            
                list_file_video.append ( name )
                list_all_known_sufix.append ( suff[1] )
            
            elif suff[1].upper() in suff_documents :
            
                list_file_documents.append ( name )
                list_all_known_sufix.append ( suff[1] )
            
            elif suff[1].upper() in suff_images :
            
                list_file_images.append ( name )
                list_all_known_sufix.append ( suff[1] )
            
            elif suff[1].upper() in suff_arhives :
            
                list_file_archives.append( name )
                list_all_known_sufix.append( suff[1] )
            else :
            
                list_file_others.append ( name )
                list_all_unknown_sufix.append ( suff[1] )
            
    list_all_known_sufix = list ( set ( list_all_known_sufix) )

    list_all_unknown_sufix = list ( set ( list_all_unknown_sufix ) )

    path_info_file = Path(f"{root_path}/file_info_in_dir.txt")
    
    if not path_info_file.is_file() :

        with open (path_info_file , "a") as fh :
            ...

    tab ="\t"*5

    with open ( path_info_file, 'w') as fh :
            fh.writelines( f'\n{tab}Список відомих скрипту розширень, що були в папці :\n\n     {list_all_known_sufix}\n\n')
            fh.writelines( f'{tab}Список невідомих скрипту розширень, що були в папці :\n\n   {list_all_unknown_sufix}\n\n')
            fh.writelines( f'{tab}Список всіх Музичних файлів, що були в папці :\n\n    {list_file_audio}\n\n')
            fh.writelines( f'{tab}Список всіх Відео файлів, що були в папці :\n\n       {list_file_video}\n\n')
            fh.writelines( f'{tab}Список всіх Документ файлів, що були в папці :\n\n    {list_file_documents}\n\n')
            fh.writelines( f'{tab}Список всіх Фото файлів, що були в папці :\n\n        {list_file_images}\n\n')
            fh.writelines( f'{tab}Список всіх Аріхів файлів, що були в папці :\n\n      {list_file_archives}\n\n')
            fh.writelines( f'{tab}Список всіх Невідомих файлів, що були в папці :\n\n   {list_file_others}\n\n')

def sort_dir ( root_path , path ) : #  Функція отримує два парметри. Перший шлях кореневий (шлях до папки яку сортуємо ) і Другий шлях поточної папки оскільки функція буде викликатись рекурсивно то він буде містити  шлях до поточної папки яку перевірямо в даий момент.
                                    #  Алгорим : Проходимось циклом по всіх шляхах (файлах і папках) в папці що сортуємо 
                                                # Перевіряємо : # якщо шлях вказує на папку заходимо в неї рекурсивно  (функція викликає саме себе *sort_dir ( root_path , path ) , де в path буде міститись вже шлях на поточну папку.)
                                                                # якщо шлях вказує на файл переносимо його нашою фінкцією *replace_files ( root_path, item )
                                                                # Так ми пройдемся по всіх підпапкам що знаходяться в нашій папці що сортуємо  і по всіх їхніх підпапках  і їхніх підпапках і так поки всі підпапки незакінчаться.
                                                                # з кожної заберем файли , Нормалізуємо їх назви, перенесем у відповідну папку з запропонованих завданям категорії, Розпакуємо архіви які нам зустрінуться згідно вимого завдання.
                                                                # Всі папки які будуть без файлів і без вкладених папок  будуть видалені.Всі файли з яких перенесем всі файли будуть стануть порожніми і їх тако ж видалемо.
                                                                # Також Ми перевіряємо чи в нашій коріневій папці і її підпапках є папки з назвами вміст яких ми ігноруємо згідно вимог завдання.
                                                # В кінці роботи нашої фінкції *sort_dir ( root_path , path ) в папці що сортуємо ми отримаємо :
                                                            # Перше - Всі підпапки з назвами запропонованих в *SORT_CATEORY для сортування категорій в яких будуть міститись відповідні до категорії файли з нормалізованими назвами згідно вимог завдання.
                                                            # Друге - Файл з назвою "file_info_in_dir.txt" в якій буде міститись інформація яку потрібно зібрати за умовами завдання. 

     
    try :  
     for item in path.iterdir() : 

        
        if item.is_dir() : 

            if not item.stem in SORT_CATEORY :
                
                sort_dir ( root_path , item ) 
           
            if len ( os.listdir ( item ) ) == 0 :
                
                item.rmdir() 
        
        if item.is_file(): 
            
            replace_files ( root_path, item )
    
    except:
       
       pass 
    
    lists_file_sort ( list_name_all_file , root_path)     


# Основная функция
def main(path_str: str = None) -> str:
    '''Основна функція яка буде приймає один аргумент це шлях до папки яку сортуємо
    і запускає весь процес сортування.'''
    

    if path_str is None:
        path_str = sys.argv[1]
    try:
        root_path = Path(path_str)
        path = Path(path_str)

    except IndexError:
        return f"{YLLOW}\n Ви не вели шляху до папки яку будемо сортувати !!!!\n{DEFALUT}"
    if not path.exists():
        return f"{YLLOW}Вказаний Вами шлях {RED}'{path}'{YLLOW} нажаль не існує !!!.\nСпробуйте ще раз.{DEFALUT}"
    
    sort_dir ( root_path , path )
    
    return f"{YLLOW}Всі Ваші папки успішно посортовані !!!\nПосортована папки знаходиться ось тут {PURPURE}{path}{YLLOW}\n\
        Список відсортованих файлів {BIRUZA}'file_info_in_dir.txt'"


if __name__ == "__main__":
    print(main())