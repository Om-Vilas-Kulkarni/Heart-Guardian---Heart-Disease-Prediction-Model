import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def checkup():

    def finalresults(p_age, p_gender, p_cp, p_rbps, p_chol, p_fbs, p_ecg, p_exang, p_slope, p_fluoroscopy,p_thal):
        result = model.predict([[p_age, p_gender, p_cp, p_rbps, p_chol, p_fbs, p_ecg, p_exang, p_slope, p_fluoroscopy, p_thal]])
        if result == 1:
            print(f"Result: The analysis shows that age {p_age} is a {agerisk} factor, while the {p_chol}mg/dl cholesterol seems {chol_ind} level. The {p_rbps}bps indicates {bps_ind} range along with {pain} type contributes to potential risk. Although {fbs_ind} could be less concerning, but the {ecg_ind} and {exang_ind} are strong indicating factors. Additionally, the presence of {pslope_ind}, {fluoro_ind} and the patient seems to have {thal_ind}. All these factors contribute to a risk profile. These combined findings highlights the person has heart disease. However, I am just a machine learning model and could be inaccurate, I'm still learning through datasets. It's better to consult a doctor before reaching to conclusion. Thank you!")
            speak(f"The analysis shows that age {p_age} is a {agerisk} factor, while the {p_chol}mg/dl cholesterol seems {chol_ind} level. The {p_rbps}bps indicates {bps_ind} range along with {pain} type contributes to potential risk. Although {fbs_ind} could be less concerning, but the {ecg_ind} and {exang_ind} are strong indicating factors. Additionally, the presence of {pslope_ind}, {fluoro_ind} and the patient seems to hav {thal_ind}. All these factors contribute to a risk profile. These combined findings highlights the person has heart disease. However, I am just a machine learning model and could be inaccurate, I'm still learning through datasets. It's better to consult a doctor before reaching to conclusion. Thank you!")

        elif result == 0:
            print(f"Result: The analysis shows that age {p_age} is a {agerisk} factor, while the {p_chol}mg/dl cholesterol seems {chol_ind} level. The {p_rbps}bps indicates {bps_ind} range along with {pain} type contributes to less potential risk. Although {fbs_ind} could be less concerning, but the {ecg_ind} and {exang_ind} are strong indicating factors. However, the presence of {pslope_ind}, {fluoro_ind} and the patient seems to have {thal_ind}, seems out to be a moderate risk. All these factors indicate a low risk profile. These combined findings highlights the person may not have heart disease. However, I am just a machine learning model and could be inaccurate, I am still learning through datasets. It's better to consult a doctor before reaching to conclusion. Thank you!")
            speak(f"The analysis shows that age {p_age} is a {agerisk} factor, while the {p_chol}mg/dl cholesterol seems {chol_ind} level. The {p_rbps}bps indicates {bps_ind} range along with {pain} type contributes to less potential risk. Although {fbs_ind} could be less concerning, but the {ecg_ind} and {exang_ind} are strong indicating factors. However, the presence of {pslope_ind}, {fluoro_ind} and the patient seems to have {thal_ind}, seems out to be a moderate risk. All these factors indicate a low risk profile. These combined findings highlights the person may not have heart disease. However, I am just a machine learning model and could be inaccurate, I am still learning through datasets. It's better to consult a doctor before reaching to conclusion. Thank you!")

    def checkthal(p_age, p_gender, p_cp, p_rbps, p_chol, p_fbs, p_ecg, p_exang, p_slope, p_fluoroscopy):
        speak("Finally, what is patient's thalassemia type?")
        p_thal = int(input("\nEnter Paitent's Thalassemia:-\nNormal=0\nFixed Defect=1\nReversible Defect=2\nResponse:"))
        if p_thal == 0:
            global thal_ind
            thal_ind = "Normal Haemoglobin levels"
            finalresults(p_age, p_gender, p_cp, p_rbps, p_chol, p_fbs, p_ecg, p_exang, p_slope, p_fluoroscopy, p_thal)
        elif p_thal == 1:
            thal_ind = "Fixed Thalassemia"
            finalresults(p_age, p_gender, p_cp, p_rbps, p_chol, p_fbs, p_ecg, p_exang, p_slope, p_fluoroscopy, p_thal)
        elif p_thal == 2:
            thal_ind = "Reversible Thalassemia"
            finalresults(p_age, p_gender, p_cp, p_rbps, p_chol, p_fbs, p_ecg, p_exang, p_slope, p_fluoroscopy,p_thal)
        else:
            speak("Invalid Input!")
            checkthal(p_age, p_gender, p_cp, p_rbps, p_chol, p_fbs, p_ecg, p_exang, p_slope, p_fluoroscopy)

    def checkfluoro(p_age, p_gender, p_cp, p_rbps, p_chol, p_fbs, p_ecg, p_exang, p_slope):
        speak("Thank you. How many major vessels (ranging from 0 to 3) are colored by fluoroscopy?")
        p_fluoroscopy = int(input("\nNumber of major vessels (0-3) colored by fluoroscopy:"))
        if p_fluoroscopy == 0:
            global fluoro_ind
            fluoro_ind = "Fluoroscopy indicates no blockage"
            checkthal(p_age, p_gender, p_cp, p_rbps, p_chol, p_fbs, p_ecg, p_exang, p_slope, p_fluoroscopy)
        elif p_fluoroscopy == 1:
            fluoro_ind = "Fluoroscopy indicates 1 blockage"
            checkthal(p_age, p_gender, p_cp, p_rbps, p_chol, p_fbs, p_ecg, p_exang, p_slope, p_fluoroscopy)
        elif p_fluoroscopy > 1:
            fluoro_ind = f"Fluoroscopy indicates {p_fluoroscopy} blockages"
            checkthal(p_age, p_gender, p_cp, p_rbps, p_chol, p_fbs, p_ecg, p_exang, p_slope, p_fluoroscopy)
        else:
            speak("Invalid Input!")
            checkfluoro(p_age, p_gender, p_cp, p_rbps, p_chol, p_fbs, p_ecg, p_exang, p_slope)

    def checkpslope(p_age,p_gender,p_cp,p_rbps,p_chol,p_fbs,p_ecg,p_exang):
        speak("How would you describe the ST slope of patient's heart during peak exercise?")
        p_slope = int(input("\nHow is the ST Slope ?\nUpsloping=0\nFlat=1\nDownsloping=2\nResponse:"))
        if p_slope == 0:
            global pslope_ind
            pslope_ind = "ST Upsloping may indicate low risk"
            checkfluoro(p_age,p_gender,p_cp,p_rbps,p_chol,p_fbs,p_ecg,p_exang,p_slope)
        elif p_slope == 1:
            pslope_ind = "Flat ST may indicate moderate risk"
            checkfluoro(p_age,p_gender,p_cp,p_rbps,p_chol,p_fbs,p_ecg,p_exang,p_slope)
        elif p_slope == 2:
            pslope_ind = "ST Downsloping indicates less blood flow to heat"
            checkfluoro(p_age, p_gender, p_cp, p_rbps, p_chol, p_fbs, p_ecg, p_exang,p_slope)
        else:
            speak("Invalid Input!")
            checkpslope(p_age,p_gender,p_cp,p_rbps,p_chol,p_fbs,p_ecg,p_exang)

    def checkexang(p_age,p_gender,p_cp,p_rbps,p_chol,p_fbs,p_ecg):
        speak("I see. Is there any exercise-induced angina?")
        p_exang = int(input("\nIs there any exercise induced angina ?\nNo=0\nYes=1\nResponse:"))
        if p_exang == 0:
            global exang_ind
            exang_ind = "No significant chest pain while performing exercise"
            checkpslope(p_age,p_gender,p_cp,p_rbps,p_chol,p_fbs,p_ecg,p_exang)
        elif p_exang == 1:
            exang_ind = "Exercise-Induced Angina"
            checkpslope(p_age,p_gender,p_cp,p_rbps,p_chol,p_fbs,p_ecg,p_exang)
        else:
            speak("Invalid Input!")
            checkexang(p_age, p_gender, p_cp, p_rbps, p_chol, p_fbs, p_ecg)

    def checkecg(p_age,p_gender,p_cp,p_rbps,p_chol,p_fbs):
        speak("Understood. What is the patient's electrocardiogram (ECG) report result?")
        p_ecg = int(input("\nPatient ECG:-\nNormal=0\nST-T Wave Abnormality=1\nLeft Ventricular Hypertrophy(LVH)=2\nResponse:"))
        if p_ecg == 0:
            global ecg_ind
            ecg_ind="Normal ECG"
            checkexang(p_age,p_gender,p_cp,p_rbps,p_chol,p_fbs,p_ecg)
        elif p_ecg == 1:
            ecg_ind="ST-T Wave Abnormality can indicate reduced blood flow to heart"
            checkexang(p_age,p_gender,p_cp,p_rbps,p_chol,p_fbs,p_ecg)
        elif p_ecg == 2:
            ecg_ind="Left Ventricular Hypertrophy (LVH) indicates potential heart risk"
            checkexang(p_age,p_gender,p_cp,p_rbps,p_chol,p_fbs,p_ecg)
        else:
            speak("Invalid Input!")
            checkecg(p_age,p_gender,p_cp,p_rbps,p_chol,p_fbs)

    def checkfbs(p_age,p_gender,p_cp,p_rbps,p_chol):
        speak("Ok! Is patient's fasting blood sugar above 120 milligrams per deciliter?")
        p_fbs = int(input("\nEnter fasting blood sugar > 120 mg/dl ?\nFalse=0\nTrue=1\nResponse:"))
        if p_fbs==0:
            global fbs_ind
            fbs_ind = "Fasting Blood Sugar < 120"
            checkecg(p_age,p_gender,p_cp,p_rbps,p_chol,p_fbs)
        elif p_fbs==1:
            fbs_ind = "Fasting Blood Sugar > 120"
            checkecg(p_age,p_gender,p_cp,p_rbps,p_chol,p_fbs)
        else:
            speak("Invalid Input!")
            checkfbs(p_age,p_gender,p_cp,p_rbps,p_chol)

    def checkchol(p_age,p_gender,p_cp,p_rbps):
        speak("Thanks! Now, please enter patient's cholesterol level in milligrams per deciliter")
        p_chol = int(input("\nEnter cholesterol in mg/dl: "))
        if p_chol <= 210:
            global chol_ind
            chol_ind = "Normal"
            checkfbs(p_age,p_gender,p_cp,p_rbps,p_chol)
        elif 211<=p_chol <265:
            chol_ind = "Borderline"
            checkfbs(p_age,p_gender,p_cp,p_rbps,p_chol)
        elif 265<=p_chol<600:
            chol_ind = "Potential risk"
            checkfbs(p_age,p_gender,p_cp,p_rbps,p_chol)
        else:
            speak("Invalid Input!")
            checkchol(p_age,p_gender,p_cp,p_rbps)

    def checkbps(p_age,p_gender,p_cp):
        speak("Noted. What is the patient's resting blood pressure?")
        p_rbps = int(input("\nEnter rest bps: "))
        if 60<= p_rbps <= 120:
            global bps_ind
            bps_ind = "Normal blood pressure"
            checkchol(p_age,p_gender,p_cp,p_rbps)
        elif 121<= p_rbps < 140:
            bps_ind = "Moderate blood pressure"
            checkchol(p_age,p_gender,p_cp,p_rbps)
        elif 140<= p_rbps <150:
            bps_ind = "Stage 1 Hypertention"
            checkchol(p_age,p_gender,p_cp,p_rbps)
        elif 150<= p_rbps <180:
            bps_ind = "Stage 2 Hypertention"
            checkchol(p_age,p_gender,p_cp,p_rbps)
        elif 180<= p_rbps<280:
            p_rbps = "Hypertension Crises"
            checkchol(p_age,p_gender,p_cp,p_rbps)
        else:
            speak("Invalid Input!")
            checkbps(p_age,p_gender,p_cp)

    def checkcp(p_age,p_gender):
        speak("Got it. Now, please select the type of chest pain experienced")
        p_cp = int(input("\nSelect type of chest pain:-\nTypical Angina=0\nAtypical Angina=1\nNon-Anginal-Pain=2\nAsymptomatic=3\nResponse:"))
        if p_cp == 0:
            global pain
            pain = "Typical Anginal chest pain"
            checkbps(p_age,p_gender,p_cp)
        elif p_cp == 1:
            pain = "Atypical Anginal chest pain"
            checkbps(p_age,p_gender,p_cp)
        elif p_cp == 2:
            pain = "Non-Anginal chest pain "
            checkbps(p_age,p_gender,p_cp)
        elif p_cp == 3:
            pain = "Asymptomatic chest pain"
            checkbps(p_age,p_gender,p_cp)
        else:
            speak("Invalid Input!")
            checkcp(p_age,p_gender)

    def checkgender(p_age):
        speak("Thank you. Next, could you tell me patient's gender?")
        p_gender = int(input("\nEnter gender:-\nFemale=0\nMale=1\nResponse: "))
        if 0 <= p_gender <= 1:
            checkcp(p_age,p_gender)
        else:
            speak("Invalid Input!")
            checkgender(p_age)

    def checkage():
        speak("Please tell me the patient's age")
        p_age = int(input("Enter the age: "))
        if 1 <= p_age <= 110:
            if p_age < 35:
                global agerisk
                agerisk = "Low risk"
                checkgender(p_age)
            elif 35 <= p_age < 50:
                agerisk = "Moderate risk"
                checkgender(p_age)
            elif 50 <= p_age < 65:
                agerisk = "Elevated risk"
                checkgender(p_age)
            elif 65 <= p_age < 80:
                agerisk = "Potential risk"
                checkgender(p_age)
            elif p_age >= 80:
                agerisk = "Potential High Risk"
                checkgender(p_age)
            else:
                speak("Please enter valid age!")
                checkage()
    checkage()

print('Welcome! I am Heart Guardian, your personal healthcare AI assistant for heart disease prediction.')
speak("Welcome! I am Heart Guardian, your personal healthcare AI assistant for heart disease prediction. I'm here to assess potential heart disease risks. To begin, I need some information. Let’s proceed step by step.")

try:
    df = pd.read_csv('heart.csv')
    x = df[['age', 'sex', 'chest_pain', 'restbps', 'chol', 'fbs', 'restecg', 'exang', 'ST_slope', 'fluoroscopy_vessels',
            'thal']]
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    model = RandomForestClassifier(n_estimators=100, criterion='gini')
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    mconfusionmatrix = confusion_matrix(y_test, y_pred)
    classificationreport = classification_report(y_test, y_pred)
    imp_features = pd.Series(model.feature_importances_, index=X_train.columns).sort_values(ascending=False)
    checkup()
    print(f"Accuracy of Model: {accuracy * 100} %")
    print(f"Confusion Matrix of Model:\n{mconfusionmatrix}")
    print(f"Classification Report of Model:\n{classificationreport}")
    print(f"Important Features:\n{imp_features}")

except Exception as error:
    print(error)

