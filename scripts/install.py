#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, shutil
from pathlib import Path

PLUGIN = "wagner-engineering-security"
ENTRY = {
    "name": PLUGIN,
    "source": {"source": "local", "path": f"./plugins/{PLUGIN}"},
    "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
    "category": "Security",
}

def load_marketplace(path: Path) -> dict:
    if not path.exists():
        return {"name": "personal", "interface": {"displayName": "Personal"}, "plugins": []}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data.get("plugins"), list):
        raise SystemExit(f"marketplace inválido: {path}")
    return data

def install_link(src: Path, dst: Path) -> None:
    if dst.is_symlink() or dst.exists():
        if dst.is_symlink() or dst.is_file():
            dst.unlink()
        else:
            shutil.rmtree(dst)
    os.symlink(src, dst, target_is_directory=True)

def install_copy(src: Path, dst: Path) -> None:
    if dst.is_symlink() or dst.is_file():
        dst.unlink()
    elif dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["auto", "symlink", "copy"], default="auto")
    args = ap.parse_args()

    root = Path(__file__).resolve().parents[1]
    src = root / "plugins" / PLUGIN
    if not (src / ".codex-plugin" / "plugin.json").exists():
        raise SystemExit("plugin.json não encontrado")

    home = Path.home()
    dst_root = home / "plugins"
    dst_root.mkdir(parents=True, exist_ok=True)
    dst = dst_root / PLUGIN

    mode = args.mode
    if mode in {"auto", "symlink"}:
        try:
            install_link(src, dst)
            mode = "symlink"
        except OSError:
            if args.mode == "symlink":
                raise
            install_copy(src, dst)
            mode = "copy"
    else:
        install_copy(src, dst)

    mp = home / ".agents" / "plugins" / "marketplace.json"
    mp.parent.mkdir(parents=True, exist_ok=True)
    data = load_marketplace(mp)
    data.setdefault("name", "personal")
    data.setdefault("interface", {"displayName": "Personal"})
    data["plugins"] = [p for p in data["plugins"] if p.get("name") != PLUGIN]
    data["plugins"].append(ENTRY)
    mp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Installed {PLUGIN} via {mode}: {dst}")
    print(f"Marketplace updated: {mp}")

if __name__ == "__main__":
    main()
