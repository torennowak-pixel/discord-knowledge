import psutil
import win32gui
import win32process


def inspect_window(hwnd):
    if not win32gui.IsWindowVisible(hwnd):
        return

    title = win32gui.GetWindowText(hwnd).strip()
    if not title:
        return

    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    width = right - left
    height = bottom - top

    _, pid = win32process.GetWindowThreadProcessId(hwnd)

    try:
        process_name = psutil.Process(pid).name()
    except Exception:
        process_name = "<unknown>"

    class_name = win32gui.GetClassName(hwnd)

    print("=" * 80)
    print(f"Title   : {title}")
    print(f"Process : {process_name}")
    print(f"PID     : {pid}")
    print(f"Class   : {class_name}")
    print(f"Pos     : left={left}, top={top}")
    print(f"Size    : {width} x {height}")


def main():
    print("=" * 80)
    print("Win32 Visible Windows")
    print("=" * 80)

    win32gui.EnumWindows(lambda hwnd, _: inspect_window(hwnd), None)


if __name__ == "__main__":
    main()