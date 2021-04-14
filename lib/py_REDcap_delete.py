from redcap import Project
from lib.py_REDcap_import import getConfig


def delete_records(id):
    config = getConfig()
    project = Project(config["api_url"], config["api_key"])
    project.delete_records(id)


if __name__ == "__main__":
    delete_records([900])
