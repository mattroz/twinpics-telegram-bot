from pathlib import Path


def read_token(path_to_config: Path) -> str:
    with open(path_to_config, 'r') as f:
        token = f.read()
    return token
