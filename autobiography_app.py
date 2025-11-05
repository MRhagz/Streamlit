import streamlit as st
import pandas as pd
import time

# --- Page Configuration ---
st.set_page_config(
    page_title="About Moen",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.google.com',
        'Report a bug': None,
        'About': "This is an autobiographical app for Moen Malone I. Rago."
    }
)

# --- Sidebar ---
# The sidebar is used for navigation, interaction, and supplementary info.
with st.sidebar:
    st.image("static/grad_pic.JPG", 
             use_container_width=True) # <-- Corrected parameter
    
    st.title("Moen Malone I. Rago")
    st.caption("Computer Science Student")
    
    st.divider()

    # --- Interactive Widgets ---
    st.header("Connect with Me")
    
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send")
        
        if submitted:
            st.success("Message sent! (Note: This is a demo)")
            st.toast("Thank you for connecting!")

    st.divider()
    
    # --- More Widgets for Demonstration ---
    st.subheader("Rate This Bio")
    rating = st.slider("How insightful was this story?", 0, 10, 8)
    
    st.subheader("Stay Updated")
    st.checkbox("Subscribe to my future projects newsletter?")
    
    st.subheader("Visit Date")
    st.date_input("When are you reading this?")

# --- Main Page Content ---
st.title("About Moen")
st.markdown("Welcome to my personal and professional journey.")

# --- Using Tabs for Sections ---
# Tabs are a great way to organize a lot of content without a long scroll.
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
    "I. Introduction", 
    "II. Early Life", 
    "III. Education", 
    "IV. Present Life", 
    "V. Hobbies", 
    "VI. Challenges", 
    "VII. Inspirations", 
    "VIII. Goals", 
    "IX. Conclusion"
])

# --- Tab 1: Introduction ---
with tab1:
    st.header("I. Introduction")
    
    col1, col2 = st.columns([2, 3])
    with col1:
        st.image("static/suit.jpg", 
                 caption="Born in Jasaan, Misamis Oriental", 
                 use_container_width=True) # <-- Corrected parameter
    
    with col2:
        st.markdown("""
        **Moen Malone I. Rago** is a Computer Science student born on March 1, 2004, in Aplaya, Jasaan, Misamis Oriental. 
        He is adventurous, athletic, and deeply curious about how things work. From a young age, he has shown a passion 
        for exploring, learning, and creating. Whether it’s through sports or coding, Moen thrives on challenges 
        that push his limits.
        """)
        
        # --- Using st.info for Quotes ---
        st.info(
            """
            > "You have the power over your mind—not outside events. Realize this and you will have strength."
            >
            > — **Marcus Aurelius**
            """
        )
        
        st.markdown("""
        He believes that self-control and determination are keys to achieving success, learning early on that 
        he must work hard for what he wants rather than relying on others.
        """)

# --- Tab 2: Early Life & Family ---
with tab2:
    st.header("II. Early Life and Family Background")
    
    st.markdown("""
    Moen grew up in the coastal barangay of Aplaya, Jasaan, Misamis Oriental. His childhood was filled with 
    laughter, games, and adventures shared with neighborhood friends. When technology began to emerge, his 
    fascination with computers was sparked. Initially, it was video games like Dota and Counter-Strike 
    that caught his attention, but soon he became curious about how computers functioned.
    """)
    
    # --- Using st.expander for details ---
    with st.expander("Childhood Projects & Hobbies"):
        st.markdown("""
        With a creative mind, he would repurpose used batteries, broken toys, and Styrofoam into small 
        projects like toy boats that raced on the village canals. This early resourcefulness and inventiveness 
        would become the foundation of his problem-solving mindset.
        """)
        st.image("static/boat.png", 
                 caption="Childhood was filled with adventure and creativity.")

    st.markdown("""
    Raised in a family that valued hard work and perseverance, Moen learned to make the best out of limited 
    resources. His parents taught him the importance of self-discipline, humility, and gratitude, lessons 
    that shaped his sense of purpose and work ethic.
    """)
    
    # --- Using st.multiselect ---
    st.multiselect(
        "Key values learned:",
        ["Hard Work", "Perseverance", "Self-Discipline", "Humility", "Gratitude"],
        default=["Hard Work", "Perseverance", "Self-Discipline"]
    )

# --- Tab 3: Education ---
with tab3:
    st.header("III. Education and School Life")
    st.markdown("Moen started his educational journey at Aplaya Elementary School...")
    
    # --- Using st.progress for a visual timeline ---
    st.subheader("Educational Timeline")
    st.progress(100, text="Aplaya Elementary School (Completed)")
    st.progress(100, text="Jaclupan National High School (Completed)")
    st.progress(100, text="University of San Jose - Recoletos (SHS)")
    
    # --- Using st.success to highlight achievements ---
    st.success("Achievement: St. Augustine Academic Excellence Award (SHS)")
    
    st.progress(75, text="Cebu Institute of Technology - University (In Progress)")
    
    st.markdown("""
    He is now pursuing a degree in Computer Science at CIT-U. College has been both exciting and challenging. 
    Through rigorous courses, he has honed his analytical thinking and programming skills.
    """)

