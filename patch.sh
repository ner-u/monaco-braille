#!/bin/bash

fallback_font="DejaVuSans.ttf"

# new result variable
out_dir="patched_fonts"

# if doesn't exist,
mkdir -p "$out_dir"

for base_font in MonacoLigaturized*.ttf; do
  out_name="${out_dir}/${base_font}"

  echo "patching ${base_font}..."
  fontforge -script patch.py "$base_font" "$fallback_font" "$out_name"
done

echo "finished"
