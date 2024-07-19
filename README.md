<div align='center'>
   
![Screenshot 2024-07-19 184140](https://github.com/user-attachments/assets/51aaddd6-7480-4f9c-9084-f4a536fd6eb6)



<br>

# Diagnose

Skin cancer detection from your skin images.

Watch Demo Video - <a href='https://youtu.be/4SZCctRP6pY?si=rJg-NmuyWCnfI59y'>Click here</a>
   
</div>

## Project Overview

**Melanoma** is a type of skin cancer that can be deadly if not detected early. It accounts for 75% of skin cancer deaths. A solution which can evaluate images and alert the dermatologists about the presence of melanoma has the potential to reduce a lot of manual effort needed in diagnosis.

Our application detects the following skin diseases:
- Actinic keratosis
- Basal cell carcinoma
- Dermatofibroma
- Melanoma
- Nevus
- Pigmented benign keratosis
- Seborrheic keratosis
- Squamous cell carcinoma
- Vascular lesion

  
# Technology Stack Used:

- Python
- Machine Learning
- Streamlit

### APIs used

- [Google maps API for places](https://maps.googleapis.com): To show all nearby dermatologists, based on the current location of the user.

## How it works?

Our application utilizes machine learning to predict what skin disease you may have, from your skin images!
We then recommend you specialized doctors based on your type of skin diseases.

<div align='center'>

<h2>Screenshots</h2>

![Screenshot 2024-07-19 185943](https://github.com/user-attachments/assets/e053f13f-ce96-4396-bacb-dd97a9fb23b1)

![Screenshot 2024-07-19 190001](https://github.com/user-attachments/assets/3b954f8e-9459-41b2-820c-14281837ab89)


![Screenshot 2024-07-19 190030](https://github.com/user-attachments/assets/5e2bf7b4-f632-4e5c-a971-5f8ea38f729d)

![Screenshot 2024-07-19 190120](https://github.com/user-attachments/assets/1216f9eb-5fa6-4976-afea-171b449ece90)

![Screenshot 2024-07-19 190136](https://github.com/user-attachments/assets/96114a9d-4d32-439d-9389-788ba779ac32)

![Screenshot 2024-07-19 190153](https://github.com/user-attachments/assets/a33860bc-c173-498d-bbfb-0c5246dedf6b)

![Screenshot 2024-07-19 190217](https://github.com/user-attachments/assets/a21bcd46-2537-4687-a477-fd8430f8f1b1)


![Screenshot 2024-07-19 190231](https://github.com/user-attachments/assets/49a77939-1b2d-41d4-9e99-996df2000d32)








<h2>Demo Video</h2>



https://github.com/user-attachments/assets/934809d6-6d5b-45f9-9b27-aa5cc4ad69cc



</div>

## Setting up Local Development

1. Clone the repository

```
git clone https://github.com/coder12git/Diagnose.git
```

2. Navigate to the project folder

```
cd Diagnose/
```

3. Create a virtual environment

```
python3 -m venv venv
```

4. Activate the virtual environment

for Linux and Mac:

```
source venv/bin/activate
```

for Windows:

```bash
venv\Scripts\activate
```

5. Install dependencies

 ```bash
 pip install -r requirements.txt
 ```

6. Run the app

```bash
streamlit run ./About.py
```
    

<hr/>

<div align='center'>
  <h3>Thanks for visiting!</h3>
</div>
