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
        return Image.open(path)
    except Exception as e:
        st.warning(f"Missing/invalid image: {path.name} ({e})")
        return None

# Updated working Lottie link
lottie_coding = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_0yfsb3a1.json")
lottie_contact = load_lottie_url("https://lottie.host/5dabaff6-7ed5-40ef-b15e-c8d7603d8fec/4oObtAepCE.json")

# image upload for project 1
image1 = safe_open_image(APP_DIR / "images" / "project1.png")
# image upload for project 2
image2 = safe_open_image(APP_DIR / "images" / "project2.png")


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
        options=["About", "Experience & Skills", "Projects", "Contact"],
        icons=["person-circle","1-circle" , "code-slash", "chat"],
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
Aug 2025 – Present · 6 mos · On-site

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

# ----- Projects ----
if selected == "Projects":
    st.write("---")
    st.header("Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        if image1:
            st.image(image1, caption="")

    with text_column:
        st.subheader("OLT Auto Command")
        st.write(
            """
             Discover how to automate OLT power checks command with Python and Streamlit, all wrapped up in a Docker container to minimize manual errors and save you precious time.
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
              Configured Cisco routers and switches with VLANs, inter-VLAN routing, EtherChannel, and STP load-balancing. 
              Secured the network using port security and SSH, and optimized IP addressing through SLSM, VLSM, and other techniques.
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