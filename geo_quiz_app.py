import streamlit as st
import pandas as pd
import random

############################# form function  ######################################################
def question_set(df):
    user_answers = []
    wrong_answers = []
    score = 0

    with st.form("quiz", clear_on_submit=True):
        for i in range(df.shape[0]):
            row = df.iloc[i]
            options = ['Select', row['option1'], row['option2'], row['option3'], row['option4']]
            user_answer = st.radio(row['question'], options, key=i, horizontal=True)
            user_answers.append(user_answer)
        submitted = st.form_submit_button("Submit")

    if submitted:
        for i in range(df.shape[0]):
            row = df.iloc[i]
            if user_answers[i] == row['answer']:
                score += 1
            else:
                wrong_answers.append(row['question'])

        
        percentage = (score / df.shape[0]) * 100
        st.success(f"✅ You got {score} correct out of {df.shape[0]} !!!")
        st.info(f"🎯 Your Score {percentage:.2f}%")

        if percentage == 100:
            st.balloons()
        else:
            st.error("Wrong Answers !!!")
            for i, wrong in enumerate(wrong_answers, start=1):
                correct_answer = df[df['question'] == wrong]['answer'].values[0]
                st.warning(f"{i}. {wrong}")
                st.info(f'Correct Answer: **{correct_answer}**')
    
#################################################################################
# Import file of questions and options
capital_all = pd.read_csv("capitals_city.csv")

st.subheader("🌍 Geographical Knowledge")

######################    Tab1
tab1, tab2 = st.tabs(['Capital City Quiz','Country Quiz'])

with tab1:
    col1, col2 = st.columns(2)
    continent_selected = col1.radio("Select the continent you want to play:", options= ["Asia","Europe","North America","South America","Australia","Africa"])
        
    ########################           Asia    ###################################################
    if continent_selected == "Asia":
        col2.image("images/asia.png")
        df_continent = capital_all[capital_all['continent'] == "Asia"]
        df_continent.reset_index(drop=True, inplace=True)
        select_asia_level = col1.selectbox("Select Level", options= ['Level-1','Level-2','Level-3','Level-4','Level-5'])
        if select_asia_level == "Level-1":
            df = df_continent.iloc[0:10]
            st.write(select_asia_level)
            question_set(df)

        elif select_asia_level == "Level-2":
            df = df_continent.iloc[10:20]
            st.write(select_asia_level)
            question_set(df)
        elif select_asia_level == "Level-3":
            df = df_continent.iloc[20:30]
            st.write(select_asia_level)
            question_set(df)
        elif select_asia_level == "Level-4":
            df = df_continent.iloc[30:40]
            st.write(select_asia_level)
            question_set(df)

        elif select_asia_level == "Level-5":
            df = df_continent.iloc[40:50]
            st.write(select_asia_level)
            question_set(df)
        else:
            pass
    ########################           Europe    ###################################################

    if continent_selected == "Europe":
        col2.image("images/europe.png")
        df_continent = capital_all[capital_all['continent'] == "Europe"]
        df_continent.reset_index(drop=True, inplace=True)
        select_europe_level = col1.selectbox("Select Level", options= ['None','Level-1','Level-2','Level-3','Level-4','Level-5'])
        if select_europe_level == "Level-1":
            df = df_continent.iloc[0:10]
            st.write(select_europe_level)
            question_set(df)

        elif select_europe_level == "Level-2":
            df = df_continent.iloc[10:20]
            st.write(select_europe_level)
            question_set(df)
        elif select_europe_level == "Level-3":
            df = df_continent.iloc[20:30]
            st.write(select_europe_level)
            question_set(df)
        elif select_europe_level == "Level-4":
            df = df_continent.iloc[30:40]
            st.write(select_europe_level)
            question_set(df)

        elif select_europe_level == "Level-5":
            df = df_continent.iloc[40:50]
            st.write(select_europe_level)
            question_set(df)
        else:
            pass

    ########################        North America    ###################################################

    if continent_selected == "North America":
        col2.image("images/north_america.png")
        df_continent = capital_all[capital_all['continent'] == "North America"]
        df_continent.reset_index(drop=True, inplace=True)
        select_n_america_level = col1.selectbox("Select Level", options= ['None','Level-1','Level-2','Level-3'])
        if select_n_america_level == "Level-1":
            df = df_continent.iloc[0:10]
            st.write(select_n_america_level)
            question_set(df)

        elif select_n_america_level == "Level-2":
            df = df_continent.iloc[10:20]
            st.write(select_n_america_level)
            question_set(df)
        elif select_n_america_level == "Level-3":
            df = df_continent.iloc[20:30]
            st.write(select_n_america_level)
            question_set(df)
        
        else:
            pass

    ########################        South America    ###################################################

    if continent_selected == "South America":
        col2.image("images/south_america.png")
        df_continent = capital_all[capital_all['continent'] == "South America"]
        df_continent.reset_index(drop=True, inplace=True)
        # select_n_america_level = col1.selectbox("Select Level", options= ['None','Level-1'])
        # if select_n_america_level == "Level-1":
        df = df_continent
        # st.write(select_n_america_level)
        question_set(df)

    ########################        Australia    ###################################################

    if continent_selected == "Australia":
        col2.image("images/australia.png")
        df_continent = capital_all[capital_all['continent'] == "Australia"]
        df_continent.reset_index(drop=True, inplace=True)
        select_australia_level = col1.selectbox("Select Level", options= ['None','Level-1','Level-2'])
        if select_australia_level == "Level-1":
            df = df_continent.iloc[0:7]
            st.write(select_australia_level)
            question_set(df)

        elif select_australia_level == "Level-2":
            df = df_continent.iloc[7:]
            st.write(select_australia_level)
            question_set(df)
        else:
            pass

    ########################           Asia    ###################################################
    if continent_selected == "Africa":
        col2.image("images/africa.png")
        df_continent = capital_all[capital_all['continent'] == "Africa"]
        df_continent.reset_index(drop=True, inplace=True)
        select_asia_level = col1.selectbox("Select Level", options= ['None','Level-1','Level-2','Level-3','Level-4','Level-5','Level-6'])
        if select_asia_level == "Level-1":
            df = df_continent.iloc[0:10]
            st.write(select_asia_level)
            question_set(df)

        elif select_asia_level == "Level-2":
            df = df_continent.iloc[10:20]
            st.write(select_asia_level)
            question_set(df)
        elif select_asia_level == "Level-3":
            df = df_continent.iloc[20:30]
            st.write(select_asia_level)
            question_set(df)
        elif select_asia_level == "Level-4":
            df = df_continent.iloc[30:40]
            st.write(select_asia_level)
            question_set(df)

        elif select_asia_level == "Level-5":
            df = df_continent.iloc[40:50]
            st.write(select_asia_level)
            question_set(df)

        elif select_asia_level == "Level-6":
            df = df_continent.iloc[50:60]
            st.write(select_asia_level)
            question_set(df)

        else:
            pass
