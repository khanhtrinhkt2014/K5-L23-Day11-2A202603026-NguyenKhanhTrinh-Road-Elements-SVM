"""Split one CVAT for images 1.1 export holding all 28 images into <name>-front.zip (A..) and <name>-fisheye.zip (B..).

Usage (PowerShell, from the repo folder):
    python split_cvat.py <combined-export.zip> <name>
Example:
    python split_cvat.py "$HOME\\Downloads\\all.zip" nguyenkhanhtrinh

Standard library only. The combined zip is read, never changed.
"""
from __future__ import annotations

import copy
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

SLOT = re.compile(r"^([AB])(\d\d)_")


def read_xml(path: Path) -> bytes:
    if zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as zf:
            names = [n for n in zf.namelist() if n.rsplit("/", 1)[-1] == "annotations.xml"]
            if not names:
                sys.exit(f"{path.name}: khong co annotations.xml - hay export dang CVAT for images 1.1")
            if any(n.lower().endswith((".jpg", ".png", ".jpeg")) for n in zf.namelist()):
                print("Canh bao: zip goc co kem anh; file tach ra se KHONG kem anh (dung yeu cau).")
            return zf.read(names[0])
    return path.read_bytes()


def slot_of(name: str) -> str | None:
    m = SLOT.match(name.replace("\\", "/").rsplit("/", 1)[-1])
    return m.group(1) if m else None


def build(root: ET.Element, keep: str) -> tuple[ET.Element, int]:
    out = copy.deepcopy(root)
    n = 0
    for im in list(out.findall("image")):
        if slot_of(im.get("name", "")) != keep:
            out.remove(im)
        else:
            im.set("id", str(n))
            n += 1
    return out, n


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    src, name = Path(sys.argv[1]), sys.argv[2]
    root = ET.fromstring(read_xml(src))
    if root.tag != "annotations":
        sys.exit("Khong phai file CVAT for images 1.1 (the goc khac <annotations>)")
    images = root.findall("image")
    other = [im.get("name") for im in images if slot_of(im.get("name", "")) is None]
    if other:
        print("Anh khong mang ma A../B.. (bi bo qua):", *other, sep="\n  ")
    for keep, part in (("A", "front"), ("B", "fisheye")):
        tree, n = build(root, keep)
        out = Path(f"{name}-{part}.zip")
        if out.resolve() == src.resolve():
            sys.exit(f"{out} trung voi file goc; doi ten file goc truoc")
        ET.indent(tree)
        xml = '<?xml version="1.0" encoding="utf-8"?>\n' + ET.tostring(tree, encoding="unicode") + "\n"
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
            zf.writestr("annotations.xml", xml)
        print(f"{out}: {n} anh")


if __name__ == "__main__":
    main()
