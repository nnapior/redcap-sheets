from redcap import Project
from redcapImport import getConfig


def delete_records(id):
    config = getConfig()
    project = Project(config["api_url"], config["api_key"])
    response = project.delete_records(id)
    return response

if __name__ == "__main__":
    delete_records([900])

