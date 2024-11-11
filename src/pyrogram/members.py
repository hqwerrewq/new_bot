from client import client


async def pyro_get_chat_members(chat_id):
    member_user_name = []
    async for member in client.get_chat_members(chat_id):
        if member.user.is_bot:
            continue
        member_user_name.append(member.user.username)
    return member_user_name
#