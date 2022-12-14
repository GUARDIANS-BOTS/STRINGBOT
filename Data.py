from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

๐ฅ You Can Use This bot to Generate Pyrogram and Telethon String Season. Use The Below Button to know more!
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("๐ฐ Start To Generate String ๐ฐ", callback_data="generate")],
        [InlineKeyboardButton(text=" Back ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("๐ฐ Start To Generate String ๐ฐ", callback_data="generate")]
    ]

    support_button = [
        [InlineKeyboardButton("โ Support โ", url="https://t.me/GuardianSupport_XD")]
    ]
    channels_button = [
        [InlineKeyboardButton("โ Our Channels & Bots โ", url="https://t.me/Team_Guardians")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("๐ฐ Start To Generate String ๐ฐ", callback_data="generate")],
        [
            InlineKeyboardButton("How to Use โ", callback_data="help"),
            InlineKeyboardButton(" About", callback_data="about")
        ],
        [
            InlineKeyboardButton("๐ฎ๐ณ Bot Owner ๐ฎ๐ณ", url="https://t.me/DinoGuardian"),
            InlineKeyboardButton("โ Support โ", url="https://t.me/GuardianSupport_XD")
        ],
        [InlineKeyboardButton("โ Our Channels & Bots โ", url="https://t.me/Team_Guardians")],
    ]
        

    # Help Message
    HELP = """
ยป Click the below button or use /generate command to start generating session!
ยป Click the required button; [Pyrogram/Telethon]
ยป Enter the required variables when asked.
"""

    # About Message
    ABOUT = """
๐จโ๐ป **About Me** 

A telegram bot to generate pyrogram and telethon string session...

[Pyrogram](docs.pyrogram.org)
[Telethon](docs.telethon.org)

Language : [Python](www.python.org)
"""
