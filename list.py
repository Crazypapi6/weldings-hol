#import streamlit as st
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
from pathlib import Path

# Specify the directory path containing image files
image_directory = "products/promotion_products"

# Create a generator of Path objects for all .jpg files
image_paths = Path(image_directory).glob("*.jpg")

# Convert Path objects to strings
image_strings = [str(p) for p in image_paths]

# Print the list of image file paths
print("List of image file paths:")
for path in image_strings:
    print(path)


#import streamlit as st

prompt= {}
messages = st.container(height=300)
if prompt := st.chat_input("Say something"):
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(f"Echo: {prompt}")
