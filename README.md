Patch brailes to Monaco for ASCII arts


## BnA Example
<img width="1920" height="1080" alt="Screenshot 2026-03-27 230541" src="https://github.com/user-attachments/assets/400db7f8-b107-4f2e-950b-eb841cc0807c" />

<img width="1920" height="1080" alt="Screenshot 2026-03-28 000250" src="https://github.com/user-attachments/assets/99c7bbe6-e97f-4739-87a4-ff39032da7d1" />
[source]([https://github.com/kernelSlvt/dotfiles/](https://github.com/kernelSlvt/dotfiles/blob/main/.config/nvim/lua/plugins)

## Prerequisites
- python3 and fontforge
  ```bash
  sudo apt install fontforge python3-fontforge
- [DejaVuSans.ttf](https://dejavu-fonts.github.io) (only works with this and [Maple Mono](https://github.com/subframe7536/maple-font) (though their brailles don't work too well with Monaco), tested JetBrainsMonoNerdFont-Regular.ttf, JetBrainsMonoNerdFont-ExtraBold.ttf, DejaVuSansMNerdFont-Bold.ttf, DejaVuSansMNerdFontMono-Regular.ttf)
- Ligaturized version of [Monaco NF](https://github.com/thep0y/monaco-nerd-font) 

## Usage
with all of the required fonts in one folder, run `patch.sh`


alternatively, manually patch each file with
```bash
fontforge -script patch.py <base_font.ttf> <braille_fallback.ttf> <output_name.ttf>

