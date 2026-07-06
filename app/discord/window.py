from dataclasses import dataclass

import psutil
import win32gui
import win32process


@dataclass
class DiscordWindow:
    title: str
    process_name: str
    pid: int
    left: int
    top: int
    width: int
    height: int


def _window_from_handle(hwnd) -> DiscordWindow | None:
    if not win32gui.IsWindowVisible(hwnd):
        return None

    title = win32gui.GetWindowText(hwnd).strip()
    if not title:
        return None

    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    width = right - left
    height = bottom - top

    if width <= 0 or height <= 0:
        return None

    _, pid = win32process.GetWindowThreadProcessId(hwnd)

    try:
        process_name = psutil.Process(pid).name()
    except Exception:
        return None

    if process_name.lower() != "discord.exe":
        return None

    return DiscordWindow(
        title=title,
        process_name=process_name,
        pid=pid,
        left=left,
        top=top,
        width=width,
        height=height,
    )


def find_discord_window() -> DiscordWindow | None:
    found_windows = []

    def callback(hwnd, _):
        try:
            window = _window_from_handle(hwnd)
        except Exception:
            return True

        if window is not None:
            found_windows.append(window)

        return True

    win32gui.EnumWindows(callback, None)

    if not found_windows:
        return None

    return found_windows[0]