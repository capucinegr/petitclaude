#_____________________________________ IMPORT __________________________________________
import streamlit as st
import base64
import numpy as np
import pandas as pd
import random

#_____________________________________ FILE __________________________________________
#To read csv file and create Dataframe more easly in the code

def read_csv_file(file) :
    data = pd.read_csv(file)
    df = pd.DataFrame(data=data)
    return df

#Just to show the Dataset if we want with checkbox
def print_checkbox(df) :
    st.markdown("<h1 color=#0E2552'>     </h1>", unsafe_allow_html=True)
    if st.checkbox('See Dataset :'):
        st.write(df)


#You can find the css part in the css file, it's to personnalize the application
#we need to read it
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

#_____________________________________ HEADER __________________________________________
#we make the design of the header with the title and the logo

def header() :
    LOGO_IMAGE = "picture\home\logo_chou.png"
    MAL_PICT = "picture\home\malardalen-university-vasteras-sweden.jpg"
    st.markdown('<p class="recog_title">recog</p>', unsafe_allow_html=True)
    st.markdown(f"""<img class="recog_img" src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}">""", unsafe_allow_html=True)
    st.markdown(f"""<img class="mal_img" src="data:image/png;base64,{base64.b64encode(open(MAL_PICT, "rb").read()).decode()}">""", unsafe_allow_html=True)
#_____________________________________ PAGES __________________________________________
#Each Page have his function to partitionate the code


#--------------------------------------- HOME ---------------------------------------
def home_page() :
    #HEADER TO SAY WELCOME to the site
    st.markdown('<p class="welcome">Welcome to the Recog site</p>', unsafe_allow_html=True)
    
    #INTRODUCTION
    st.markdown('<p class="body_text">The number of patients in rehabilitation after a stroke amounted to more than 16,000 people in 2018. Rehabilitation can last for years, sometimes going to more than 5 years of physiotherapy, rehabilitation… But how to help the health personnel to facilitate this rehabilitation?</p>', unsafe_allow_html=True)
    st.markdown('<p class="body_text">This is possible thanks to the RECOG research project: it examines how to use EEG with AI and robotics to facilitate the rehabilitation of stroke patients.</p>', unsafe_allow_html=True)

    #TITLE WHAT IS RECOG which explain what is the project
    st.markdown('<p class="whatisrecog">What is our project ? </p>', unsafe_allow_html=True)
    #EXPLICATION PROJECT
    st.markdown('<p class="body_text">Our project is therefore a part of this research project. It involves using a camera that analyzes the gaze of a patient who is playing a memory game to adjust the difficulty according to their gaze. It is a real-time project connected to an IC and programmed in Labview which uses robotics and artificial intelligence.</p>', unsafe_allow_html=True)
    st.markdown('<p class="body_text">You will find below an image illustrating our project, the following one illustrates the system.</p>', unsafe_allow_html=True)
    
    #IMAGE PRESENTATION PROJECT
    IM_PROJ='picture\home\img_explication.png'
    st.markdown(f"""<img class="pict_proj" src="data:image/png;base64,{base64.b64encode(open(IM_PROJ, "rb").read()).decode()}">""", unsafe_allow_html=True)
    
    #IMAGE SYSTEM if push button, else we explain how the system work
    b = st.button("System")
    if b:
        IM_SYS='picture\home\system.png'
        st.markdown(f"""<img class="pict_syst" src="data:image/png;base64,{base64.b64encode(open(IM_SYS, "rb").read()).decode()}">""", unsafe_allow_html=True)
    else :
        st.markdown('<p class="body_text">The system is based on acquiring data, processing it while the game is taking place. Then we send the data to the ANN which classifies the data to send feedback on the difficulty that will change the game.</p>', unsafe_allow_html=True)
    


    #TITLE GOALS and explication of the goals of the project
    st.markdown('<p class="welcome">Our Goals</p>', unsafe_allow_html=True)
    st.markdown('<p class="body_text">The objective of this project is to have a qualitative and optimized system providing feedback as quickly as possible. This is why the execution time is an important factor to take into account in this project. The goal is also to help the 16,000 stroke patients each year as well as hospitals, hopefully in the future nationwide.</p>', unsafe_allow_html=True)
    #columns to show goals
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Speed", value="200 ms", delta = '198 ms')
    with col2:
        map_hospital()

