import streamlit as st
from PIL import Image, ImageOps, ImageDraw
import base64
import os

# Paths for images
image_path = "my/my_photo.jpg"
linkedin_logo_path = "logo/LinkedIn.png"
github_logo_path = "logo/GitHub.png"
email_logo_path = "logo/Email.png"
whatsapp_logo_path = "logo/WhatsApp.png"

def image_to_base64(image_path):
    """Convert an image file to base64 encoding."""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return None

def make_rounded_image(image_path, size=(150, 150)):
    """Create a circular version of the image."""
    try:
        img = Image.open(image_path).convert("RGBA")
        img = img.resize(size, Image.Resampling.LANCZOS)

        mask = Image.new("L", size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size[0], size[1]), fill=255)

        rounded_img = ImageOps.fit(img, size, centering=(0.5, 0.5))
        rounded_img.putalpha(mask)
        return rounded_img
    except FileNotFoundError:
        return None

# Convert images to base64 for HTML usage
linkedin_logo_base64 = image_to_base64(linkedin_logo_path)
github_logo_base64 = image_to_base64(github_logo_path)
email_logo_base64 = image_to_base64(email_logo_path)
whatsapp_logo_base64 = image_to_base64(whatsapp_logo_path)

# HTML button templates for each button with base64 logo images
linkedin_button_html = f"""<a href="https://linkedin.com" target="_blank"><img src="data:image/png;base64,{linkedin_logo_base64}" width="30"></a>""" if linkedin_logo_base64 else ""
github_button_html = f"""<a href="https://github.com" target="_blank"><img src="data:image/png;base64,{github_logo_base64}" width="30"></a>""" if github_logo_base64 else ""
email_button_html = f"""<a href="mailto:example@example.com" target="_blank"><img src="data:image/png;base64,{email_logo_base64}" width="30"></a>""" if email_logo_base64 else ""
whatsapp_button_html = f"""<a href="https://wa.me/123456789" target="_blank"><img src="data:image/png;base64,{whatsapp_logo_base64}" width="30"></a>""" if whatsapp_logo_base64 else ""

# Sidebar Navigation
page = st.sidebar.selectbox("Select a Page", ["CV", "Portfolio"])

