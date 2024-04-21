import streamlit as st 
from streamlit_option_menu import option_menu
import sqlite3
import pandas as pd

def Manager() -> None:
    st.sidebar.header("Shopping 24..")
    st.header(':gray[Manage Shop]', divider='rainbow')
    st.write(':rainbow[This Section Manages products and product sales]')
    st.toast('Manager')

    def add_product(name, price, id):
        try:
        # Connect to the database
            conn = sqlite3.connect('db/products.db')
        # Create a cursor object
            c = conn.cursor()
        # Insert a new row into the posts table
            c.execute('INSERT INTO products (name, price, id) VALUES (?,?,?)', (name, price, id))
        # Save the changes to the database
            conn.commit()
        # Close the connection and the cursor
            conn.close()
        except sqlite3.Error as e:
        # Print the error message
            print(e)
            
    def get_all_products():
        try:
        # Connect to the database
            conn = sqlite3.connect('db/products.db')
        # Create a cursor object
            c = conn.cursor()
        # Select all the rows from the posts table
            c.execute('SELECT * FROM products')
        # Fetch all the results
            data = c.fetchall()
        # Close the connection and the cursor
            conn.close()
        # Return the data
            return data
        except sqlite3.Error as e:
        # Print the error message
            print(e)    

    def get_products_by_name(name):
        try:
        # Connect to the database
            conn = sqlite3.connect('db/products.db')
        # Create a cursor object
            c = conn.cursor()
        # Select the row from the posts table that matches the title
            c.execute('SELECT * FROM products WHERE name=?', (name,))
        # Fetch the result
            data = c.fetchone()
        # Close the connection and the cursor
            conn.close()
        # Return the data
            return data
        except sqlite3.Error as e:
        # Print the error message
            print(e)

    def delete_product(name):
        try:
        # Connect to the database
            conn = sqlite3.connect('db/products.db')
        # Create a cursor object
            c = conn.cursor()
        # Delete the row from the posts table that matches the title
            c.execute('DELETE FROM products WHERE name=?', (name,))
        # Save the changes to the database
            conn.commit()
        # Close the connection and the cursor
            conn.close()
        except sqlite3.Error as e:
        # Print the error message
            print(e)

    add_product("Nike T.shirts",500, 500)
    add_product("Lakers fan kit",100,100)
    add_product("Saint-Inc Merch",300,300)
    print(get_all_products())
    print(get_products_by_name('Saint-Inc Merch'))
    delete_product('Lakers fan kit')
    print(get_all_products())

    name_temp = """
<div style="background-color:aliceblue;padding:10px;border-radius:10px;margin:10px;">
<h4 style="color:gray;text-align:center;">{}</h4>
<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;">
<h6>Name: {}</h6>
<br/>
<br/>
<p style="text-align:justify"> {}</p>
</div>
"""
    
    product_temp = """
<div style="background-color:aliceblue;padding:10px;border-radius:5px;margin:10px;">
<h4 style="color:gray;text-align:center;">{}</h4>
<h6>Name: {}</h6>
<h6>Price: {}</h6>
<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;width: 50px;height: 50px;border-radius: 50%;">
<br/>
<br/>
<p style="text-align:justify"> {}</p>
</div>
"""
    
    
    choice = option_menu(
                menu_title="Shopping 24 Manager's office",
                options=("Home", "View Products", "Add Products", "Search", "Manage"),
                menu_icon="shop",
                icons=("house","eye", "plus", "search", "box"),
                orientation = "horizontal",
                default_index=0,
                styles={
                    "container": {"padding": "initial","background-color": 'antiquewhite', "boarder-color": 'aliceblue'},
                    "icon": {"color":"gray","font-size": "15px"},
                    "nav-link": {"color":"gray","font-size": "12px", "text-align": "initial", "margin":"10px"},
                    "nav-link-selected": {"background-color": "white"},
                    }
                    )         
    if choice == "Home":
        st.title(":gray[Welcome to Shopping 24 admin]")
        st.divider()
        st.info("You can View, Add, Search, Manage products using the Nav Bar", icon = "🏠")
        col1, col2, col3 = st.columns(3)
        with col1:
            with st.container(border=True):
                st.image("https://static.streamlit.io/examples/cat.jpg", caption="Hello")

        with col2:
            with st.container(border=True):
                st.image("https://static.streamlit.io/examples/cat.jpg", caption="Hello")

        with col3:
            with st.container(border=True):
                st.image("https://static.streamlit.io/examples/cat.jpg", caption="Hello")

    elif choice == "View Products":
        st.divider()
        st.info("Here you can see all the available products in the shop.", icon="👔")
    # Get all the posts from the database
        products = get_all_products()
    # Display each post as a card
        for product in products:
            st.markdown(name_temp.format(product[1], product[0], product[2]), unsafe_allow_html=True)
        # Add a button to view the full post
        if st.button("Read More"):
            st.markdown(product_temp.format(product[1], product[0], product[3], product[2]), unsafe_allow_html=True)
    elif choice == "Add Products":
        st.divider()
        st.info("Here you can add a new product to the database.", icon="📭")
    # Create a form to get the post details
        with st.form(key="add_form"):
            name = st.text_input("Product Name")
            price = st.text_input("Price")
            id = st.text_area("Product ID")
            submit = st.form_submit_button("Add Product")
    # If the form is submitted, add the post to the database
            if submit:
                add_product(name, price, id)
                st.success("Product added successfully")
    elif choice == "Search":
        st.title(":gray[Search for remaining and available products]")
        st.info("Here you can search for a product by name and id.", icon= "🔍")
    # Create a text input to get the search query
        query = st.text_input("Search Products")
    # If the query is not empty, search for the matching posts
        if query:
        # Get all the posts from the database
            products = get_all_products()
        # Filter the posts by the query
            results = [product for product in products if query.lower() in product[0].lower() or query.lower() in product[1].lower()]
        # Display the results
            if results:
                st.write(f"Found {len(results)} matching posts:")
                for result in results:
                    st.markdown(name_temp.format(result[1], result[0], result[2][:50] + "..."), unsafe_allow_html=True)
                # Add a button to view the full post
                    if st.button("Read More", key=result[1]):
                        st.markdown(product_temp.format(result[1], result[0], result[3], result[2]), unsafe_allow_html=True)
                    else:
                        st.write("No matching posts found")
    elif choice == "Manage":
        st.info("Here you can delete products or view some statistics.", icon="📑")
    # Create a selectbox to choose a post to delete
        names = [product[1] for product in get_all_products()]
        name = st.selectbox("Select a product to delete", names)
    # Add a button to confirm the deletion
        if st.button("Delete"):
            delete_product(name)
            st.success("Post deleted successfully")
    # Create a checkbox to show some statistics
        if st.checkbox("Show statistics"):
        # Get all the posts from the database
            products = get_all_products()
        # Convert the posts to a dataframe
            df = pd.DataFrame(products, columns=["Name", "Price", "ID"])
        # Display some basic statistics
            with st.container(border=True):
                st.write("**Number of products:**", len(products))
                st.write("**Most Expensive Product:**", df["Price"].max())
                st.write("**Least Expensive Product:**", df["Price"].min())
        # Display a bar chart of posts by author
            st.write("**Products:**")
            name_count = df["Name"].value_counts()
            st.bar_chart(name_count)

Manager()