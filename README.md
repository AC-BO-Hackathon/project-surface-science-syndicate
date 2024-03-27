[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=14492630)
# Autograding Example: Python
This example project is written in Python, and tested with pytest.

## The assignment
The tests are failing right now because the method isn't outputting the correct string. Fixing this up will make the tests green.

## Setup command

See `postCreateCommand` from [`devcontainer.json`](.devcontainer/devcontainer.json).

## Run command
`pytest`

## Notes
- pip's install path is not included in the PATH var by default, so without installing via `sudo -H`, pytest would be unaccessible.
