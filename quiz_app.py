import streamlit as st

st.set_page_config(page_title="Easy MCQ Quiz", layout="centered")

st.title("📝 Easy Logical Reasoning and Grammar MCQ Quiz")

score = 0

st.header("Logical Reasoning Questions")

q1 = st.radio("1. If all roses are flowers, and some flowers fade quickly, then:", ["A) All roses fade quickly", "B) Some roses may fade quickly", "C) No rose fades quickly", "D) None of the above"])
if q1.startswith("B"):
    score += 1

q2 = st.radio("2. Find the next number in the series: 2, 4, 6, 8, ___", ["A) 10", "B) 12", "C) 14", "D) 16"])
if q2.startswith("A"):
    score += 1

q3 = st.radio("3. If CAT is coded as 3120, then DOG is coded as:", ["A) 4157", "B) 4156", "C) 4147", "D) 4165"])
if q3.startswith("A"):
    score += 1

q4 = st.radio("4. If oranges cost more than apples and bananas cost less than apples, which is cheapest?", ["A) Oranges", "B) Apples", "C) Bananas", "D) Cannot be determined"])
if q4.startswith("C"):
    score += 1

q5 = st.radio("5. Which one is different from the group?", ["A) Circle", "B) Square", "C) Triangle", "D) Rectangle"])
if q5.startswith("A"):
    score += 1

q6 = st.radio("6. If today is Tuesday, what day will it be after 5 days?", ["A) Friday", "B) Saturday", "C) Sunday", "D) Monday"])
if q6.startswith("B"):
    score += 1

q7 = st.radio("7. John is taller than Peter, and Peter is taller than Sam. Who is the tallest?", ["A) Peter", "B) Sam", "C) John", "D) Cannot say"])
if q7.startswith("C"):
    score += 1

q8 = st.radio("8. Complete the series: A, C, E, G, ___", ["A) I", "B) H", "C) J", "D) K"])
if q8.startswith("A"):
    score += 1

q9 = st.radio("9. If you rearrange the letters 'CITY', you get the name of a:", ["A) Fruit", "B) Place", "C) Animal", "D) Bird"])
if q9.startswith("B"):
    score += 1

q10 = st.radio("10. If 1st January is a Sunday, what will be the day on 8th January?", ["A) Monday", "B) Sunday", "C) Saturday", "D) Tuesday"])
if q10.startswith("B"):
    score += 1

st.header("Grammar Questions")

q11 = st.radio("1. Choose the correct sentence:", ["A) He go to school every day.", "B) He goes to school every day.", "C) He gone to school every day.", "D) He going to school every day."])
if q11.startswith("B"):
    score += 1

q12 = st.radio("2. Which is a noun in the sentence: 'The dog barked loudly.'", ["A) The", "B) Dog", "C) Barked", "D) Loudly"])
if q12.startswith("B"):
    score += 1

q13 = st.radio("3. Choose the correct plural form of 'child':", ["A) Childs", "B) Childes", "C) Children", "D) Childrens"])
if q13.startswith("C"):
    score += 1

q14 = st.radio("4. Fill in the blank: She ___ playing in the garden.", ["A) is", "B) are", "C) were", "D) be"])
if q14.startswith("A"):
    score += 1

q15 = st.radio("5. Which word is an adjective in the sentence: 'She has a red dress.'", ["A) She", "B) Has", "C) Red", "D) Dress"])
if q15.startswith("C"):
    score += 1

q16 = st.radio("6. Which is the correct past tense of 'run'?", ["A) Runned", "B) Ran", "C) Running", "D) Runs"])
if q16.startswith("B"):
    score += 1

q17 = st.radio("7. Fill in the blank: I ___ a book now.", ["A) read", "B) am reading", "C) reading", "D) reads"])
if q17.startswith("B"):
    score += 1

q18 = st.radio("8. Which sentence is correct?", ["A) They is playing.", "B) They are play.", "C) They are playing.", "D) They playing are."])
if q18.startswith("C"):
    score += 1

q19 = st.radio("9. Which is a pronoun?", ["A) Happy", "B) Quickly", "C) She", "D) Car"])
if q19.startswith("C"):
    score += 1

q20 = st.radio("10. Choose the correct article: '___ apple a day keeps the doctor away.'", ["A) A", "B) An", "C) The", "D) No article"])
if q20.startswith("B"):
    score += 1

if st.button("Submit and View Score"):
    st.success(f"Your Score: {score} / 20")
    if score < 10:
        st.info("Keep practicing to improve your logical and grammar skills!")
    elif score < 16:
        st.info("Good job! You are on your way to mastery.")
    else:
        st.info("Excellent! You have strong logical and grammar skills.")
