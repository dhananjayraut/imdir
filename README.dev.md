DEV README

create virtual env
```
python3 -m venv .venv
```

active virtual env
```
source ./.venv/bin/activate
```

install local version
```
pip install -e .
```

install build tools
```
pip install pdoc3 build twine
```

create module documentation
```
pdoc -o docs/ --html ./
```

move documentation to correct place
```
mv docs/imdir.html docs/index.html
```

create builds ready for distribution
```
python3 -m build
```

upload builds to pypi
```
python3 -m twine upload dist/*
```