#Map of hospital in Sweden to show where the system can be use
def map_hospital() :
    data = read_csv_file('data\hospital_data.csv')
    st.map(data)


#--------WHO ARE WE PART to explain the role of each student
def whoarewe_page() :
    #Title
    st.markdown('<p class="welcome">Who are we ?</p>', unsafe_allow_html=True)
    #Name of everyone    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<p class="role">Project Manager</p>', unsafe_allow_html=True)
        st.markdown('<p class="name">Sara LENMAN</p>', unsafe_allow_html=True)
    with col2:
        st.markdown('<p class="role">Safety/Dependability Manager</p>', unsafe_allow_html=True)
        st.markdown('<p class="name">Emil CARMEGREN</p>', unsafe_allow_html=True)
    with col3:
        st.markdown('<p class="role">Softare Manager</p>', unsafe_allow_html=True)
        st.markdown('<p class="name">Marina LOPEZ MURCIA</p>', unsafe_allow_html=True)
    col4, col5 = st.columns(2)
    with col4 :
        st.markdown('<p class="role">Verification and Validation Manager</p>', unsafe_allow_html=True)
        st.markdown('<p class="name">Niclas BORG SIGG</p>', unsafe_allow_html=True)
    with col5:
        st.markdown('<p class="role">Testing Manager and Quality Manager</p>', unsafe_allow_html=True)
        st.markdown('<p class="name">Michael BABRA</p>', unsafe_allow_html=True)



