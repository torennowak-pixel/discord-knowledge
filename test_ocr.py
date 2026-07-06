from pathlib import Path

from rapidocr_onnxruntime import RapidOCR


def main():
    screenshots_dir = Path("data/screenshots")
    screenshots = sorted(screenshots_dir.glob("*.png"))

    if not screenshots:
        print("Keine Screenshots gefunden.")
        return

    latest_screenshot = screenshots[-1]
    print(f"Nutze Screenshot: {latest_screenshot}")

    ocr = RapidOCR()
    result, _ = ocr(str(latest_screenshot))

    if not result:
        print("Kein Text erkannt.")
        return

    print()
    print("Erkannter Text:")
    print("=" * 80)

    for line in result:
        text = line[1]
        print(text)


if __name__ == "__main__":
    main()