import sys
import fontforge


def braille(base_font, fallback_font, output_name):
    
    # assigns the .ttf binary into a var
    v_base = fontforge.open(base_font)
    v_fallback = fontforge.open(fallback_font)
    
    # select braille unicode on fallback_font and yank to clipboard
    v_fallback.selection.select(("ranges", "unicode"), 0x2800, 0x28FF)
    v_fallback.copy()

    # again but paste
    v_base.selection.select(("ranges", "unicode"), 0x2800, 0x28FF)
    v_base.paste()

    v_base.generate(output_name)
    print(f"patched {base_font} to {output_name}")
    
    v_base.close()
    v_fallback.close()


if __name__ == "__main__":
   # check if argc is exactly 4
   # braille_patch base_font fallback_font output_name
    if (len(sys.argv) != 4):
        print("usage: fontforge -script patch.py <base_font> <fallback_font> <output_name>")
        sys.exit(1)
    
    braille(sys.argv[1], sys.argv[2], sys.argv[3])
