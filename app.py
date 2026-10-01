import streamlit as st

# Page Configuration
st.set_page_config(page_title="Best of Luck & Happy Birthday! 🎉", page_icon="🎂", layout="centered")

# Native Streamlit Balloons
st.balloons()

# Direct Pure HTML Rendering
html_content = """
<style>
.stApp {
    background: linear-gradient(135deg, #a8c0ff 0%, #3f2b96 100%);
}
.interview-card {
    background-color: #ffffff;
    padding: 35px 20px;
    border-radius: 25px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.25);
    text-align: center;
    margin: 10px auto;
    border-top: 10px solid #ff4b2b;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.giant-heading {
    font-size: 32px;
    font-weight: 900;
    color: #ff2a5f;
    text-transform: uppercase;
    letter-spacing: 1px;
    line-height: 1.3;
    margin: 20px 0;
}
.custom-para {
    font-size: 18px;
    color: #2c3e50;
    line-height: 1.7;
    text-align: center;
    background-color: #f7f9fc;
    padding: 20px;
    border-radius: 18px;
    border-left: 6px solid #3f2b96;
    margin-bottom: 25px;
    font-weight: 500;
}
.bday-card {
    background: linear-gradient(135deg, #ff0844 0%, #ffb199 100%);
    color: white;
    padding: 20px;
    border-radius: 18px;
    font-size: 26px;
    font-weight: 900;
    letter-spacing: 1px;
    box-shadow: 0 8px 20px rgba(255, 8, 68, 0.3);
    text-transform: uppercase;
}
.badge {
    display: inline-block;
    background-color: #eef2f5;
    color: #333;
    padding: 8px 14px;
    margin: 4px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: bold;
}
</style>

<div class="interview-card">
    <div style="font-size: 55px; margin-bottom: 10px;">💼 🎯 👔 ✨</div>
    <div>
        <span class="badge">🚀 Future Star</span>
        <span class="badge">🌟 Ace The Test</span>
        <span class="badge">💪 You Got This!</span>
    </div>
    
    <div class="giant-heading">
        BEST OF LUCKK FOR UR INTERVIEWWWW CUTUUU
    </div>
    
    <div class="custom-para">
        hiieee barkuuuuuuuu bhut acha intervieww dooo
        or dete rhoo yk just practicee or in sha allah 
        bhuttt achi achi jgh se barku k pass offers ayengin
        k madam dekhen gin areh bhaee jaon toh jaon khnn yeaaa
        toh hope for the bestt cutuuu , 
        in sha allah u will ace ur interviewss
        ( yeh vocabs aapki nh thin ai smjhhhh betuu )
    </div>
    
    <div class="bday-card">
        🎈 ALSOOOOO <br> HAPPY BIRTHDAYY CUTUUUU 🎂🎉
    </div>
</div>
"""

st.html(html_content)
