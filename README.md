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
c = caps

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

> Your branch has to follow this naming convention: type/category/name \
> Example: feature/command/stats

### How to merge my branch?

> To merge your changes into develop, you need to create a merge request from GitLab interface. Go on Merge Requests > New merge request > Select a source branch (your branch) + a target branch (often develop), click on compare branch and continue, and then assign your request to a project owner.

<div align="center">

## Dependencies Documentations

</div>

- __**Discord.py**__  → https://discordpy.readthedocs.io/en/latest/api.html
- __**Keyring**__ → https://keyring.readthedocs.io/en/latest/
- __**Logging**__ → https://docs.python.org/3/library/logging.html
- __**Pydoc**__ → https://www.youtube.com/watch?v=URBSvqib0xw
- __**Unittest**__ → https://docs.python.org/3/library/unittest.html
- __**Pdoc**__ → https://pdoc3.github.io/pdoc/doc/pdoc/#gsc.tab=0
