init -400 python hide:

    media_init_code = ["init -500:"]

    def get_bg(file_name):
        bg_parts = renpy.re.match(r"images/(cg|bg)/([^/]+)/([^.]+)\..+", file_name)
        if bg_parts:
            image_type, label_name, image_name = bg_parts.groups()
            return f'    image {image_type} {label_name} {image_name} = "{file_name}"'
        

    def get_sprite(file_name):
        pass
    def get_music_sound(file_name):
        bg_parts = renpy.re.match(r"audio/(music|sound)/([^.]+)\..+", file_name)
        if bg_parts:
            image_type, image_name = bg_parts.groups()
            return f'    define {image_type}_{image_name} = "{file_name}"'
        
    def get_voice(file_name):
        bg_parts = renpy.re.match(r"audio/voice/([^/]+)/([^/]+)/([^.]+)\..+", file_name)
        if bg_parts:
            label_name, character_name, voice_name = bg_parts.groups()
            return f'    define voice_{label_name}_{character_name}_{voice_name} = "{file_name}"'

    for file_name in renpy.list_files():
        for parser in [get_bg, get_music_sound, get_sprite, get_voice]:
            parser_result = parser(file_name)
            if parser_result:
                media_init_code.append(parser_result)
                continue    
        
        # if file_name.startswith("images/scenes/") and not "/previews/" in file_name:
        #     image_name = file_name.split("/")[-1].split(".")[0]
        #     if "-" in image_name:
        #         continue
        #     if file_name.endswith(".jpg"):

        #         media_init_code.append(
        #             f'    image {image_name} = "{file_name}"'
        #         )

        #     elif file_name.endswith(".webm"):
        #         media_init_code.append(
        #             f'    image {image_name} = Movie(play="{file_name}", loop=True, start_image="{file_name.replace("/"+image_name, "/previews/"+image_name).replace("webm", "jpg")}")'
        #         )


    def save_file():
        code = "\n".join(media_init_code)
        with open(config.basedir+"\\game\\source\\media_init.rpy", "r", encoding="UTF-8") as file:
            if file.read() == code:
                return

        with open(config.basedir+"\\game\\source\\media_init.rpy", "w", encoding="UTF-8") as file:
            file.write(code)

    save_file()