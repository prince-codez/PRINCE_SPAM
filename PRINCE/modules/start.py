from telethon import __version__, events, Button
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

# ⚡ Stylish Buttons ⚡
START_BUTTON = [
    [Button.inline("⚡ ᴄᴏᴍᴍᴀɴᴅs ⚡", data="help_back")],
    [
        Button.url("📢 ᴄʜᴀɴɴᴇʟ", "https://t.me/SWEETY_BOT_UPDATE"),
        Button.url("💬 sᴜᴘᴘᴏʀᴛ", "https://t.me/APNA_CLUB_09")
    ],
    [Button.url("🔗 ʀᴇᴘᴏ", "https://google.com")]
]

# 🎭 Multiple Bot Instances 🎭
BOT_INSTANCES = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

# 🚀 Command Handler 🚀
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        
        TEXT = f"""
🔹 **ʜᴇʟʟᴏ [{event.sender.first_name}](tg://user?id={event.sender.id})!**  
🔹 **ɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})**   
━━━━━━━━━━━━━━━━━━━━━━━  
🚀 ᴅᴇᴠᴇʟᴏᴘᴇʀ:** [ᴘʀɪɴᴄᴇ](https://t.me/PRINCE_WEBZ)  
💻 xʙᴏᴛꜱ ᴠᴇʀsɪᴏɴ: `M3.3`  
🐍 ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ: `3.11.3`  
📡 ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ: `{__version__}`  
━━━━━━━━━━━━━━━━━━━━━━━
        """
        
        await event.client.send_file(
            event.chat_id,
            "https://i.ibb.co/39WSm9zM/IMG-20250207-080405-192.jpg",
            caption=TEXT, 
            buttons=START_BUTTON
        )

# 🎯 Registering Handler for All Bots 🎯
for bot in BOT_INSTANCES:
    bot.on(events.NewMessage(pattern="/start"))(start)