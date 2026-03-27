Patch brailes to Monaco for ASCII arts
## BnA
<img width="1920" height="1080" alt="Screenshot 2026-03-27 230448" src="https://github.com/user-attachments/assets/325eb240-f7ff-441a-a91b-9e3ffd6fda96" />
<img width="1920" height="1080" alt="Screenshot 2026-03-28 000250" src="https://github.com/user-attachments/assets/99c7bbe6-e97f-4739-87a4-ff39032da7d1" />


## Prerequisites
- python3 and fontforge
  ```bash
  sudo apt install fontforge python3-fontforge```
- DejaVuSans.ttf (only works with this and Maple Mono (though their brailles don't work too well with Monaco), tested JetBrainsMonoNerdFont-Regular.ttf, JetBrainsMonoNerdFont-ExtraBold.ttf, DejaVuSansMNerdFont-Bold.ttf, DejaVuSansMNerdFontMono-Regular.ttf)
- Ligaturized version of [thep0y/monaco-nerd-font](https://github.com/thep0y/monaco-nerd-font) 

## Usage
with all of the required fonts in one folder, run `patch.sh`

alternatively, 
```bash
fontforge -script patch.py <base_font.ttf> <braille_fallback.ttf> <output_name.ttf>```

