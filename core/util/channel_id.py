import json


async def get_channel_id_by_command_name(ctx, command_name: str):
    # Opening JSON file
    try:
        with open('core/data/channel_id.json', 'r') as openfile:
            return json.load(openfile)[command_name]
    except KeyError:
        await ctx.send(f"Aucun channel n'a été défini pour la fonctionnalité `{ctx.command.name}`. Utilises `!link {ctx.command.name}` dans le channel de ton choix.")


async def get_channel_id_by_feature_name(feature_name: str):
    # Opening JSON file
    try:
        with open('core/data/channel_id.json', 'r') as openfile:
            return json.load(openfile)[feature_name]
    except KeyError:
        return None