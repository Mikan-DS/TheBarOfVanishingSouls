init python:
    about_text = _("""

Эта мрачная, почти мистическая новелла с элементами безумия была создана в рамках конкурса для "Капелла Джема 2". Странные истории и не менее странные их герои уже ждут вас, мои дорогие читатели. 

Состав команды:

Сценарист: Денис Сапунов
Художник: Дарья Мелихова
Программисты: Дядюшка Сэм (Mikan) и Артём Колючий
Команда озвучки Sunset Voice:
Айлин: Лилия Пак
Бармен-рассказчик: Галкин Николай
Садовник: Dima Matveichuk
Крупье: Александра Чернова
Джеймс: Саша Кауфелд
Ричард: Кирилл Балашов
Молодой бармен: Даниил Кушнеров
Игрок: Иван Хроменков

Материалы используемые для музыкального и звукового сопровождения: 
Unseen Horrors - Kevin MacLeod
Zubaida by Breuss Arrizabalaga Quintet
Aberration by 1st Contact
Dances and Dames by Kevin MacLeod
I Knew a Guy by Kevin MacLeo
Faster Does It by Kevin MacLeod
Off to Osaka by Kevin MacLeod
Dances and Dames by Kevin MacLeod
At the End of the Show byJesse Spillane

    """).strip()


screen about():
    tag menu

    use game_menu_framed(_("ОБ ИГРЕ")):
        viewport:
            mousewheel True
            text "[about_text!t]\n\nСделано с помощью {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]"