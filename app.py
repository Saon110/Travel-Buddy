import streamlit as st

INTEGRATION_ID = st.secrets["WATSON_INTEGRATION_ID"]
REGION = st.secrets["WATSON_REGION"]
SERVICE_INSTANCE_ID = st.secrets["WATSON_SERVICE_INSTANCE_ID"]

print(INTEGRATION_ID)
print(REGION)
print(SERVICE_INSTANCE_ID)


# Streamlit Page Configuration
st.set_page_config(page_title="Travel Buddy", layout="wide")

# Inline HTML for Full-Screen Background and Content Layout
background_html = """
<style>
body {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
.main {
    background-image: url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1920');
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
}
.content-box {
    background: rgba(0, 0, 0, 0.7);
    color: #ffffff;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    width: 80%;
    max-width: 800px;
}
.chat-icon {
    position: absolute;
    top: 20%;
    right: 5%;
    z-index: 1000;
    cursor: pointer;
}
</style>
<div class="main">
    <div class="content-box">
        <h1>Travel Buddy</h1>
        <p>Welcome to your AI-powered travel assistant! Let us guide you through your travel plans, provide destination suggestions, and answer all your travel questions.</p>
        <p>Start chatting below to get personalized recommendations and make your travel planning seamless and enjoyable.</p>
    </div>
    <div class="chat-icon" id="chat-widget"></div>
</div>
"""

# Inject HTML
st.markdown(background_html, unsafe_allow_html=True)

# Embed Watson Assistant Web Chat Script
watson_chat_script = f"""
<script>
  window.watsonAssistantChatOptions = {{
    integrationID: "{INTEGRATION_ID}", // Integration ID from environment variables
    region: "{REGION}", // Region from environment variables
    serviceInstanceID: "{SERVICE_INSTANCE_ID}", // Service instance ID from environment variables
    onLoad: async (instance) => {{ 
        await instance.render(); 
        const chatButton = document.querySelector('.chat-icon');
        chatButton.addEventListener('click', () => instance.openWindow());
    }}
  }};
  setTimeout(function(){{
    const t=document.createElement('script');
    t.src="https://web-chat.global.assistant.watson.appdomain.cloud/versions/" + 
          (window.watsonAssistantChatOptions.clientVersion || 'latest') + "/WatsonAssistantChatEntry.js";
    document.head.appendChild(t);
  }});
</script>
"""

# Embed Watson Chat Widget
st.components.v1.html(watson_chat_script, height=500)  # Hide default widget; only icon is shown