#--------------------------------------- PAGE OF MEMORY GAME ---------------------------------------
def MG_page() :
    #title of page
    st.markdown('<p class="welcome">Memory Game</p>', unsafe_allow_html=True)
    
    #text to explain memory game
    st.markdown("<p class='body_text'>The memory game is actually a game used to analyze a patient's ability to respond to a stroke. It consists of a game grid where squares appear and the patient has to answer if the square was placed in the same place as the previous square. There are several difficulty levels as well as different game modes: 0-back, 1-back, 2-back.</p>", unsafe_allow_html=True)

    #picture Memory Game
    IM_MG='picture\Memory_Game\mg_img.png'
    st.markdown(f"""<img class="pict_mg" src="data:image/png;base64,{base64.b64encode(open(IM_MG, "rb").read()).decode()}">""", unsafe_allow_html=True)
    
    #Print back modes and choose one
    option = st.selectbox('Game modes',['0-back','1-back','2-back'])
    if option == '0-back':
        st.markdown("<p class='body_text'> In the 0-back mode, one initial square is shown to the patient. Then, other squares appear one by one and the patient has to confirm whether or not they are in the same place as the initial one.</p>", unsafe_allow_html=True)
        #print exemple to explain
        col1, col2, col3 = st.columns(3)
        with col1:
            st.title("1st Round")
            IM_0back1='picture\Memory_Game\mg_0back_1.png'
            st.markdown(f"""<img class="pict_back" src="data:image/png;base64,{base64.b64encode(open(IM_0back1, "rb").read()).decode()}">""", unsafe_allow_html=True)
        with col2:
            st.title("2nd Round")
            IM_0back2='picture\Memory_Game\mg_0back_2.png'
            st.markdown(f"""<img class="pict_back" src="data:image/png;base64,{base64.b64encode(open(IM_0back2, "rb").read()).decode()}">""", unsafe_allow_html=True)
        with col3:
            st.title("3rd Round")
            IM_0back3='picture\Memory_Game\mg_0back_3.png'
            st.markdown(f"""<img class="pict_back" src="data:image/png;base64,{base64.b64encode(open(IM_0back3, "rb").read()).decode()}">""", unsafe_allow_html=True)
    
    if option == '1-back':
        st.markdown("<p class='body_text'>1-back mode, the patient has to compare each appearing square with the previous one, and then tell if it is in the same place as the previous one or not.</p>", unsafe_allow_html=True)
        #print exemple to explain
        col1, col2, col3 = st.columns(3)
        with col1:
            st.title("1st Round")
            IM_1back1='picture\Memory_Game\mg_1back_1.png'
            st.markdown(f"""<img class="pict_back" src="data:image/png;base64,{base64.b64encode(open(IM_1back1, "rb").read()).decode()}">""", unsafe_allow_html=True)
        with col2:
            st.title("2nd Round")
            IM_1back2='picture\Memory_Game\mg_1back_2.png'
            st.markdown(f"""<img class="pict_back" src="data:image/png;base64,{base64.b64encode(open(IM_1back2, "rb").read()).decode()}">""", unsafe_allow_html=True)
        with col3:
            st.title("3rd Round")
            IM_1back3='picture\Memory_Game\mg_1back_3.png'
            st.markdown(f"""<img class="pict_back" src="data:image/png;base64,{base64.b64encode(open(IM_1back3, "rb").read()).decode()}">""", unsafe_allow_html=True)
    if option == '2-back':
        st.markdown("<p class='body_text'>The 2-back allows you to respond if the square is in the same place as the square present two turns before this one. In the 2-back mode, the patient has to compare each appearing square with the two previous ones.</p>", unsafe_allow_html=True)
        #print exemple to explain
        col1, col2, col3 = st.columns(3)
        with col1:
            st.title("1st Round")
            IM_2back1='picture\Memory_Game\mg_2back_1.png'
            st.markdown(f"""<img class="pict_back" src="data:image/png;base64,{base64.b64encode(open(IM_2back1, "rb").read()).decode()}">""", unsafe_allow_html=True)
        with col2:
            st.title("2nd Round")
            IM_2back2='picture\Memory_Game\mg_2back_2.png'
            st.markdown(f"""<img class="pict_back" src="data:image/png;base64,{base64.b64encode(open(IM_2back2, "rb").read()).decode()}">""", unsafe_allow_html=True)
        with col3:
            st.title("3rd Round")
            IM_2back3='picture\Memory_Game\mg_2back_3.png'
            st.markdown(f"""<img class="pict_back" src="data:image/png;base64,{base64.b64encode(open(IM_2back3, "rb").read()).decode()}">""", unsafe_allow_html=True)
 
    #Explain the training and classifying mode
    st.markdown('<p class="welcome">Classify/Training</p>', unsafe_allow_html=True)
    mode = st.radio(
        "There are also two modes to either train the model or classify the responses. The first one sends information to the NNA while the other one analyzes the patient’s behavior.",
        ('Training','Classify'))

    if mode == 'Training':
        st.markdown("<p class='body_text'>A model needs to be well trained before it can begin to classify data, which is the reason why the Training mode exists. It allows sending the necessary data to train the ANN.</p>", unsafe_allow_html=True)

    else:
        st.markdown("<p class='body_text'>Once trained, it can correctly classify the data sent by the Classify game mode. Here we send the data and then sum it to wait for the results to adjust the game. All this process is described more in the rest of the website.</p>", unsafe_allow_html=True)

    


#--------------------------------------- PAGE OF Preprocessing ---------------------------------------

def pupil_size(data) :
    data['pupil_size'] = (data['pupil_right']+data['pupil_left'])/2
    return data


############# ONLY WITHOUT DATA #############
#We use random data to show how it can be but it will be change
def random_float(low, high):
    return random.random()*(high-low) + low

