def clean_ocr_lines(lines: list[str]) -> list[str]:
    cleaned = []

    for line in lines:
        text = line.strip()

        if not text:
            continue

        if len(text) <= 1:
            continue

        if text in cleaned:
            continue

        cleaned.append(text)

    return cleaned