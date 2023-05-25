async def startGame(bot,event):
    back_msg = "you have enter xiuxian world"
    
    await bot.call_api('send_group_msg', **{
        'group_id': event.group_id,
        'message': back_msg
    })