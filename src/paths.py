from pathlib import Path
import yaml

def data_root() -> Path:
    cfg = Path(__file__).resolve().parents[1] / "configs" / "paths.yaml"
    with cfg.open("r", encoding="utf-8") as f:
        y = yaml.safe_load(f)
    return Path(y["DATA_ROOT"])

DATA_ROOT = data_root()
