# MS.Librarian.Python
Модуль для покиска книг по названию
Поиск ведется по: ReadRate Litres и через Google bookAPI

Текущая версия модуля доспупна как Docker контейнер spiii/lib, разворачиватся на порту 9090

Метод обращения: Get запрос следующего формата на серверр где развернут котейнет
        157.230.108.47:9090/v1.0/{имя ресурса}/{название книги}       
    Для примера:
        157.230.108.47:9090/v1.0/Litres/Маленький принц
        157.230.108.47:9090/v1.0/Google/Python cookbook

Формат ответа:
    json file следующего формата:
        'title':name,                   #название книги
        'status':"found",               #станус (found/not founc)
        'author':'author',              #автор книги 
        'link':link,                    #ссылка на книгу 
        'cover_link':cover_link,        #ссылка на обложку
        'description':descripiton,      #описания книги
        'review':review                 #обзор на книгу
    
    в зависимости от источника некоторые поля могут пока что отсутствовать
                
