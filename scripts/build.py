"""Build offline demo previews and importable ZIPs. Never reads private config."""
import json
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from trmnl_outside_window.common import clock, packet
from trmnl_outside_window import collector


def build():
    directory = ROOT
    data = collector.demo(clock({}))
    packet(data)
    (directory / ".trmnlp.yml").write_text(json.dumps({"time_zone": "Europe/Prague", "variables": data}))
    for command in ("lint", "build"):
        subprocess.run(["bundle", "exec", "trmnlp", command], cwd=directory, check=True)
    target = ROOT / "dist" / "trmnl-outside-window.zip"
    target.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted((directory / "src").iterdir()):
            if path.suffix in (".liquid", ".yml"):
                archive.write(path, path.name)
    with zipfile.ZipFile(target) as archive:
        assert archive.testzip() is None
        assert "settings.yml" in archive.namelist()
        assert len(archive.namelist()) == 6
    print(f"Ready: {target.name}")


if __name__ == "__main__":
    build()
