import json


class FileDealer:
    def __init__(self):
        self.hello = "world"

    # TXT PART:
    def save_message(self, notification):
        with open("./FILES/Info.txt", "w") as info:
            info.write(f"{notification}")
            info.close()

    def get_message(self):
        with open("./FILES/Info.txt", "r") as msg:
            result = msg.read()
            msg.close()
        return result

    # JSON PART:
    def create_json_file(self):
        dictionary = {
            "chincho2022@yahoo.com": {
                "name": "Nika",
                "surname": "Chinchaladze"
            }
        }
        with open("./FILES/data.json", "w") as docs:
            json.dump(dictionary, docs, indent=4)
            docs.close()

    def update_json(self, email, name, surname):
        new_data = {
            email: {
                "name": name,
                "surname": surname
            }
        }
        try:
            with open("./FILES/data.json", "r") as docs:
                output = json.load(docs)
                output.update(new_data)
                docs.close()
        except json.decoder.JSONDecodeError:
            self.create_json_file()
        else:
            with open("./FILES/data.json", "w") as docs:
                json.dump(output, docs, indent=4)
                docs.close()

    def read_json(self):
        with open("./FILES/data.json", "r") as docs:
            output = json.load(docs)
            docs.close()
            answer = [item for item in output.keys()]
            return answer

    def return_wanted_user(self, email):
        with open("./FILES/data.json", "r") as docs:
            output = json.load(docs)
            docs.close()
            return output[email]
