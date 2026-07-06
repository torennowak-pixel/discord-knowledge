from app.discord.window import find_discord_window


window = find_discord_window()

if window is None:
    print("Kein Discord gefunden.")
else:
    print("Discord gefunden!")
    print(window)