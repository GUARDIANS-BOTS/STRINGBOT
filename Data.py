from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

🔥 You Can Use This bot to Generate Pyrogram and Telethon String Season. Use The Below Button to know more!
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔰 Start To Generate String 🔰", callback_data="generate")],
        [InlineKeyboardButton(text=" Back ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔰 Start To Generate String 🔰", callback_data="generate")]
    ]

    support_button = [
        [InlineKeyboardButton("⚜ Support ⚜", url="https://t.me/GuardianSupport_XD")]
    ]
    channels_button = [
        [InlineKeyboardButton("✅ Our Channels & Bots ✅", url="https://t.me/Team_Guardians")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔰 Start To Generate String 🔰", callback_data="generate")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton(" About", callback_data="about")
        ],
        [
            InlineKeyboardButton("🇮🇳 Bot Owner 🇮🇳", url="https://t.me/DinoGuardian"),
            InlineKeyboardButton("⚜ Support ⚜", url="https://t.me/GuardianSupport_XD")
        ],
        [InlineKeyboardButton("✅ Our Channels & Bots ✅", url="https://t.me/Team_Guardians")],
    ]
        

    # Help Message
    HELP = """
» Click the below button or use /generate command to start generating session!
» Click the required button; [Pyrogram/Telethon]
» Enter the required variables when asked.
"""

    # About Message
    ABOUT = """
👨‍💻 **About Me** 

A telegram bot to generate pyrogram and telethon string session...

[Pyrogram](docs.pyrogram.org)
[Telethon](docs.telethon.org)

Language : [Python](www.python.org)
"""
