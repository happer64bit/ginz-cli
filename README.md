![Logo](https://raw.githubusercontent.com/happer64bit/ginz-cli/dev/assets/ginz.webp)

# Ginz

Ginz is a command-line tool for cloning multiple repositories from GitHub based on a configuration file. It simplifies the process of cloning multiple repositories by allowing you to specify the repositories and their branches in a single configuration file.

## Features

- Clones multiple repositories from GitHub.
- Supports specifying the branch for each repository.
- Provides progress updates during the cloning process. (Coming)
- Easy-to-use command-line interface.(Coming)
- Customizable through a configuration file.

## Installation

1. Ensure that Python 3.x is installed on your system.
2. Open a terminal or command prompt.
3. Run the following command to install Ginz:

### Via `pip`

```sh
pip install git+https://github.com/happer64bit/ginz-cli
```

## Usage

1. Create a configuration file named `Ginz.toml` in the desired directory. The file should be in the TOML format.
2. Add repository entries to the configuration file in the following format:

```toml
[repository-name]
source = "https://github.com/username/repository-name"
branch = "main"
```

Replace `[repository-name]` with a unique name for each repository, `source` with the GitHub repository URL, and `branch` with the desired branch name (optional, defaults to "main").

3. Open a terminal or command prompt.
4. Navigate to the directory containing the `Ginz.toml` configuration file.
5. Run the following command to start the cloning process:

```
ginz
```

Ginz will read the configuration file, clone the specified repositories, and display progress updates during the cloning process.

## Options

Ginz supports the following command-line options:

- `--version` or `-v`: Prints the version of Ginz.
- `--help` or `-h`: Displays help information and usage instructions.
- `--refetch` : Update All Repo in `Ginz.toml`
- `--config-url <url>` : Fetch Config and run

## Example

Let's assume you have the following `Ginz.toml` configuration file:

```toml
[project-a]
source = "https://github.com/user-a/project-a"
branch = "main"

[project-b]
source = "https://github.com/user-b/project-b"
branch = "development"
```

Running the command `gint` in the directory containing the `Ginz.toml` file will clone `project-a` from the `main` branch and `project-b` from the `development` branch.
