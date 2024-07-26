# Noscemus Database - ETL

---

## Authors

* Vojtěch Kaše

## License

CC-BY-SA 4.0, see attached License.md

---

# Description

This repository serves for extraction, preprocessing and exploration of the textual data and metadata from the Noscemus database ([website](https://wiki.uibk.ac.at/noscemus/Main_Page)). It also trains word vector representations on this dataset. This repository is part of the [TOME project](https://tome.flu.cas.cz).

# Getting started

```bash
git clone [url-of-the-git-file]
cd [name-of-the-repo]
# (recommendation: create and activate a virtual environement)
pip install -r requirements.txt
```

We reccomend to use a dedicated virtual environment for the whole project:

```bash
python3 -m venv noscemus_venv # or specify your own source python to replicate (e.g. python3.12 etc.)
noscemus_venv/bin/python -m pip install --upgrade pip
noscemus_venv/bin/python -m pip install -r requirements.txt
noscemus_venv/bin/python -m ipykernel install --user -name=noscemus_kernel # create the jupyter kernel to be used by the notebooks
echo "/noscemus_venv/" >> .gitignore # add the virtual_venv directory to .gitignore, to prevents its synchronization via github
```

Anytime you need to install another package, run `noscemus_venv/bin/python -m pip install <package-name>` or have the environment activated: `source noscemus_venv/bin/activate`.

Finally, go to the `scripts` directory and run the Jupyter notebooks you wish;-).

---

## Scripts

The scripts are in the `scripts` subfolder and their numbers and titles should be self-explanatory. Usually, they have the form of Jupyter notebooks.
