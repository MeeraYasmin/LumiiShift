"""
LumiiShift - AI-Powered Mood Tracking Application
A Streamlit app that provides empathetic AI responses to user emotions.
"""

import streamlit as st
import requests
import os
from io import BytesIO
from PIL import Image
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="LumiiShift",
    page_icon="🌈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Constants
THUMBNAIL_URL = "https://raw.githubusercontent.com/MeeraYasmin/LumiiShift/main/asset/LumiiShift.jpg"
API_URL = "https://api.together.ai/v1/chat/completions"
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.3"

def get_api_key():
    """Get API key from environment or user input."""
    # Try to get from environment first
    api_key = os.getenv("TOGETHER_API_KEY")
    
    if not api_key:
        api_key = st.text_input(
            "Enter your Together.ai API key:",
            type="password",
            help="Get your API key from https://together.ai"
        )
        
        if not api_key:
            st.warning("Please enter your API key to use LumiiShift.")
            st.info("💡 Tip: Create a `.env` file with `TOGETHER_API_KEY=your_key` to avoid entering it each time.")
            st.stop()
    
    return api_key

def load_thumbnail():
    """Load and display the app thumbnail."""
    try:
        response = requests.get(THUMBNAIL_URL, timeout=10)
        response.raise_for_status()
        thumbnail = Image.open(BytesIO(response.content))
        st.image(thumbnail, use_container_width=True)
    except requests.RequestException:
        st.warning("Could not load thumbnail image.")

def get_lumiishift_response(mood, api_key):
    """Get AI response for the selected mood."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are LumiiShift, a friendly, safe, empathetic AI companion. "
                    "Provide brief, supportive responses acknowledging the user's mood. "
                    "Be warm, understanding, and encouraging. Keep responses under 50 words."
                ),
            },
            {
                "role": "user",
                "content": f"My current mood is: {mood}."
            }
        ],
        "max_tokens": 100,
        "temperature": 0.7
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        result = response.json()
        
        return result.get("choices", [{}])[0].get("message", {}).get("content", 
                                                                    "I understand how you're feeling. 💙")
    
    except requests.exceptions.HTTPError as e:
        return f"API Error: {e.response.status_code}. Please check your API key."
    except requests.exceptions.Timeout:
        return "Request timed out. Please try again."
    except requests.exceptions.RequestException:
        return "Connection error. Please check your internet connection."

# Initialize session state
if "clicked_mood" not in st.session_state:
    st.session_state.clicked_mood = None
if "lumiishift_reply" not in st.session_state:
    st.session_state.lumiishift_reply = ""

# Main app
def main():
    # Get API key
    api_key = get_api_key()
    
    # Load thumbnail
    load_thumbnail()
    
    # App header
    st.title("🌈 LumiiShift")
    st.markdown("*Click your mood to see a personalized response and color experience!*")
    
    # Import mood map from separate module for better organization
    from mood_data import MOOD_MAP
    
    # Custom CSS for mood buttons
    st.markdown("""
    <style>
    .mood-button {
        transition: all 0.3s ease;
        border-radius: 25px;
        border: 2px solid transparent;
        padding: 10px 20px;
        margin: 5px;
        font-weight: 600;
        text-align: center;
        cursor: pointer;
        animation: pulse 2s infinite;
    }
    
    .mood-button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        border-color: #fff;
    }
    
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.8; }
        100% { opacity: 1; }
    }
    
    .mood-display {
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        margin: 20px 0;
        animation: fadeIn 0.8s ease-in-out;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Mood selection
    st.markdown("### 🎭 Select Your Current Mood:")
    
    # Create mood buttons in a grid
    cols = st.columns(5)
    for idx, (mood, (color, message)) in enumerate(MOOD_MAP.items()):
        with cols[idx % 5]:
            emoji = message.split()[-1] if message.split()[-1].encode('utf-8').isalpha() == False else "💭"
            
            if st.button(
                f"{emoji} {mood.replace('_', ' ').title()}",
                key=mood,
                help=f"Feeling {mood}? {message}"
            ):
                st.session_state.clicked_mood = mood
                
                with st.spinner('Getting your personalized LumiiShift response...'):
                    st.session_state.lumiishift_reply = get_lumiishift_response(mood, api_key)
    
    # Display selected mood and response
    if st.session_state.clicked_mood:
        color, message = MOOD_MAP[st.session_state.clicked_mood]
        mood_display_name = st.session_state.clicked_mood.replace('_', ' ').title()
        
        # Create color-coded mood display
        st.markdown(
            f"""
            <div class="mood-display" style="background: linear-gradient(135deg, {color.lower().replace(' ', '')}, {color.lower().replace(' ', '')}88);">
                <h2 style="color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
                    {mood_display_name}
                </h2>
                <p style="color: white; font-size: 18px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
                    {message}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Display AI response
        st.markdown("### 🤖 LumiiShift Response:")
        st.info(st.session_state.lumiishift_reply)
        
        # Special effects for positive moods
        if st.session_state.clicked_mood in ["happy", "excited", "overjoyed", "joyful"]:
            st.balloons()
        elif st.session_state.clicked_mood in ["calm", "peaceful", "relaxed"]:
            st.snow()

if __name__ == "__main__":
    main()
