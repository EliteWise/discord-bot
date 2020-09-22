<div align="center">

# Odyssia Bot

## PEP 8 - Naming Conventions

</div>

| directories | packages  | modules/files  | classes | functions | variables | constants |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| l | l | l + u | cw | l + u | l + u | c + u |

### Legend:

l = lowercase \
u = underscores \
cw = CapWords \
c = CAP

<div align="center">

## Installation

</div>

Clone the project: ```git clone https://gitlab.com/odyssia_dev/odyssia-bot``` \
Create virtual environment and install dependencies:

- ```mkdir venv```
- ```python -m venv venv```
- ```venv\Scripts\activate```
- ```pip install -r requirements.txt```
- [Optionnal] ```deactivate```

<div align="center">

## Branches Conventions

</div>

### How to create a branch?

> On GitLab, you can click on Repository > Branches > New Branch, then give it a name. Your branch need to be created from Develop most of the time.

### How to name my branch?

> Your branch has to follow this naming convention: type/name \
> Example: feature/stats \
> When the name contain multiple words which must be separated, you can use dashes \
> Example: feature/player-stats

### How to merge my branch?

> To merge your changes into develop, you need to create a merge request from GitLab interface. Go on Merge Requests > New merge request > Select a source branch (your branch) + a target branch (often develop), click on compare branch and continue, and then assign your request to a project owner.

<div align="center">

## Dependencies Documentations

</div>

- __**Discord.py**__  → https://discordpy.readthedocs.io/en/latest/api.html
- __**Pdoc**__ → https://medium.com/cemac/simple-documentation-generation-in-python-using-pdoc-16fb86eb5cd5
- __**Git-Secret**__ → https://git-secret.io/
- __**Logging**__ → https://docs.python.org/3/library/logging.html
- __**Unittest**__ → https://docs.python.org/3/library/unittest.html
