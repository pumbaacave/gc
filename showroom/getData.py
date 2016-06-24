import pyrebase



config = {
	"apiKey": "AIzaSyBlH4CqBx3r1Mw9W7lfmgV1X_eGeMSF3nE",
	"authDomain": "blueloc.firebaseapp.com",
	"databaseURL": "https://blueloc.firebaseio.com",
	"storageBucket": "project-5482889621425468821.appspot.com",
    "serviceAccount":"blueloc-e70c5cb5c871.json",
};


# retrieve data from firebase, get-back object is 'OrderedDict'

def run():
    firebase = pyrebase.initialize_app(config)
    auth =firebase.auth()
    user = auth.sign_in_with_email_and_password("pumbaacave@yahoo.co.jp", "test123")
    db = firebase.database()
    #data = db.child("auto-update").get(user['idToken'])
    data = db.child("uuid").get(user['idToken'])
    
    return data
    
def getOneRecord(data):
    dict1 = data.val()#OrderedDict under "uuid"
    allRecordOfOneId = dict1.popitem()# tuple [0] is ID,[1] is all record
    allRecord = allRecordOfOneId[1]
    targetDict ={}
    timestamp = 0
    for key,value in allRecord.items():
        tempMilis = value.get("milis",0)
        if tempMilis > timestamp:
            timestamp = tempMilis
            targetDict =value
        
    return targetDict    
    
def printOD(dict):
    for k,v in dict.items():
            print(k,v)
    return
#with urllib.request.urlopen(url) as response:
#   html = response.read()