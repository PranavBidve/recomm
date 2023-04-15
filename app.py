from contextlib import redirect_stderr
from operator import methodcaller
from pickletools import read_uint1
from wsgiref.util import request_uri
from flask import Flask, request, jsonify, render_template, request, redirect, url_for
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('C:\\Users\\bidve\\Downloads\\VIT Downloads\\TARP\\Path Recommender\\University_Path_Recommender.pkl','rb'))
# model = pickel.load(open("C:\Users\bidve\Downloads\VIT Downloads\TARP\Real-Estate-Price-Prediction-of-Bangalore-City\Path Recommender\University_Path_Recommender.pkl"))
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    if(request.method == 'POST'):
        area = 2
        bhk = 2
        bath = 4
        location = request.form['location']
      
        data_columns= ["total_sqft", "bath", "bhk", "1st block jayanagar", "1st phase jp nagar", "2nd phase judicial layout", "2nd stage nagarbhavi", "5th block hbr layout", "5th phase jp nagar", "6th phase jp nagar", "7th phase jp nagar", "8th phase jp nagar", "9th phase jp nagar", "aecs layout", "abbigere", "akshaya nagar", "ambalipura", "ambedkar nagar", "amruthahalli", "anandapura", "ananth nagar", "anekal", "anjanapura", "ardendale", "arekere", "attibele", "beml layout", "btm 2nd stage", "btm layout", "babusapalaya", "badavala nagar", "balagere", "banashankari", "banashankari stage ii", "banashankari stage iii", "banashankari stage v", "banashankari stage vi", "banaswadi", "banjara layout", "bannerghatta", "bannerghatta road", "basavangudi", "basaveshwara nagar", "battarahalli", "begur", "begur road", "bellandur", "benson town", "bharathi nagar", "bhoganhalli", "billekahalli", "binny pete", "bisuvanahalli", "bommanahalli", "bommasandra", "bommasandra industrial area", "bommenahalli", "brookefield", "budigere", "cv raman nagar", "chamrajpet", "chandapura", "channasandra", "chikka tirupathi", "chikkabanavar", "chikkalasandra", "choodasandra", "cooke town", "cox town", "cunningham road", "dasanapura", "dasarahalli", "devanahalli", "devarachikkanahalli", "dodda nekkundi", "doddaballapur", "doddakallasandra", "doddathoguru", "domlur", "dommasandra", "epip zone", "electronic city", "electronic city phase ii", "electronics city phase 1", "frazer town", "gm palaya", "garudachar palya", "giri nagar", "gollarapalya hosahalli", "gottigere", "green glen layout", "gubbalala", "gunjur", "hal 2nd stage", "hbr layout", "hrbr layout", "hsr layout", "haralur road", "harlur", "hebbal", "hebbal kempapura", "hegde nagar", "hennur", "hennur road", "hoodi", "horamavu agara", "horamavu banaswadi", "hormavu", "hosa road", "hosakerehalli", "hoskote", "hosur road", "hulimavu", "isro layout", "itpl", "iblur village", "indira nagar", "jp nagar", "jakkur", "jalahalli", "jalahalli east", "jigani", "judicial layout", "kr puram", "kadubeesanahalli", "kadugodi", "kaggadasapura", "kaggalipura", "kaikondrahalli", "kalena agrahara", "kalyan nagar", "kambipura", "kammanahalli", "kammasandra", "kanakapura", "kanakpura road", "kannamangala", "karuna nagar", "kasavanhalli", "kasturi nagar", "kathriguppe", "kaval byrasandra", "kenchenahalli", "kengeri", "kengeri satellite town", "kereguddadahalli", "kodichikkanahalli", "kodigehaali", "kodigehalli", "kodihalli", "kogilu", "konanakunte", "koramangala", "kothannur", "kothanur", "kudlu", "kudlu gate", "kumaraswami layout", "kundalahalli", "lb shastri nagar", "laggere", "lakshminarayana pura", "lingadheeranahalli", "magadi road", "mahadevpura", "mahalakshmi layout", "mallasandra", "malleshpalya", "malleshwaram", "marathahalli", "margondanahalli", "marsur", "mico layout", "munnekollal", "murugeshpalya", "mysore road", "ngr layout", "nri layout", "nagarbhavi", "nagasandra", "nagavara", "nagavarapalya", "narayanapura", "neeladri nagar", "nehru nagar", "ombr layout", "old airport road", "old madras road", "padmanabhanagar", "pai layout", "panathur", "parappana agrahara", "pattandur agrahara", "poorna pragna layout", "prithvi layout", "r.t. nagar", "rachenahalli", "raja rajeshwari nagar", "rajaji nagar", "rajiv nagar", "ramagondanahalli", "ramamurthy nagar", "rayasandra", "sahakara nagar", "sanjay nagar", "sarakki nagar", "sarjapur", "sarjapur  road", "sarjapura - attibele road", "sector 2 hsr layout", "sector 7 hsr layout", "seegehalli", "shampura", "shivaji nagar", "singasandra", "somasundara palya", "sompura", "sonnenahalli", "subramanyapura", "sultan palaya", "tc palaya", "talaghattapura", "thanisandra", "thigalarapalya", "thubarahalli", "tindlu", "tumkur road", "ulsoor", "uttarahalli", "varthur", "varthur road", "vasanthapura", "vidyaranyapura", "vijayanagar", "vishveshwarya layout", "vishwapriya layout", "vittasandra", "whitefield", "yelachenahalli", "yelahanka", "yelahanka new town", "yelenahalli", "yeshwanthpur"]   
    #    
        # loc_index = data_columns.index(location)
    
        
    
        x = np.zeros(len(data_columns))
        # x[0] = area
        # x[1] = bath
        # x[2] = bhk
    
        # if(loc_index>=0):
        #    x[loc_index] = 1

        output = round(model.predict([x])[0], 2)  

        if output<0:            
           return render_template('index.html')

           
        output = "Working as a Senior Manager at McKinsey & Company typically requires an advanced degree, several years of consulting experience, and a strong track record of delivering high-quality results for clients. The role involves leading client engagements, managing teams, developing new business opportunities, and earning a competitive salary with performance-based bonuses and benefits. The company places a strong emphasis on training, development, and work-life balance.";        
        output1 = "Pursue an undergraduate degree in a related field such as business, economics, or engineering";
        output2 = "Gain work experience in consulting or a related field through internships"; 
        output3 = "Consider pursuing an advanced degree such as an MBA or PhD to enhance your skills and credentials";       
        output4 = "Network with current and former McKinsey & Company employees to learn potential career opportunities";       
        output5 = "Apply for an entry-level position at McKinsey & Company";       
        output6 = "Gain experience in managing teams and leading client engagements to prepare for a Senior Manager role";       
        output7 = "Consider pursuing additional training and development opportunities offered by McKinsey & Company";       
        output8 = "Apply for a Senior Manager position at McKinsey & Company";    
        # 
        # output = "Candidates interested in applying for judicial positions in the Maharashtra High Court can visit the official website of the High Court or the website of the Maharashtra Public Service Commission (MPSC) for more information. The notification for the recruitment process is usually advertised in leading newspapers and on the official websites."
        # output1 = "Complete your education: You will need to have a law degree from a recognized university."
        # output2 = "Gain experience as an advocate: After completing your law degree, need to practice as an advocate for at least 10 years."
        # output3 = "Stay updated: As an advocate, you should stay updated on the latest legal developments."
        # output4 = "Qualify in the Judicial Service Examination: conducted by the Maharashtra Public Service Commission."
        # output5 = "Clear the Interview: After qualifying in the written examination, you will need to clear the interview."
        # output6 = "Get appointed as a Civil Judge: Once you clear the examination and interview, you may be appointed as a civil judge."
        # output7 = "Get promoted to higher positions: After gaining experience, you may be considered for promotion to higher positions."
        # output8 = "Get appointed as a High Court Judge: Based on merit and seniority, you may be appointed as a judge in the Maharashtra High Court."   
    return render_template('index.html', prediction_text =  "{}".format(output),  o1 =  "{}".format(output1),  o2 =  "{}".format(output2),  o3 =  "{}".format(output3),  o4 =  "{}".format(output4),  o5 =  "{}".format(output5),  o6 =  "{}".format(output6),  o7 =  "{}".format(output7),  o8 =  "{}".format(output8))
          
                
        
   



if __name__=='__main__':
    app.run(debug = True)  
