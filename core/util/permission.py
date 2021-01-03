async def is_admin(ctx):
    return ctx.message.author.guild_permissions.administrator