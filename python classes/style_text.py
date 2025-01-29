def st(
    text,
    color=None,
    bg_color=None,
    bold=False,
    italic=False,
    underline=False,
    strikethrough=False,
    invert=False
):
    codes = []

    # Add text effects
    if bold:
        codes.append("1")
    if italic:
        codes.append("3")
    if underline:
        codes.append("4")
    if strikethrough:
        codes.append("9")
    if invert:
        codes.append("7")

    if color:
        codes.append(f"38;2;{color[0]};{color[1]};{color[2]}")

    if bg_color:
        codes.append(f"48;2;{bg_color[0]};{bg_color[1]};{bg_color[2]}")

    style_code = ";".join(codes)
    return f"\033[{style_code}m{text}\033[0m" if codes else text
