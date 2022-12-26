from flask import Flask, request, jsonify, render_template
import os, glob, base64, json

app = Flask(__name__)

if not os.path.exists("annotations"):
    os.mkdir("annotations")
if not os.path.exists("datasets"):
    os.mkdir("datasets")

extent = ["jpg","png"]
def getDataset():
    datasets = []
    for i in extent:
        datasets = datasets + glob.glob(f"datasets/*.{i}")
    for i in datasets:
        with open(i,"rb") as f:
            be = base64.b64encode(f.read())
            yield be.decode('utf-8')+"\t"+i
dataset = [i.split("\t") for i in getDataset()]

@app.route("/")
def index():
    with open(".env") as f:
        env = {i.split("=")[0].strip():i.split("=")[1].replace('"','').replace("'",'').strip() for i in f.read().strip().split("\n") if i}
    return render_template("./index.html", env=env)

def process():
    global generater_dataset
    data = next(generater_dataset, None)
    if data==None:
        generater_dataset = getDataset()
        return process()
    else: 
        return data.split("\t")

@app.route("/save",methods = ["POST"])
def save():
    data = request.get_json()
    print(data)
    for link,points in data.items():
        if not os.path.exists(link):
            continue
        link = link.split("/")[-1].split(".")[0]
        for id_p, p in points.items():
            with open(f"annotations/{link}.jsonl","a", encoding='utf-8') as f:
                json.dump(p, f, ensure_ascii=False)
                f.write('\n')
            print(link,p)
    return jsonify({"type":"success"})

generater_dataset = getDataset()
@app.route("/getImg",methods = ["GET"])
def getImg():
    c = request.args.get('c', '')
    c = int(c)*10 if c else 0
    print(c)
    data={}
    # for i in range(10):
    #     img, link = process()
    #     data[i] = {
    #         "img" : img,
    #         "link" : link
    #     }
    data["data"] = {}
    for i, (img, link) in enumerate(dataset[c:c+10]):
        data["data"][i] = {
            "img" : img,
            "link" : link
        }
        data["max"] = len(dataset)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True,port=8001)