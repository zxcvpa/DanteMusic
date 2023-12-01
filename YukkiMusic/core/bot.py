#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import sys

from pyrogram import Client
from pyrogram.types import BotCommand

import config

from ..logging import LOGGER


class YukkiBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"MENGAKTIFKAN BOT")
        super().__init__(
            "DanteMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        try:
            await self.send_message(
                config.LOG_GROUP_ID, "🤖 BOT AKTIF YA KONTOL"
            )
        except:
            LOGGER(__name__).error(
                "Bot gagal mengakses Grup log. Pastikan Anda telah menambahkan bot ke saluran log Anda dan dipromosikan sebagai admin!"
            )
            sys.exit()
        if config.SET_CMDS == str(True):
            try:
                await self.set_bot_commands(
                    [
                        BotCommand("ping", "Periksa apakah bot itu hidup atau mati"),
                        BotCommand("play", "Mulai memutar lagu yang diminta"),
                        BotCommand("skip", "Pindah ke trek berikutnya dalam antrian"),
                        BotCommand("pause", "Jeda lagu yang sedang diputar"),
                        BotCommand("resume", "Lanjutkan lagu yang dijeda"),
                        BotCommand("end", "Hapus antrian dan tinggalkan obrolan suara"),
                        BotCommand("shuffle", "Mengacak daftar putar antrean secara acak."),
                        BotCommand("playmode", "Memungkinkan Anda mengubah mode putar default untuk obrolan Anda"),
                        BotCommand("settings", "Buka pengaturan bot musik untuk obrolan Anda.")
                        ]
                    )
            except:
                pass
        else:
            pass
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error(
                "Harap promosikan Bot sebagai Admin di Grup Logger"
            )
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"🤖 BOT MUSIC DIAKTIFKAN SEBAGAI {self.name}")
        
