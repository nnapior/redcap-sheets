from redcap import Project



def delete_records(id, apiKey):
    print(id)
    project = Project("https://dri.udel.edu/redcap/api/", apiKey)
    project.delete_records([id])


if __name__ == "__main__":
    #delete_records([900])
    pass