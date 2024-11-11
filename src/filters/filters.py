async def admins_filter(msg, bot):
    user = await bot.get_chat_member(msg.chat.id, msg.from_user.id)
    if user.status == user.status.ADMINISTRATOR or user.status == user.status.CREATOR:
        return True
    else:
        return False


async def member_filter(msg, bot):
    user = await bot.get_chat_member(msg.chat.id, msg.from_user.id)
    if (user.status == user.status.MEMBER or
            user.status == user.status.ADMINISTRATOR or
            user.status == user.status.CREATOR):
        return True
