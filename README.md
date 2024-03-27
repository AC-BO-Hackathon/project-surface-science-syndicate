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
