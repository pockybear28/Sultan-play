# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram import filters
from pyrogram.types import Message

from MusicMan.services.callsmusic.callsmusic import client as USER


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    await USER.send_message(
        message.chat.id,
        "Halo, Saya adalah **Layanan Asistant Sultan Music.**\n\n ❗️ **Rules:**\n   - Jangan Spam Pesan disini\n   - Jangan Spam Lagu Biar Ga Error\n   - Jangan lupq subscribe channel ini @suppmusicquotes \n\n 👉 **KIRIM LINK INVITE ATAU USERNAME GRUP, JIKA ASSISTANT TIDAK DAPAT BERGABUNG DENGAN GRUP ANDA.**\n\n ⛑ **Group Support :** @userbotmaker - **GroupChat :** @RepublicOfCaliber - **Owner** @suppnigga\n\n",
    )
    return
