import streamlit as st
from PIL import Image, ImageOps, ImageDraw
import base64
import os
# Define the image path with the absolute path
image_path = "C:\\Users\\bdalr\\Desktop\\cv\\public\\my\\my_photo.jpg"

# Check if the image exists
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

# Sidebar Navigation for Pages
page = st.sidebar.selectbox("Select a Page", ["CV", "Portfolio"])

if page == "CV":
    st.title('CV of Abdulrhman Salama')

    # Handle missing image gracefully
    if os.path.exists(image_path):
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

        # Example Certificate Display
        certificate_path = "C:\\Users\\bdalr\\Desktop\\cv\\public\\certificate\\Ai_mec.jpg"
        team_photo_path = "C:\\Users\\bdalr\\Desktop\\cv\\public\\my\\mec_academy.jpg"

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
        st.image("C:\\Users\\bdalr\\Desktop\\cv\\public\\certificate\\AI_Mahara_tec.png", caption="Certificate of AI from MaharaTec")

        st.write("### MaharaTec - Database Fundamentals")
        st.image("C:\\Users\\bdalr\\Desktop\\cv\\public\\certificate\\database_fundamentals_mahara_tec.png", caption="Certificate of Database Fundamentals")

        st.write("### MaharaTec - Python Basic")
        st.image("C:\\Users\\bdalr\\Desktop\\cv\\public\\certificate\\Python_basic_mahara_tec.png", caption="Certificate of Python Basic")

    st.header("Contact Information")
    st.write("""
    - **Email**: bdalrhmnslmt@gmail.com
    - **LinkedIn**: [LinkedIn Profile](https://www.linkedin.com/in/abdulrhman-salama-908a09255)
    - **GitHub**: [GitHub Profile](https://github.com/abdulrhmansalama)
    - **Phone**: +201090586412
    """)

elif page == "Portfolio":
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

    # Contact Information


    # Function to convert image to base64
    def image_to_base64(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    # Paths for the logo images (LinkedIn, GitHub, Email, WhatsApp)
    linkedin_logo_path = "C:\\Users\\bdalr\\Desktop\\cv\\public\\logo\\LinkedIn.png"
    github_logo_path = "C:\\Users\\bdalr\\Desktop\\cv\\public\\logo\\GitHub.png"
    email_logo_path = "C:\\Users\\bdalr\\Desktop\\cv\\public\\logo\\Email.png"
    whatsapp_logo_path = "C:\\Users\\bdalr\\Desktop\\cv\\public\\logo\\WhatsApp.png"  # WhatsApp logo path

    # Convert the logos to base64
    linkedin_logo_base64 = image_to_base64(linkedin_logo_path)
    github_logo_base64 = image_to_base64(github_logo_path)
    email_logo_base64 = image_to_base64(email_logo_path)
    whatsapp_logo_base64 = image_to_base64(whatsapp_logo_path)  # Convert WhatsApp logo

    # HTML button with image (LinkedIn)
    linkedin_button_html = f"""
    <div style="text-align: center; margin-top: 20px;">
        <a href="https://www.linkedin.com/in/abdulrhman-salama-908a09255" target="_blank" style="
            display: inline-block;
            background-color: #0077B5;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            font-size: 16px;
            border-radius: 5px;
            border: none;
            text-align: center;
        ">
            <img src="data:image/png;base64,{linkedin_logo_base64}" alt="LinkedIn Logo" style="vertical-align: middle; width: 25px; height: 25px; margin-right: 8px;">
            LinkedIn Profile
        </a>
    </div>
    """

    # HTML button with image (GitHub)
    github_button_html = f"""
    <div style="text-align: center; margin-top: 20px;">
        <a href="https://github.com/abdulrhmansalama" target="_blank" style="
            display: inline-block;
            background-color: #333;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            font-size: 16px;
            border-radius: 5px;
            border: none;
            text-align: center;
        ">
            <img src="data:image/png;base64,{github_logo_base64}" alt="GitHub Logo" style="vertical-align: middle; width: 25px; height: 25px; margin-right: 8px;">
            GitHub Profile
        </a>
    </div>
    """

    # HTML button with image (Email)
    email_button_html = f"""
    <div style="text-align: center; margin-top: 20px;">
        <a href="mailto:bdalrhmnslmt@gmail.com" style="
            display: inline-block;
            background-color: #D14836;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            font-size: 16px;
            border-radius: 5px;
            border: none;
            text-align: center;
        ">
            <img src="data:image/png;base64,{email_logo_base64}" alt="Email Logo" style="vertical-align: middle; width: 25px; height: 25px; margin-right: 8px;">
            Send Email
        </a>
    </div>
    """

    # HTML button with image (WhatsApp)
    whatsapp_button_html = f"""
    <div style="text-align: center; margin-top: 20px;">
        <a href="https://wa.me/+201090586412" target="_blank" style="
            display: inline-block;
            background-color: #25D366;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            font-size: 16px;
            border-radius: 5px;
            border: none;
            text-align: center;
        ">
            <img src="data:image/png;base64,{whatsapp_logo_base64}" alt="WhatsApp Logo" style="vertical-align: middle; width: 25px; height: 25px; margin-right: 8px;">
            Chat on WhatsApp
        </a>
    </div>
    """

    # Now, let's integrate this into your Streamlit app
    st.title('Contact Information')

    st.write("You can reach me via the following channels:")
# Create two columns for layout
col1, col2 = st.columns(2)

# Display LinkedIn and GitHub buttons in the first column
with col1:
    st.markdown(linkedin_button_html, unsafe_allow_html=True)
    st.markdown(github_button_html, unsafe_allow_html=True)

# Display Email and WhatsApp buttons in the second column
with col2:
    st.markdown(email_button_html, unsafe_allow_html=True)
    st.markdown(whatsapp_button_html, unsafe_allow_html=True)