################################# Tab2
with tab2:
    
    # Sample only once per session to avoid changing questions on rerun
    if 'random_df_all' not in st.session_state:
        st.session_state.random_df_all = capital_all.sample(n=203)
    random_df_all = st.session_state.random_df_all


######################################### funtion
    def continent_quiz(random_df):
        unknown_question = []   
        # user_answers_country = []
        correct_answers = []
        incorrect_answers = []
        score = 0

        with st.form("country_quiz", clear_on_submit=True):
            for i in range (random_df.shape[0]):
                country = f'On which continent is **{random_df["country"].iloc[i]}** located?'
                answer_country=st.radio(country, options= ["","Africa","Asia","Australia","Europe","North America","South America"],horizontal=True)
                if answer_country == random_df['continent'].iloc[i]:
                    correct_answers.append(answer_country)
                    score += 1

                else:
                    incorrect_answers.append(answer_country)
                    unknown_question.append(random_df["country"].iloc[i])

            submitted_country_quiz = st.form_submit_button("Submit")

        
        if submitted_country_quiz:
            percentage = (score / 10) * 100
            st.success(f"✅ You got {score} correct out of 10 !!!")
            st.info(f"🎯 Your Score {percentage:.2f}%")
            
            if percentage ==100:
                st.snow()

            else:
                st.error("❌ Some answers were incorrect!")

                for country in unknown_question:
                    correct_answer_con = random_df[random_df['country'] == country]['continent'].values[0]
                    st.warning(f"Incorrect Country: {country}")
                    st.info(f"Correct Answer: {correct_answer_con}")
    #############################################################################################            
    st.image("images/world_map_3360.jpg",)
    select_continant_level = st.selectbox("Test your knowledge about continents", options= ['Level-1','Level-2','Level-3','Level-4','Level-5',
                                                                 'Level-6','Level-7','Level-8','Level-9','Level-10'
                                                                 
                                                                 ])
    #     if 
    # continent_quiz(random_df)
        # if select_asia_level == "Level-1":
        #     df = df_continent.iloc[0:10]
        #     st.write(select_asia_level)
        #     question_set(df)

    if select_continant_level == "Level-1":
        # st.write(random_df_all.head())
        random_df = random_df_all.iloc[0:10]
        continent_quiz(random_df)
    if select_continant_level == "Level-2":
        # st.write(random_df_all.head())
        random_df = random_df_all.iloc[10:20]
        continent_quiz(random_df)

    if select_continant_level == "Level-3":
        # st.write(random_df_all.head())
        random_df = random_df_all.iloc[20:30]
        continent_quiz(random_df)

    if select_continant_level == "Level-4":
        # st.write(random_df_all.head())
        random_df = random_df_all.iloc[30:40]
        continent_quiz(random_df)
    if select_continant_level == "Level-5":
        # st.write(random_df_all.head())
        random_df = random_df_all.iloc[40:50]
        continent_quiz(random_df)
    if select_continant_level == "Level-6":
        # st.write(random_df_all.head())
        random_df = random_df_all.iloc[50:60]
        continent_quiz(random_df)
    if select_continant_level == "Level-7":
        # st.write(random_df_all.head())
        random_df = random_df_all.iloc[60:70]
        continent_quiz(random_df)
    if select_continant_level == "Level-8":
        # st.write(random_df_all.head())
        random_df = random_df_all.iloc[70:80]
        continent_quiz(random_df)
    if select_continant_level == "Level-9":
        # st.write(random_df_all.head())
        random_df = random_df_all.iloc[80:90]
        continent_quiz(random_df)
    if select_continant_level == "Level-10":
        # st.write(random_df_all.head())
        random_df = random_df_all.iloc[90:100]
        continent_quiz(random_df)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<hr style="margin-top: 30px;">
<div style="text-align: center; font-size: 0.9em; color: gray;">
    Created by <b>Partho Sarothi Das</b><br>
    <i>Aspiring Data Scientist | Passionate about ML & Visualization</i><br>
    Email: <a href="mailto:partho52@gmail.com">partho52@gmail.com</a><br><br>
    Globe images used in this app are sourced from <a href="https://commons.wikimedia.org" target="_blank">Wikimedia Commons</a> and licensed under 
    <a href="https://creativecommons.org/licenses/by-sa/3.0/" target="_blank">CC BY-SA 3.0</a>. Images may have been resized or renamed for educational use.
</div>
""", unsafe_allow_html=True)