if page == "CV":
    st.title('CV of Abdulrhman Salama')

    # Display profile image
    try:
        img = make_rounded_image(image_path)
        if img:
            st.image(img, caption='Abdulrhman Salama', width=150)
        else:
            st.warning("Profile image not found.")
    except Exception as e:
        st.error(f"Error displaying profile image: {e}")

    st.header("Personal Information")
    st.write("""
    - **Full Name**: Abdulrhman Salama
    - **Specialization**: Computer Engineering
    - **Interests**: Artificial Intelligence (AI) and Machine Learning
    - **Current Year**: 3rd Year, Computer Engineering
    """)

    st.header("Education")
    st.write("""
    - **University**: Alexandria
    - **Degree Program**: Bachelor in Computer Engineering
    - **Expected Graduation Year**: 2026
    """)

    st.header("Skills")
    st.write("""
    - **Programming Languages**: Python, C++, SQL
    - **Machine Learning Libraries**: TensorFlow, Keras, Scikit-learn
    - **AI Concepts**: Neural Networks, Deep Learning, Reinforcement Learning
    - **Tools & Software**: MATLAB, Jupyter, Git, Docker
    """)

    st.header("Projects")
    st.write("""
    - **AI-based Prediction Model**: Developed a model to predict outcomes using machine learning techniques.
    - **Image Recognition with Deep Learning**: Trained models for object detection and image classification.
    - **Data Analysis Project**: Explored and analyzed datasets for insights using Python.
    """)

    st.header("Certifications")
    st.write("""
    - **AI & Machine Learning**: Completed courses from MEC Academy, MaharaTec, Coursera.
    """)

    if st.button('See More'):
        st.subheader("Detailed Certificates")

        certificate_path = "certificate/Ai_mec.jpg"
        team_photo_path = "my/mec_academy.jpg"

        if os.path.exists(certificate_path) and os.path.exists(team_photo_path):
            team_photo_rounded = make_rounded_image(team_photo_path)

            st.write("### MEC Academy - AI Course")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.image(certificate_path, caption="Certificate of AI from MEC Academy", use_column_width=True)
            with col2:
                st.image(team_photo_rounded, caption="Team photo with MEC Academy", use_column_width=False)
        else:
            st.error("Certificates or photos not found.")

        st.write("### MaharaTec - AI Course")
        st.image("certificate/AI_Mahara_tec.png", caption="Certificate of AI from MaharaTec")

        st.write("### MaharaTec - Database Fundamentals")
        st.image("certificate/database_fundamentals_mahara_tec.png", caption="Certificate of Database Fundamentals")

        st.write("### MaharaTec - Python Basic")
        st.image("certificate/Python_basic_mahara_tec.png", caption="Certificate of Python Basic")

         # Load and prepare images
        certificate_path = "certificate/we_Training.jpg"
        team_photo_path = "my/we_best_trainer.jpg"
        team_photo_rounded = make_rounded_image(team_photo_path)

        # WE Training Certificate
        st.write("### [WE] Egyptian Telecommunications Training")
        col1, col2 = st.columns([1, 1])  # Create two columns for layout
        with col1:
            st.image(certificate_path, caption="Training Certificate from WE", use_column_width=True)
        with col2:
            st.image(team_photo_rounded, caption="Best Trainer Certificate from WE", use_column_width=False)

    

    st.header("Contact Information")
    st.write("""
    You can reach me via the following channels:
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(linkedin_button_html, unsafe_allow_html=True)
        st.markdown(github_button_html, unsafe_allow_html=True)

    with col2:
        st.markdown(email_button_html, unsafe_allow_html=True)
        st.markdown(whatsapp_button_html, unsafe_allow_html=True)

elif page == "Portfolio":
    st.title('Portfolio of Abdulrhman Salama')

    st.header("About Me")
    st.write("""
    Hello! I am Abdulrhman Salama, a Computer Engineering student passionate about Artificial Intelligence and Machine Learning.
    Below are some of the projects and work I have done related to AI, machine learning, and more.
    """)

    st.header("Projects")
    st.write("""
    - **AI-based Prediction Model**: A machine learning model used to predict [something]. Technologies used: Python, Scikit-learn.
    - **Image Recognition with Deep Learning**: A deep learning model trained to recognize objects in images. Technologies used: TensorFlow, Keras.
    - **Data Analysis Project**: Analyzing large datasets using machine learning algorithms to extract insights. Technologies used: Python, Pandas, Scikit-learn.
    """)

    st.header("GitHub & Repositories")
    st.write("""
    Check out my projects on GitHub:
    - [GitHub Repository 1](https://github.com/yourusername/project1)
    - [GitHub Repository 2](https://github.com/yourusername/project2)
    """)

    st.header("Kaggle Profile")
    st.write("""
    Explore my work and notebooks on Kaggle:
    - [Kaggle Profile](https://www.kaggle.com/abdulrhmansalama)
    """)

    st.header("Other Work")
    st.write("""
    - **Blog Posts**: I've written a few blog posts about AI and machine learning. You can check them out here: [Blog Link].
    - **Open Source Contributions**: I actively contribute to open-source projects, especially in AI and machine learning.
    """)

    st.header("Contact Information")
    st.write("""
    You can reach me via the following channels:
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(linkedin_button_html, unsafe_allow_html=True)
        st.markdown(github_button_html, unsafe_allow_html=True)

    with col2:
        st.markdown(email_button_html, unsafe_allow_html=True)
        st.markdown(whatsapp_button_html, unsafe_allow_html=True)
