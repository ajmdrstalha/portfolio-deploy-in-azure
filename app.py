import requests
from pathlib import Path
from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="AJ MD. RS TALHA",
    layout="wide"
)
#st.set_page_config(page_title="AJ MD. RS TALHA")

def load_lottie_url(url: str):
    try:
        r = requests.get(url, timeout=10)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception:
        return None

APP_DIR = Path(__file__).resolve().parent

def safe_open_image(path: Path):
    try:
        if not path.exists():
            return None
        return Image.open(path)
    except Exception as e:
        st.warning(f"Invalid image: {path.name} ({e})")
        return None

# Updated working Lottie link
lottie_coding = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_0yfsb3a1.json")
lottie_contact = load_lottie_url("https://lottie.host/5dabaff6-7ed5-40ef-b15e-c8d7603d8fec/4oObtAepCE.json")

# image upload for project 1
image1 = safe_open_image(APP_DIR / "images" / "project1.png")
# image upload for project 2
image2 = safe_open_image(APP_DIR / "images" / "project2.png")

# image upload for project 3 (AWS CI/CD)
aws_cicd_image1 = safe_open_image(APP_DIR / "images" / "aws_cicd_image1.png")

# image upload for project 4 (Azure CI/CD)
azure_cicd_image = safe_open_image(APP_DIR / "images" / "Pipeline.jpg")

# image upload for project 5 (Jenkins CI/CD)
jenkins_cicd_image = safe_open_image(APP_DIR / "images" / "jenkins_cicd.jpg")


# ----- Header Section ----
st.subheader("Welcome to my portfolio")
st.title("AJ MD RS TALHA")
st.write("IT DevOps & System Engineer")


# ----- Load CSS for Bootstrap Icons ----
# LinkedIn URL
linkedin_url = "https://www.linkedin.com/in/ajmdrstalha/"
github_url = "https://github.com/ajmdrstalha"
# Load Bootstrap Icons
st.markdown(
    """
    <link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
    """,
    unsafe_allow_html=True,
)

