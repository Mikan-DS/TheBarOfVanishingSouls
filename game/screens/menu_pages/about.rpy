init python:
    about_text = _("""

Ресурсы:

Вступление: Unseen Horrors - Kevin MacLeod (авторское право - Creative Commons CC BY 3.0) -
https://www.chosic.com/download-audio/27249/
Звук открывания двери: w.forster.1@gmail.com - https://opengameart.org/content/creaky-door-
hinge-spooky
Звук перетасовывания карт (в игре обрезанная версия от оригинала): Kenney -
https://opengameart.org/content/54-casino-sound-effects-cards-dice-chips
Звук дождя из вступления (в игре немного видоизменён): WuxiaScrub -
https://opengameart.org/content/rain-long-thunder
Щелчок пистолета (слегка обрезана дорожка):
Elmarp - https://freesound.org/people/Elmarp/sounds/367000/
Звук выстрела (частично обрезан): newlocknew -
https://freesound.org/people/newlocknew/sounds/713017/
Наливание бренди: Mish7913 - https://freesound.org/people/Mish7913/sounds/741348/
Один из треков в бар: Zubaida by Breuss Arrizabalaga Quintet
https://freemusicarchive.org/music/Breuss_Arrizabalaga_Quintet/Nfamoudou-Boudougou/03_-
_breuss_arrizabalaga_quintet_-_zubaida/ (пока под вопросом)
Aberration by1st Contact (CC BY-SA) -
https://freemusicarchive.org/music/1st-contact/single/aberration/
Dances and Dames by Kevin MacLeod -
https://freemusicarchive.org/music/Kevin_MacLeod/Jazz_Sampler/Dances_and_Dames_1428/
I Knew a Guy by Kevin MacLeod -
https://freemusicarchive.org/music/Kevin_MacLeod/Jazz_Sampler/I_Knew_a_Guy/
Faster Does It by Kevin MacLeod -
https://freemusicarchive.org/music/Kevin_MacLeod/Jazz_Sampler/Faster_Does_It/
Off to Osaka by Kevin MacLeod -
https://freemusicarchive.org/music/Kevin_MacLeod/Jazz_Sampler/Off_to_Osaka_1502/
Dances and Dames by Kevin MacLeod -
https://freemusicarchive.org/music/Kevin_MacLeod/Jazz_Sampler/Dances_and_Dames/
At the End of the Show byJesse Spillane - https://freemusicarchive.org/music/Jesse_Spillane/the-
meeting-place/at-the-end-of-the-show/



    """).strip()


screen about():
    tag menu

    use game_menu_framed(_("ОБ ИГРЕ")):
        viewport:
            mousewheel True
            text "[about_text!t]\n\nСделано с помощью {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]"