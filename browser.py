import webbrowser
import json
def browseropen(task):
    link = open("/home/trootech/Jay_Intern/Python_Excerise/AI_MODEL/links.json", "r")
    obj = json.load(link)
    for i in obj["links"]:
        if i in task:
            webbrowser.open(obj["links"][i])
            return f"Opening {i}"
