import streamlit as st
from PIL import Image, ImageOps, ImageDraw
import base64

# CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
        font-family: Arial, sans-serif;
        color: #333;
    }
    .container {
        margin: 0 auto;
        text-align: center;
    }
    .title {
        font-size: 36px;
        color: #0078d7;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 18px;
        color: #555;
        margin-bottom: 20px;
    }
    .profile-pic {
        border-radius: 50%;
        width: 150px;
        height: 150px;
        object-fit: cover;
        border: 3px solid #0078d7;
    }
    .social-icons a img {
        margin: 0 10px;
        transition: transform 0.3s ease;
    }
    .social-icons a img:hover {
        transform: scale(1.2);
    }
    .section-header {
        font-size: 24px;
        color: #0078d7;
        margin-top: 30px;
        margin-bottom: 10px;
    }
    .button-container {
        margin-top: 20px;
    }
    .button {
        background-color: #0078d7;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        text-decoration: none;
        font-size: 16px;
        cursor: pointer;
    }
    .button:hover {
        background-color: #005bb5;
    }
    </style>
""", unsafe_allow_html=True)

# Profile Section
st.markdown('<div class="container">', unsafe_allow_html=True)
st.markdown('<div class="title">CV of Abdulrhman Salama</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Computer Engineering Student | AI & Machine Learning Enthusiast</div>', unsafe_allow_html=True)

# Profile Picture
image_path = "my/my_photo.jpg"
try:
    profile_image = Image.open(image_path)
    profile_image.save("profile.png")
    st.image("profile.png", width=150, caption="Abdulrhman Salama", use_column_width=False)
except FileNotFoundError:
    st.warning("Profile image not found.")

# Personal Information
st.markdown('<div class="section-header">Personal Information</div>', unsafe_allow_html=True)
st.markdown("""
<ul>
    <li><strong>Full Name:</strong> Abdulrhman Salama</li>
    <li><strong>Specialization:</strong> Computer Engineering</li>
    <li><strong>Interests:</strong> Artificial Intelligence (AI) and Machine Learning</li>
    <li><strong>Current Year:</strong> 3rd Year, Computer Engineering</li>
</ul>
""", unsafe_allow_html=True)

# Social Icons
linkedin_logo = "path_to_your_image/LinkedIn.png"  # Add correct paths
github_logo = "path_to_your_image/GitHub.png"
email_logo = "path_to_your_image/Email.png"
whatsapp_logo = "path_to_your_image/WhatsApp.png"

st.markdown('<div class="section-header">Contact Information</div>', unsafe_allow_html=True)
st.markdown('<div class="social-icons">', unsafe_allow_html=True)
st.markdown(f'<a href="https://www.linkedin.com/in/abdulrhman-salama-908a09255/" target="_blank"><img src="data:image/png;base64,{linkedin_logo}" width="30"></a>', unsafe_allow_html=True)
st.markdown(f'<a href="https://github.com/abdulrhmansalama" target="_blank"><img src="data:image/png;base64,{github_logo}" width="30"></a>', unsafe_allow_html=True)
st.markdown(f'<a href="mailto:bdalrhmnslmt@gmail.com" target="_blank"><img src="data:image/png;base64,{email_logo}" width="30"></a>', unsafe_allow_html=True)
st.markdown(f'<a href="https://wa.me/+201090586412" target="_blank"><img src="data:image/png;base64,{whatsapp_logo}" width="30"></a>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="button-container">', unsafe_allow_html=True)
st.markdown('<a href="https://www.linkedin.com/in/abdulrhman-salama-908a09255/" class="button">Connect with me</a>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
