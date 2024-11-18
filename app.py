import streamlit as st

# Streamlit Page Configuration
st.set_page_config(page_title="Travel Buddy", layout="centered")

# Background Image and Custom CSS
page_bg = """
<style>
body {
    background-image: './env.jpeg' ; /* Reliable travel-themed image */
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
    font-family: Arial, sans-serif;
}

h1 {
    color: #ffffff;
    text-align: center;
    font-size: 3rem;
    margin-top: 20px;
}

.intro-box {
    background: rgba(0, 0, 0, 0.6); /* Semi-transparent black background */
    color: #ffffff;
    padding: 20px;
    border-radius: 10px;
    margin: 20px auto;
    text-align: center;
    width: 80%;
}

.intro-box h2 {
    font-size: 2rem;
}

.intro-box p {
    font-size: 1.2rem;
    line-height: 1.6;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# App Title
st.markdown("<h1>Travel Buddy</h1>", unsafe_allow_html=True)

# Welcome Message and Introduction
intro_text = """
<div class="intro-box">
    <h2>Welcome to Travel Buddy!</h2>
    <p>
        Your ultimate AI-powered travel assistant. Let us help you plan your journeys, discover new destinations, 
        and answer any travel-related questions you may have. Whether you're dreaming of a relaxing beach holiday, 
        a thrilling adventure, or a cultural city break, we're here to make your travel dreams come true!
    </p>
    <p>
        Start chatting below to explore the best travel options, get recommendations, and enjoy a seamless travel planning experience.
    </p>
</div>
"""
st.markdown(intro_text, unsafe_allow_html=True)

# Embed Watson Assistant Web Chat Script
watson_chat_script = """
<script>
  window.watsonAssistantChatOptions = {
    integrationID: "6850854c-7e26-4fb8-a645-759885a79662", // The ID of this integration.
    region: "eu-gb", // The region your integration is hosted in.
    serviceInstanceID: "5942c55e-23f0-46bc-9149-00dd4ea5a70b", // The ID of your service instance.
    onLoad: async (instance) => { await instance.render(); }
  };
  setTimeout(function(){
    const t=document.createElement('script');
    t.src="https://web-chat.global.assistant.watson.appdomain.cloud/versions/" + 
          (window.watsonAssistantChatOptions.clientVersion || 'latest') + "/WatsonAssistantChatEntry.js";
    document.head.appendChild(t);
  });
</script>
"""

# Display Watson Chat Widget
st.components.v1.html(watson_chat_script, height=500)
