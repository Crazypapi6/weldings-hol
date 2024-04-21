import streamlit as st

import numpy as np
import pandas as pd
import time

from streamlit.logger import get_logger
from streamlit_extras.colored_header import colored_header
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.streaming_write import write
from streamlit_extras.mention import mention
from streamlit_extras.app_logo import add_logo
from streamlit_extras.badges import badge

LOGGER = get_logger(__name__)

#from modules import login

def run():
    st.set_page_config(page_title="Shopping 24.",page_icon=None, layout= "centered")
    #add_logo(logo_url="images\components\cow.jpg", height=50)
    colored_header(
             label="Shopping 24.",
             description="Browse through our shop to view products and place orders",
             color_name="gray-70"
             )
    st.sidebar.header(":gray[Shopping 24..]")
    st.toast(':gray[Welding Hol.]', icon="🛠️")

    tab1, tab2, tab3 = st.tabs([":gray[**Home**]", ":gray[**Requests and Promos**]", ":gray[**Contact Us**]"])
    with tab1:
        st.title(
            ":gray[**Home**]",
            help=("This is our home page, Enjoy")
        )
        cola, cola2 = st.columns(2)
        with cola:
            with st.container(border=True, height=300):
                 video_file = open('videos/video1.mp4', 'rb')
                 video_bytes = video_file.read()
                 st.video(video_bytes)
                 st.write("- _Welcome to our online shop_")
            with cola2:
                with st.container(border=True, height=300):
                    video_file = open('videos/video1.mp4', 'rb')
                    video_bytes = video_file.read()
                    st.video(video_bytes)
                    st.write("- _Thank you for visiting us_")   
        st.markdown(
                    """
                    :gray[**This online shop is desgined to advertise our products to you, our valued customers**]
                    """
                )
        st.link_button('Contact Me', 
                            url= "wa.me/+263782012633",
                            help="Contact me on whatsapp",
                             use_container_width=True)      
        st.divider()

        # start of the products page
        st.write(":gray[**This is our most latest produce**]")
        image_column,text_column = st.columns(2)
        with image_column:
            container = st.container(border=True,height=250)
            container.image("products/item7.jpg")
        with text_column:
            with st.container():
                st.subheader(':gray[Yeezy Slides 20''s'' @ $60]', help="Deliveries will be made within 72 hours for free")
                st.info("There are only 4 left")
                st.divider()
                with st.container(border=True):
                    st.markdown("""
                            :gray[*Kanye West Release*]
                            :green[*Long Lasting*]
                            :blue[*Comfortable*]
                            """)   
        st.write(
            ":gray[**Top products**]"
        )
        col1 , col2 , col3 = st.columns(3)
        with col1:
             container = st.container(border=True,
                                      height=250)
             container.image("products/item1.jpg")
             st.link_button('Order', 
                            url= "https://www.instagram.com/reel/C1M",
                            help="View product specs and purchase page",
                             use_container_width=True)
             st.markdown("""
                        :green[Palm Angels T.shirts] 
                         """)
        with col2:
            container = st.container(border=True,height=250)
            container.image("products/item2.jpg")
            st.link_button('Order', 
                            url= "https://www.instagram.com/reel/C1M",
                            help="View product specs and purchase page",
                             use_container_width=True)
            st.markdown("""
                        :green[Yeezy 350 splys] 
                         """)

        with col3:
            container = st.container(border=True,height=250)
            container.image("products/item19.jpg")
            st.link_button('Order', 
                            url= "https://www.instagram.com/reel/C1M",
                            help="View product specs and purchase page",
                             use_container_width=True)
            st.markdown("""
                        :green[Nike Female Gym set piece] 
                         """)
        
        st.divider() 
        col4, col5, col6 = st.columns(3)  
        
        with col4:
            container = st.container(border=True,height=250)
            container.image("products/item12.jpg")
            st.link_button('Order', 
                            url= "https://www.instagram.com/reel/C1M",
                            help="View product specs and purchase page",
                             use_container_width=True)
            st.markdown("""
                        :green[All converse shoes] 
                         """)
            
        with col5:
            container = st.container(border=True,height=250)
            container.image("products/item16.jpg")
            st.link_button('Order', 
                            url= "https://www.instagram.com/reel/C1M",
                            help="View product specs and purchase page",
                             use_container_width=True)
            st.markdown("""
                        :green[Designer T.Shirts] 
                         """)
            
        with col6:
            container = st.container(border=True,height=250)
            container.image("products/item17.jpg")
            st.link_button('Order', 
                            url= "https://www.instagram.com/reel/C1M",
                            help="View product specs and purchase page",
                             use_container_width=True)
            st.markdown("""
                        :green[Nike female casual set piece] 
                         """)
            
        st.divider()

        long_text = "Lorem ipsum. " * 1000
        with st.container(border=False):
            st.subheader(":blue[Promotion Products]")
            st.image(
              image="products/hoddie.jpg",
              caption="Products are cut off by 25%"
            )
            st.link_button('View More', 
                            url= "wa.me/",
                            help="View product specs and purchase page",
                             use_container_width=True)
    with tab2:
        st.header(
            ":gray[**Requests**]"
        )
        with st.form(clear_on_submit = True, key="add_form"):
            txt = st.text_area(
                 "Post Your Requests Here",
                 max_chars=500, 
                 placeholder="Type a message"
                 )
            date = st.date_input("Date")
            submit = st.form_submit_button("Request")

            if submit:
                st.write("- :gray[**You requested**]",txt, "- :gray[**Date**]", date)
                st.success("Your request has been recieved, Continue browsing", icon="👏")

        st.divider()
        st.subheader(":gray[**Weekly Promos**]")

        company_name = "The Mbizz"
        company_status = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco
laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat
non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
        _message = """
:rainbow[This section covers surrounding products in our workspace by other producers and retailers we hope you find them helpful. This week we are promoting Mbizo gas company]
"""
        st.write(_message)
        
        col1, col2, col3 = st.columns(3)

        col1.metric(label="ZAR(Rand)", value=36, delta=1.33)
        col2.metric(label="USD(US Dollar)", value=1.80, delta=1.33)
        col3.metric(label="Market(Init P)", value=1.65, delta=-1.12)
        style_metric_cards()

        st.divider()
        st.subheader(f":gray[**Preview {company_name}**]")
        def preview():
            for word in company_status.split():
                yield word + " "
                time.sleep(0.05)

            yield pd.DataFrame(
            np.random.randn(5, 10),
            columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
        )
                
        if st.button("Preview"):
            write(preview)
    
        cul1 , cul2 = st.columns(2)
        with cul1:
            st.link_button('Request a Promo', 
                            url= "https://www.instagram.com/reel/C1M",
                            help="Request a promotion from the admin",
                             use_container_width=True)
        
        with cul2:
            st.link_button(f'{company_name}', 
                            url= "https://www.instagram.com/reel/C1M",
                            help="Contact our current promo",
                             use_container_width=True)
    with tab3:
        colored_header(
            label = "Contact Us",
            description = "Get in touch with me",
            color_name = "gray-70")
        
        contact = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width", initial-scale="1.0">
    <title></title>
</head>
<body>
    <div class="contact-container">
        <form action="" method="post">
            <input type="hidden" name="" value="false">
            <input type="text" name="Username" placeholder="Username" required>
            <input type="email" name="email" placeholder="Email" required>
            <textarea name="message" id="4890" cols="30" rows="5" placeholder="Type your message"></textarea>
            <button type="submit">Submit</button>
        </form>
    </div>
</body>
</html>
"""
        colam1, colam2 = st.columns(2)
        with colam1:
            with st.container(border=True):
                st.markdown(contact, unsafe_allow_html=True)

        with colam2:
            st.markdown(
                """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <title></title>
    <style>
        body{
            font-family: 'Times New Roman', Times, serif;
        }
        product{
        width: 200px;
        height: 200px;
    }
        grid{
            display:grid;
            grid-template-columns: 200px 200px 200px;
            grid-template-rows: 200px 200px 200px;
            grid-gap: 20px 20px 20px;
            padding: 5px;
            border: 1px black;
            border-radius: 20px;
    }
    </style>
</head>
<body>
    <div class='grid'>
        <div class='product'>
            <img src="images/local.jpg" alt = "Weldings hol.">
            <img src="images/local2.jpg" alt="Talk to us">
    </div>
</body>
</html>
""",
unsafe_allow_html=True
            )
        
        def css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        css("templates/style.css")
        st.divider()
        st.subheader("**Follow me on the socials**")

        badge(type="github", name = "Crazypapi6" ,url="https://github.com/Crazypapi6")
        with st.container(border=True):
             st.markdown("- Read And Get Access To Our Licence And Documentation")

        badge(type="twitter", name="crazyPapi_6")
        with st.container(border=True):
             st.markdown("- Visit our twitter feed for more")

        mention(
    label="Pintrest",
    icon="📌",  # You can also just use an emoji
    url="https://pin.it/407ECh",
)
        with st.container(border=True):
             st.markdown("Visit my pintrest page")

        with st.container(border=True):
             st.markdown("""
<a href="https://www.buymeacoffee.com/supremecro7"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=supremecro7&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff" /></a>
                     """,
                     unsafe_allow_html=True)
             st.info("Support Us",
                     icon="🍵")
   
        with st.sidebar:
            with st.form("my_form", clear_on_submit=True):
                st.write("**Rate This Service**")
                slider_val = st.slider("How do you rate this app", help = "Slide to the desired percentage")
                checkbox_val = st.checkbox("Do you find this app helpful", help = "Check the box if True")
                submitted = st.form_submit_button("Rate")
                if submitted:
                    st.write("Rating", slider_val, "Helpful", checkbox_val)

if __name__ == "__main__":
    run()