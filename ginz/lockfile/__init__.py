import toml

class LockFile:
    def __init__(self, lockFile=None):
        if lockFile is None:
            lockFile = "ginz-lock.toml"
        self.lockFile = lockFile

    def write(self, outputFolder: str, source: str, branch: str, last_modified: str):
        # Implement the logic for writing TOML here
        toml_data = {
            'outputFolder': outputFolder,
            'source': source,
            'branch': branch,
            'last_modified': last_modified
        }
        with open(self.lockFile, 'w') as f:
            toml.dump(toml_data, f)

    def read(self):
        # Implement the logic for reading TOML here
        with open(self.lockFile, 'r') as f:
            toml_data = toml.load(f)
        return toml_data