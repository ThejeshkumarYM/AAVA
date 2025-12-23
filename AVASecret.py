_secrets = {
    "GITHUB_TOKEN": "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"
}

def getValue(key: str):
    return _secrets.get(key)
