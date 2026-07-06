from app.capture.screenshot import capture_window
from app.discord.window import find_discord_window


def main():
    window = find_discord_window()

    if window is None:
        print("Kein Discord-Fenster gefunden.")
        return

    print("Discord gefunden")
    print(f"Titel : {window.title}")
    print(f"Größe : {window.width} x {window.height}")

    screenshot_path = capture_window(window)

    print()
    print("Screenshot gespeichert:")
    print(screenshot_path)


if __name__ == "__main__":
    main()