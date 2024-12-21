import streamlit as st
from PIL import Image, ImageOps, ImageDraw
import base64
import os

image_path = "my/my_photo.jpg"
if not os.path.exists(image_path):
    st.error(f"Image file not found: {image_path}")
else:
    img = Image.open(image_path)

# Sidebar Navigation
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def make_rounded_image(image_path, size=(150, 150)):
    img = Image.open(image_path).convert("RGBA")
    img = img.resize(size, Image.Resampling.LANCZOS)

    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size[0], size[1]), fill=255)

    rounded_img = ImageOps.fit(img, size, centering=(0.5, 0.5))
    rounded_img.putalpha(mask)
    return rounded_img

page = st.sidebar.selectbox("Select a Page", ["CV", "Portfolio"])

if page == "CV":
    st.title('CV of Abdulrhman Salama')

    image_path = "my/my_photo.jpg"
    img = Image.open(image_path)

    img = img.convert("RGB")
    width, height = img.size
    diameter = min(width, height)

    img_cropped = ImageOps.fit(img, (diameter, diameter), method=0)
    mask = Image.new('L', (diameter, diameter), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, diameter, diameter), fill=255)

    img_circular = Image.new('RGB', (diameter, diameter))
    img_circular.paste(img_cropped, (0, 0), mask=mask)

    st.image(img_circular, caption='Abdulrhman Salama', width=300)

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
        team_photo_rounded = make_rounded_image(team_photo_path)

        st.write("### MEC Academy - AI Course")
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(certificate_path, caption="Certificate of AI from MEC Academy", use_column_width=True)
        with col2:
            st.image(team_photo_rounded, caption="Team photo with MEC Academy", use_column_width=False)

        st.write("### MaharaTec - AI Course")
        st.image("certificate/AI_Mahara_tec.png", caption="Certificate of AI from MaharaTec")

        st.write("### MaharaTec - Database Fundamentals")
        st.image("certificate/database_fundamentals_mahara_tec.png", caption="Certificate of Database Fundamentals")

        st.write("### MaharaTec - Python Basic")
        st.image("certificate/Python_basic_mahara_tec.png", caption="Certificate of Python Basic")

        certificate_path = "certificate/we_Training.jpg"
        team_photo_path = "my/we_best_trainer.jpg"
        team_photo_rounded = make_rounded_image(team_photo_path)

        st.write("### [WE] Egyptian Telecommunications Training")
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(certificate_path, caption="Training Certificate from WE", use_column_width=True)
        with col2:
            st.image(team_photo_rounded, caption="Best Trainer Certificate from WE", use_column_width=False)

    st.header("Contact Information")
    st.write("""
    - **Email**: bdalrhmnslmt@gmail.com
    - **LinkedIn**: [LinkedIn Profile](https://www.linkedin.com/in/abdulrhman-salama-908a09255)
    - **GitHub**: [GitHub Profile](https://github.com/abdulrhmansalama)
    - **Phone**: +201090586412
    """)

# صفحة المحفظة (Portfolio)
elif page == "Portfolio":
    # Portfolio Page
    st.title('Portfolio of Abdulrhman Salama')

    st.header("About Me")
    st.write("""
    Hello! I am Abdulrhman Salama, a Computer Engineering student passionate about Artificial Intelligence and Machine Learning.
    Below are some of the projects and work I have done related to AI, machine learning, and more.
    """)

    # Projects Section
    st.header("Projects")
    st.write("""
    - **AI-based Prediction Model**: A machine learning model used to predict [something]. Technologies used: Python, Scikit-learn.
    - **Image Recognition with Deep Learning**: A deep learning model trained to recognize objects in images. Technologies used: TensorFlow, Keras.
    - **Data Analysis Project**: Analyzing large datasets using machine learning algorithms to extract insights. Technologies used: Python, Pandas, Scikit-learn.
    """)

    # GitHub or Project Links
    st.header("GitHub & Repositories")
    st.write("""
    Check out my projects on GitHub:
    - [GitHub Repository 1](https://github.com/yourusername/project1)
    - [GitHub Repository 2](https://github.com/yourusername/project2)
    """)

    # Kaggle Profile
    st.header("Kaggle Profile")
    st.write("""
    Explore my work and notebooks on Kaggle:
    - [Kaggle Profile](https://www.kaggle.com/abdulrhmansalama)
    """)

    # Additional Information
    st.header("Other Work")
    st.write("""
    - **Blog Posts**: I've written a few blog posts about AI and machine learning. You can check them out here: [Blog Link].
    - **Open Source Contributions**: I actively contribute to open-source projects, especially in AI and machine learning.
    """)

    # Contact Information (same as CV)
    st.header("Contact Information")
    st.write("""
    - **Email**: bdalrhmnslmt@gmail.com
    - **LinkedIn**: [LinkedIn Profile](https://www.linkedin.com/in/abdulrhman-salama-908a09255)
    - **GitHub**: [GitHub Profile](https://github.com/abdulrhmansalama)
    """)