#We want plot with pupil right, pupil left and the mean of pupil size
def plot_pupil() :
    #Here its because we don't have the real data so we create it
    pupil_L_R = np.zeros((30,2))
    pupil_L_R_M = np.zeros((30,3))
    mean = np.zeros(30)
    for i in range(30):
        for j in range(2) :
            pupil_L_R[i,j]= random_float(0.003, 0.009)
    #We calculate the mean between pupil right and pupil left
    for k in range(30):
        mean[k]= (pupil_L_R[k,0]+pupil_L_R[k,1])/2
    pupil_L_R_M = np.c_[pupil_L_R,mean]
    #Create the dataframe to create the line chart
    chart_data = pd.DataFrame(
        pupil_L_R_M,
        columns=['pupil_right','pupil_left','mean_pupil_size'])

    #print the dataset
    print_checkbox(chart_data)
    #Print the title and LineChart
    st.write("Pupil Size")
    st.line_chart(chart_data)




#We want plot with the quality of data and after when we use preprocessing
def plot_quality() :
    #The first is the data sending to system
    #Here its because we don't have the real data so we create it
    quality_no_pp = np.zeros(30)
    for i in range(30):
        quality_no_pp[i]= random_float(0.06, 0.95)
    #Create the dataframe to create the line chart
    chart_quality_nopp = pd.DataFrame(
        quality_no_pp,
        columns=['quality'])
    
    #Here we want to delete the data under 0.6 because we need data with hight quality
    bad_quality = np.zeros(30)
    quality_pp = np.zeros(30)
    #So we create an array with the data that we want to delete
    for j in range (30) :
        if quality_no_pp[j]<0.6 :
            bad_quality[j] = quality_no_pp[j]
    #And after we keep the difference between the two arrays
    quality_pp = np.setdiff1d(quality_no_pp, bad_quality)
    #We create the DataFrame and after we show this
    chart_quality_pp = pd.DataFrame(
        quality_pp,
        columns=['quality'])

    
    #Print the title and LineChart without preprocessing and after with preprocessing
    col1,col2 = st.columns(2)
    with col1 :
        st.markdown("<p class='body_text'>Quality without Preprocessing</p>", unsafe_allow_html=True)
        st.line_chart(chart_quality_nopp)
    with col2 :
        st.markdown("<p class='body_text'>Quality with Preprocessing</p>", unsafe_allow_html=True)
        st.line_chart(chart_quality_pp)
    
    
#############################################



def preprocessing() :
    #read file to show plot after
    data = read_csv_file('data\pupil_data.csv')
    #title DataVisualization
    st.markdown('<p class="welcome">Preprocessing</p>', unsafe_allow_html=True)
    
    #Explain the page
    st.markdown("<p class='body_text'>During this project, data is collected by the camera to analyze the patient’s gaze. This SmartEyes camera allows usto recover the size of the pupils as well as the quality of the data. This information issorted to retrieve only the significant data by removing not good quality data or outliers, and is then sent to the ANN. Here we will show you a sample of the collected data.</p>", unsafe_allow_html=True)
    #Picture of the camera system
    im_1, im_2 = st.columns(2)
    with im_1 :
        IM_gaze='picture\datavisu\datavisu_gaze.png'
        st.markdown(f"""<img class="pict_data_visu" src="data:image/png;base64,{base64.b64encode(open(IM_gaze, "rb").read()).decode()}">""", unsafe_allow_html=True)
    with im_2 :
        IM_eye='picture\datavisu\datavisu_eye.png'
        st.markdown(f"""<img class="pict_datavisu_eye" src="data:image/png;base64,{base64.b64encode(open(IM_eye, "rb").read()).decode()}">""", unsafe_allow_html=True)

    #Print the title and plot of pupil size and quality

    st.markdown("<p class='body_text'>Once the data has been retrieved by the camera, we need to sort it in order to send only the necessary data to the ANN. To do this, we remove some data that does not influence the classification, which allows us to keep only the size of the left and right pupil as well as the quality of the data. Once this first sorting is done, we will also remove outliers such as improbable pupil size and poor quality to maintain a qualitative dataset. This will then lead to better results for the ANN.</p>", unsafe_allow_html=True)
    plot_pupil()
    plot_quality()





