import gifos


def main():
    t = gifos.Terminal(width=760, height=240, xpad=15, ypad=15)

    t.gen_text("", 1, count=8)

    t.gen_prompt(1, count=5)
    t.gen_typing_text("whoami", 1, contin=True)
    t.gen_text("\x1b[95mKarla Tovar\x1b[0m / software engineer / mexico city", 2, count=12)

    t.gen_prompt(4, count=5)
    t.gen_typing_text("cat stack", 4, contin=True)
    t.gen_text("react  next.js  typescript  tailwind  swiftui", 5, count=12)

    t.gen_prompt(7, count=5)
    t.gen_typing_text("cat focus", 7, contin=True)
    t.gen_text("frontend engineering, product thinking", 8, count=12)

    t.gen_prompt(10, count=5)
    t.gen_text("", t.curr_row, count=60, contin=True)

    t.gen_gif()


if __name__ == "__main__":
    main()