# LinkedIn icon with hyperlink
st.markdown(
    f"""
    <div style="display: flex; gap: 24px; align-items: center;">
        <p>
            <a href="{linkedin_url}" target="_blank" style="text-decoration: none;">
                <i class="bi bi-linkedin" style="font-size: 20px; color: #0A66C2;"></i>
                <span style="font-size: 18px; margin-left: 6px;">LinkedIn</span>
            </a>
        </p>
        <p>
            <a href="{github_url}" target="_blank" style="text-decoration: none;">
                <i class="bi bi-github" style="font-size: 20px; color: #24292e;"></i>
                <span style="font-size: 18px; margin-left: 6px; color: #FFFFFF;">GitHub</span>
            </a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ----- Option Menu ----
with st.container():
    selected = option_menu(
        menu_title=None,
        options=["About", "Experience & Skills", "Certifications", "Projects", "Contact"],
        icons=["person-circle", "1-circle", "patch-check", "code-slash", "chat"],
        orientation="horizontal",
    )
#------About Section ----
if selected == "About":
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("About Me")
            st.write(
                """
                Technology has always been a big part of my life. With more than 2.5 years of experience in networking, I built a strong base in Linux, Cisco, and MikroTik. For the past year, I’ve been working in DevOps, focusing on CI/CD pipelines, Azure, AWS, Docker, Kubernetes, GitHub Actions, Terraform, Ansible, server management, and cybersecurity, all centered on automation and reliability.
                """
            )
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")


# ----- Experience & Skills Section ----
if selected == "Experience & Skills":
    st.write("---")
    st.header("Experience")

    st.markdown(
        """
**IT Support & DevOps Engineer**  
TygrLabs · Full-time  
Aug 2025 – Present · On-site

- Used GitHub, Docker, and Linux for DevOps automation.
- Improved workflows and reduced deployment errors by 25%.
- Hands-on experience with Microsoft Azure, including setting up VMs and managing resources.
- Worked on DevOps workflows to streamline cloud operations.
- Configured and monitored Starlink, MikroTik routers, switches, firewalls, and Wi‑Fi.
- Troubleshot network issues, ensuring 99% uptime.
- Maintained and supported Windows Servers, network devices, and end-user systems; achieved 75% system availability.
- Managed DevOps pipelines for reliable automated deployments.
- Maintained IT infrastructure, including networks, servers, and cloud systems.
        """.strip()
    )

    st.markdown("---")

    st.markdown(
        """
**Network & System Engineer (NOC)**  
Dhaka Fiber Net Ltd. · Full-time  
Jan 2025 – Jul 2025 · 7 mos · Dhaka, Bangladesh · On-site

- Automated OLT commands using Python, increasing service delivery speed by 60%.
- Deployed network automation scripts via GitHub, improving DevOps readiness by 20%.
- Monitored and controlled network performance in a NOC environment, ensuring 99.9% uptime with automation and management tools.
- Worked on OLT systems, Cisco routers/switches, MikroTik routers, and Ubuntu servers.
- Designed and implemented chatbot workflows in ReveChat to automate customer conversations and reduce manual support workload.
        """.strip()
    )

    st.markdown("---")

    st.markdown(
        """
**Network Support Engineer**  
ASIANET Online Service · Full-time  
Jan 2024 – Dec 2024 · 1 yr · Uttara, Dhaka, Bangladesh

- Optimized network support and management with Python and MikroTik, boosting efficiency by 25%.
- Configured and managed MikroTik routers, VLANs, PPPoE, DHCP, NAT, and firewall settings.
- Monitored networks and troubleshot issues using WinBox and The Dude.
        """.strip()
    )

    st.write("---")
    st.header("Skills")
    st.markdown(
        """
- Version Control
- Linux (Ubuntu, RedHat)
- Scripting & Automation (Python, Bash)
- Networking (TCP/IP, DNS, DHCP)
- Containerization & Orchestration (Docker, Kubernetes)
- Cloud Computing (AZURE, AWS)
- CI/CD (Jenkins, GitHub Actions)
- Infrastructure as Code (Terraform, Ansible)
- Monitoring & Logging (Prometheus, Grafana)
        """.strip()
    )

    # Stop here so the old "Skills" + "Soft Skills" sections below don't render.
    st.stop()
    st.markdown(
        """
        <ul style="list-style: none; padding-left: 0;">
            <li>- Version Control</li>
            <li>- Linux (Ubuntu, RedHat)</li>
            <li>- Scripting & Automation (Python, Bash)</li>
            <li>- Networking (TCP/IP, DNS, DHCP)</li>
            <li>- Containerization & Orchestration (Docker, Kubernetes)</li>
            <li>- Cloud Computing (AZURE, AWS)</li>
            <li>- CI/CD (Jenkins, GitHub Actions)</li>
            <li>- Infrastructure as Code (Terraform, Ansible)</li>
            <li>- Monitoring & Logging (Prometheus, Grafana)</li>
        </ul>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <h3>Soft Skills</h3>
        <ul style="list-style: none; padding-left: 0;">
            <li>- Problem Solving</li>
            <li>- Team Collaboration</li>
            <li>- Communication</li>
            <li>- Adaptability</li>
            <li>- Time Management</li>
        </ul>
        """,
        unsafe_allow_html=True
    )

# ----- Certifications ----
if selected == "Certifications":
    st.write("---")
    st.header("Certifications")
    st.write("##")
    st.markdown(
    """
**Fortinet NSE Certification**  
Issuer: Fortinet · Issued: Dec 2025  
Course: Introduction the Threat Landscape 3.0

---

**DevOps Professional Training Certification**  
Issuer: Interactive Cares · Issued: Apr 2025

---

**RedHat Professional Training Certification**  
Issuer: Atova Technology · Issued: Jan 2025

---

**MikroTik Certified Network Associate (MTCNA)**  
Issuer: MikroTik · Issued: Nov 2024  
Credential ID: 2411NA9081  
Skills: Network Configuration · MikroTik RouterOS · Routing Protocols · NAT Configuration · Firewall Management · VPN Configuration · Troubleshooting · Switching & VLAN Configuration · QoS

---

**CCNA Professional Training Certification**  
Issuer: Atova Technology · Issued: Jun 2024

---

**APNIC Certifications**  
Issuer: APNIC · Issued: Jan 2024  
Courses: Routing Fundamentals · Intro to BGP · OSPF · IPv6 Fundamentals · IPv6 Address Planning

---

**Cisco Networking Academy Certifications**  
Issuer: Cisco Networking Academy · Issued: Jan 2024  
Courses: Introduction to Modern AI · IT Essentials · Junior Cybersecurity Analyst Career Path · Linux Essentials · Network Addressing & Basic Troubleshooting · Networking Basics

---

**MikroTik Professional Training Certification**  
Issuer: Atova Technology · Issued: Aug 2023
    """.strip()
    )

# ----- Projects ----
if selected == "Projects":
    st.write("---")
    st.header("Projects")
    st.write("##")

    # Project: CI/CD with Azure
    image_column, text_column = st.columns((1, 2))
    with image_column:
        if azure_cicd_image:
            st.image(azure_cicd_image, caption="")

    with text_column:
        st.subheader("CI/CD with Azure")
        st.write(
            """
            - Azure Container Registry (ACR) stores Docker images
            - Azure VM hosts the application
            - Azure Pipelines (YAML) automates build & deploy
            """
        )
        st.markdown("**Skills:** Microsoft Azure · DevOps · Azure DevOps Services · CI/CD")

    st.write("##")

    # Project: Jenkins CI/CD Pipeline
    image_column, text_column = st.columns((1, 2))
    with image_column:
        if jenkins_cicd_image:
            st.image(jenkins_cicd_image, caption="")

    with text_column:
        st.subheader("Jenkins CI/CD Pipeline Project")
        st.write(
            """
            - Built a CI/CD pipeline using Jenkins and Git
            - Automated build, testing, and deployment on every code push
            - Improved delivery speed and reliability with consistent automation
            """
        )
        st.markdown("**Skills:** Jenkins · CI/CD")

    st.write("##")

    # Project: Portfolio Deployment with CI/CD (AWS)
    image_column, text_column = st.columns((1, 2))
    with image_column:
        if aws_cicd_image1:
            st.image(aws_cicd_image1, caption="")

    with text_column:
        st.subheader("Portfolio Deployment with CI/CD (AWS)")
        st.write(
            """
            - Built and containerized the portfolio using Docker
            - Automated build/test/deploy with GitHub Actions on every push
            - Deployed and hosted the app on AWS for reliable delivery
            """
        )
        st.markdown("**Skills:** DevOps · Amazon Web Services (AWS) · GitHub Actions · Docker")
        st.markdown("[GitHub Repo](https://github.com/ajmdrstalha/Python_Protfolio_Website)")
        st.markdown("[Website Portfolio](https://ajmdrstalha.xyz)")

    st.write("##")

    image_column, text_column = st.columns((1, 2))
    with image_column:
        if image1:
            st.image(image1, caption="")

    with text_column:
        st.subheader("OLT Auto Command")
        st.write(
            """
            - Automated OLT power-check commands to reduce manual work
            - Built a simple Streamlit UI for faster operations
            - Packaged everything in Docker for easy, consistent runs
            """
        )
        st.markdown("[GitHub](https://github.com/ajmdrstalha/Epon-Command-Generator)")

    
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        if image2:
            st.image(image2, caption="")

    with text_column:
        st.subheader("Networking Project")
        st.write(
            """
                        - Configured VLANs, inter-VLAN routing, and EtherChannel on Cisco devices
                        - Implemented STP tuning / load balancing for resilient switching
                        - Secured access with SSH + port security and optimized addressing (VLSM/SLSM)
            """
        )    
        st.markdown("[File](https://drive.google.com/drive/folders/1NzzuxnJufYZXCIGWM7CDsw-z65xyFdAR)")
  
#----- Contact Section ----
if selected == "Contact":
    col1, col2 = st.columns(2)
    with col1:
        st.write("##")
        st.header("Contact Me")
        st.markdown(
            """
            Email: <a href="mailto:ajmdrstalha@gmail.com">ajmdrstalha@gmail.com</a>
            """,
            unsafe_allow_html=True
        )
    with col2:
        st_lottie(lottie_contact, height=350, key="contact")