#--------------------------------------- PAGE OF ANN ---------------------------------------
def ANN_page():
    #Title
    st.markdown('<p class="welcome">ANN</p>', unsafe_allow_html=True)

    #Explication
    st.markdown("<p class='body_text'>The ANN is the model for our project: it is an artificial neural network that attempts to model the functioning of neurons in the brain. Each neuron sends a signal to another one, which processes it and then sends it to another neuron. The processing of these neurons corresponds to a digital processing between the nodes of the neurons. Neurons are layered together, and multiple layers are used to get to the exit node.</p>", unsafe_allow_html=True)
    st.markdown("<p class='body_text'>The goal for ANN is to learn on its own by adjusting the weights of the nodes according to the learning algorithm, so that it becomes as reliable as possible. In our project, the ANN is made up of a real-time (RT) part and an FPGA part on the industrial controller (IC). These two parts communicate with each other to form and classify the data in a queue.</p>", unsafe_allow_html=True)
    #Picture
    IM_ann='picture\ANN.png'
    st.markdown(f"""<img class="pict_ann" src="data:image/png;base64,{base64.b64encode(open(IM_ann, "rb").read()).decode()}">""", unsafe_allow_html=True)




#--------------------------------------- PAGE OF FEEDBACK ---------------------------------------
def feedback_page() :
    #TItle
    st.markdown('<p class="welcome">Feedback</p>', unsafe_allow_html=True)

    #explication
    st.markdown("<p class='body_text'>As explained, the goal of this system is to be able to adapt the difficulty according to the patient’s reactions. For this, once the data has been classified by the ANN, we must create a feedback system to adjust the Memory Game. This adjustment should be gradual, and not done continuously, which is why a PID controller is used. Feedback is essential in order to maintain an ideal level of difficulty for the patient's cognitive load throughout his performance.</p>", unsafe_allow_html=True)
    #Picture Feedback
    st.markdown("<h1 color=#0E2552'>     </h1>", unsafe_allow_html=True) 
    st.image('picture\_feedback.png')





#--------------------------------------- PAGE OF PROGRESS ---------------------------------------
def plot_prog_ex():
    data = read_csv_file('data\progress.csv')
    month_choice = st.radio(
       'Choose between November or December',
        ('November', 'December'))

    if month_choice == 'November':
        data_nov = data[ data['month'] == 11 ]
        print_checkbox(data_nov)
        df = pd.DataFrame({
            'execution_time': data_nov['execution_time'],
        })
        st.line_chart(df)
    else:
        data_dec = data[ data['month'] == 12 ]
        print_checkbox(data_dec)
        df = pd.DataFrame({
            'execution_time': data_dec['execution_time'],
        })
        st.line_chart(df)

def progress_page() :
    # title
    st.markdown('<p class="welcome">Progress</p>', unsafe_allow_html=True)

    #explication
    st.markdown("<p class='body_text'>After months of work, we obviously had to observe some progress in our project. For example, it was essential to achieve the fastest possible execution so we had to optimize the code to see its execution time improve. On this page, you will be able to follow the progress of our project as well as some elements that we have optimized to improve our code.</p>", unsafe_allow_html=True)
    st.write("Exemple that can be make")
    #Print of plot
    plot_prog_ex()



#_____________________________________ MENU __________________________________________

def choose_page() :
    option = st.sidebar.selectbox('Which page :',['home','memory game','preprocessing','ANN','project progress'])
    if option == 'home' :
        home_page()
        whoarewe_page()
    if option == 'memory game' :
        MG_page()
    if option == 'preprocessing' :
        preprocessing()
    if option == 'ANN' :
        ANN_page()
        feedback_page()
    if option == 'project progress' :
        progress_page()


def main() :
    header()
    choose_page()
    

main() 