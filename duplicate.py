import json

class duplicate():

    def convert_json(self,file):
        self.file = file
        jsonlist = json.load(file)
        return jsonlist

    def remove_duplicate(self,converted):
        self.converted = converted
        turnedset = set(converted)
        return turnedset

    def write_array(self):
        with open('./links3.json','r+') as f:
            x = self.convert_json(f)
            y = self.remove_duplicate(x)
            setwitch = set(y)
            setlist = list(setwitch)
            with open('./bro.json',"w+") as g:
                json.dump(setlist,g)

if __name__ == "__main__":
   duplicate().write_array();