# --- Tab 4: College / Present Life ---
with tab4:
    st.header("IV. College / Present Life")
    st.markdown("""
    Moen chose Computer Science because it allows him to combine logic, creativity, and innovation. 
    He enjoys solving real-world problems through software and has worked on small projects.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # --- Using st.json to display structured data ---
        st.subheader("Key Courses")
        st.json({
            "Core": ["Algorithms", "Data Structures", "Discrete Structures"],
            "Projects": ["Binary Tree Visualizers", "Algorithm Simulations"]
        })
        
        # --- Using st.metric ---
        st.metric(label="Current Status", value="Actively Learning", delta="Growth")
        
    with col2:
        # --- Using st.code ---
        st.subheader("Sample Project Concept (Python)")
        st.code("""
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Example: Binary Tree Visualizer
# This project helped solidify data structure concepts.
def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root
        """, language="python")

# --- Tab 5: Hobbies, Passions, and Interests ---
with tab5:
    st.header("V. Hobbies, Passions, and Interests")
    st.markdown("Moen’s interests extend beyond coding. He is passionate about a balance of activities.")

    # --- Using st.columns for a gallery ---
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("static/book.jpg", 
                 caption="Reading (Mystery, Self-Improvement)", 
                 use_container_width=True) # <-- Corrected parameter
    with col2:
        st.image("static/gym.jpg", 
                 caption="Fitness (Gym, Running, Sports)", 
                 use_container_width=True) # <-- Corrected parameter
    with col3:
        st.image("static/desk.jpg", 
                 caption="Coding (Prototypes, New Languages)", 
                 use_container_width=True) # <-- Corrected parameter

    # --- Using st.radio ---
    st.radio(
        "Which hobby resonates most with you?",
        ["Reading", "Fitness", "Coding"],
        horizontal=True,
        index=2
    )

# --- Tab 6: Challenges and Turning Points ---
with tab6:
    st.header("VI. Challenges and Turning Points")
    st.markdown("Life hasn’t always been easy for Moen. Growing up with limited resources, he often had to make do.")
    
    # --- Using st.warning/st.success for contrast ---
    st.warning("**Challenge:** Limited resources and moments of self-doubt.")
    
    st.success("**Turning Point:** Receiving the Academic Excellence Award in senior high school.")
    
    st.markdown("Another defining moment was completing his first major coding project—a challenge that solidified his dream.")
    
    # --- Using st.spinner as a visual gag ---
    with st.spinner('Reflecting on past challenges...'):
        time.sleep(2)  # Simulate a pause for reflection
    st.write("Reflection complete: Every challenge was a lesson.")


# --- Tab 7: Inspirations and Life Lessons ---
with tab7:
    st.header("VII. Inspirations and Life Lessons")
    st.markdown("""
    Moen’s inspiration comes from great thinkers, scientists, and engineers. Philosophically, 
    he is guided by Stoicism.
    """)
    
    st.info("He believes that consistent effort is more important than occasional bursts of brilliance.")
    
    # --- Using st.table ---
    st.subheader("Core Life Lessons")
    df = pd.DataFrame({
        'Lesson': ['Discipline', 'Gratitude', 'Perseverance', 'Humility'],
        'Source': ['Family & Stoicism', 'Family', 'Self-Motivation', 'Life Experience']
    })
    st.table(df)

# --- Tab 8: Dreams, Goals, and Aspirations ---
with tab8:
    st.header("VIII. Dreams, Goals, and Aspirations")
    
    st.subheader("Ultimate Dream: Software Engineer at Apple")
    st.image("static/apple.jpg", 
             caption="Aspiring to work on innovative, user-centered products.")
    
    col1, col2 = st.columns(2)
    with col1:
        # --- Using st.expander for lists ---
        with st.expander("**Short-Term Goals**", expanded=True):
            st.markdown("""
            * Strengthen portfolio
            * Master system-level programming
            * Explore artificial intelligence
            """)
    with col2:
        with st.expander("**Long-Term Goals**", expanded=True):
            st.markdown("""
            * Become a Software Engineer at Apple
            * Mentor others and help them reach their potential
            """)
            
    # --- Using st.balloons on button click ---
    if st.button("Celebrate These Goals!"):
        st.balloons()
        
    # --- Using st.color_picker ---
    st.color_picker("Pick a color to represent this future", "#1E90FF")

# --- Tab 9: Conclusion ---
with tab9:
    st.header("IX. Conclusion")
    st.markdown("""
    From a young boy building toy boats out of discarded materials to a college student coding programs 
    that bring ideas to life, Moen’s journey is defined by curiosity, perseverance, and purpose. 
    
    His story reminds readers that every challenge can become a stepping stone to greatness. 
    As he looks toward the future, Moen remains committed to learning, creating, and inspiring others.
    """)
    
    st.divider()
    
    # --- Using st.write for a final message ---
    st.write("Thank you for reading.")
    
    # --- Final flourish ---
    st.snow()
    st.caption("With determination as his compass and curiosity as his fuel, he continues to shape his path.")