from datetime import datetime
from pathlib import Path

import mss
from PIL import Image

from app.discord.window import DiscordWindow


def capture_window(
    window: DiscordWindow,
    output_dir: str = "data/screenshots",
) -> Path:
    """
    Erstellt einen Screenshot des angegebenen Discord-Fensters.

    Args:
        window: Das gefundene Discord-Fenster.
        output_dir: Ordner, in dem der Screenshot gespeichert wird.

    Returns:
        Path zur gespeicherten PNG-Datei.
    """

    if window is None:
        raise ValueError("window darf nicht None sein.")

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    filename = datetime.now().strftime("discord-%Y%m%d-%H%M%S.png")
    file_path = output_path / filename

    region = {
        "left": window.left,
        "top": window.top,
        "width": window.width,
        "height": window.height,
    }

    with mss.mss() as sct:
        screenshot = sct.grab(region)
        image = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
        image.save(file_path)

    return file_path