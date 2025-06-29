import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# ========== CONFIG ==========

guest_table_map = {
    "-" : 0,
    ####################################
    "Aldrin Lee": 1,
    "Audrey Chan": 1,
    "Sheryl (Bride)": 1,
    "Andrew (Groom)": 1,
    "Angie Chan": 1,
    "Peter Chan": 1,
    "Rose Chua": 1,
    "Terry Koh": 1,
    "Andrea Lee": 1,
    "Theodore Koh": 1,
    ####################################
    "Simon Ang": 2,
    "Josephine Teng": 2,
    "Doreen Tan": 2,
    "Sheryl's Gong Gong": 2,
    "Jeffery Tin": 2,
    "Catherine Chan": 2,
    "Jeremy Tin": 2,
    "Christine Tang": 2,
    "Mark Tin": 2,
    "Elaine Chua": 2,
    ####################################
    "Elvin Lee": 3,
    "Katherine Heng": 3,
    "Natalie Lee": 3,
    "Nicole Lee": 3,
    "Nellie Lee": 3,
    "Megan Lee": 3,
    "Alwin Lee": 3,
    "Mavis Chan": 3,
    "Serene Lee": 3,
    ####################################
    "Casey Chan": 5,
    "Sandra Chan": 5,
    "Marc Chan": 5,
    "Cheyenne": 5,
    "Mae Chan": 5,
    "Ah Moh": 5,
    "Colin Chan": 5,
    "Luan hua": 5,
    "Collette Chan": 5,
    ####################################
    "Palvin Chan": 6,
    "Melynda Cheng": 6,
    "Oliver Chan": 6,
    "Miles Chan": 6,
    "Tom Cheng": 6,
    "Arlene Cheng": 6,
    "Stephanie Teo": 6,
    "Peter Teo": 6,
    "Tua Kng": 6,
    "Mrs Han": 6,
    ####################################
    "Nelson Koh": 7,
    "Terry’s mom": 7,
    "AD Chan": 7,
    "Carol": 7,
    "Ali Al Kuwari": 7,
    "Marlian GW": 7,
    "Matthew Lee": 7,
    "Nicholas Lee": 7,
    ####################################
    "Mr Teh": 8,
    "Mrs Teh": 8,
    "Peijing": 8,
    "Chee Huey": 8,
    "Liming": 8,
    "Nell": 8,
    "Liming Daughter 1": 8,
    "Liming Daughter 2": 8,
    "Diana": 8,
    "Diana Husband": 8,
    ####################################
    "Will Woon": 10,
    "Luna Xiong": 10,
    "Nicole Tan": 10,
    "Markus Yuen": 10,
    "Chermane Goh": 10,
    "Fonzarelli Ong": 10,
    "Joyce Skidell": 10,
    "Min Siang Loy": 10,
    "Jin Hong Ng": 10,
    "Jit Yong Ang": 10,
    ####################################
    "Cassandra Hesler": 9,
    "Bradley Goh": 9,
    "Jin Wei Krishnan": 9,
    "Tim Young": 9,
    "Charmian Koh": 9,
    "Benjamin Ang": 9,
    "Yue Ern Lee": 9,
    "Abhishek Choudhary": 9,
    "Wayne Toh": 9,
    "Jonathan Raharja": 9,
    ####################################
    "Nicholas mum": 11,
    "Nicholas dad": 11,
    "Naresh Vashdev": 11,
    "Deena Loo": 11,
    "Eric Lee": 11,
    "Val Lee": 11,
    "Kenneth Chew": 11,
    "Nicholas Phang": 11,
    "Jarell Ang": 11,
    ####################################
    "Travis Tseng": 12,
    "Christine Teo": 12,
    "Andrea Chong": 12,
    "Lim Main Ray": 12,
    "Ambrose Yew": 12,
    "Vian See": 12,
    "Makarios Tang": 12,
    "Wei Lun Gan": 12,
    "Marcus Guo": 12,
    "Janessa Yim": 12,
    "Alyssa Siow": 12,
    "Lettitia Quek": 12,
    "Edna Chah": 12,
    ####################################
    "Low Xin Yi": 15,
    "Kelly Thng": 15,
    "Claudia Lee": 15,
    "Rachel Ng": 15,
    "Trevor (Rachel)": 15,
    "Kai Qing": 15,
    "Shawn": 15,
    "Whitney David": 15,
    "Laurence Sukarti": 15,
    "Matthew Chia": 15,
    "Melanie Koh": 15,
    "Maryam Mohammed": 15,
    "Lay Shuen Kwek": 15,
    ####################################
    "Trisa Tin": 16,
    "Rikki Sim": 16,
    "Brandon Sim": 16,
    "Glenn Ang": 16,
    "Julia Sim": 16,
    "Jamie Ang": 16,
    "Ryan Ang": 16,
    "Marcus Tin": 16,
    "Ivan Tin": 16,
    "Charlene (Brandon)": 16,
    "Jan Sim": 16,
    "Nesh (Jan)": 16,
    "Faith Lee": 16,
    "Daryl Ang": 16,
    ####################################
    "Angela Shenead": 17,
    "Cheryl Cheong": 17,
    "Tania Tan": 17,
    "Kelly Ha": 17,
    "Vanessa Ghui": 17,
    "Vera Lim": 17,
    "Izzah": 17,
    "Diane Tan": 17,
    "Jeneen Foo": 17,
    "Zen Sze": 17,
    "Anzelle Lee": 17,
    "Victor Tan Zuu Yuaan": 17,
    "Justin Google Maps Foo": 17,
    ####################################
    "Willie Quek": 18,
    "Fiona Quek": 18,
    "Shirley Quek": 18,
    "Quek Wei Guang": 18,
    "Quek Yeng Ling": 18,
    "Ellie Quek": 18,
    "Evan Quek": 18,
    "Jonathan Tin": 18,
    "Justin Tin": 18,
    "Johanson Tin": 18,
    ####################################
    "3rd Uncle (Simon's side)": 19,
    "3rd Uncle's Wife (Simon's side)": 19,
    "4th Uncle (Simon)": 19,
    "Elsie Tan": 19,
    "Cindy Soon": 19,
    "Francis Soon": 19,
    "William Tan": 19,
    "Michelle Tan": 19,
    ####################################
    "Maryam (Sheryl)": 20,
    "Wati (Sheryl)": 20,
    "Annie Leung": 20,
    "Nelson Leung": 20,
    "Yee Joo Poo": 20,
    "Karen Soh": 20,
    "4th Uncle (Josephine)": 20,
    "4th Uncle's Wife (Josephine)": 20,
    "3rd Uncle (Josephine)": 20,
    "3rd Uncle's Wife (Josephine)": 20,
    ####################################
    "James Tan": 21,
    "Sharon Tan": 21,
    "Daniel Kwan": 21,
    "Joe Leng": 21,
    "Shirley Leng": 21,
    "Zach Chua": 21,
    "Sherrie Chua": 21,
    "Karen Tan": 21,
    "Kenneth Tan": 21,
    ####################################
    "Lorraine Tay": 22,
    "Peter Tay": 22,
    "Willie Liam": 22,
    "Jye Chong": 22,
    "Johnson Soh": 22,
    "Linus Terh": 22,
    "Lawrence Chan": 22,
    "Mr Adrian Tee": 22,
    "Mrs Adrian Tee": 22,
    ####################################
    "John Ow": 23,
    "Aloysius Yang": 23,
    "Yelun Yang": 23,
    "Wen Xu Goh": 23,
    "Stephen Cao": 23,
    "Hafiz Alsree": 23,
    "Paul Li": 23,
    "Cassius Kua": 23,
    "Quinn Wong": 23,
    "Ethan Sun": 23,
    ####################################
    "Sean Neighbour": 25,
    "Sean Wife": 25,
    "Opposite Neighbour": 25,
    "Opposite Neighbour Wife": 25,
    "Edgar Tan": 25,
    "Margaret Tan": 25,
    "Molly Goh": 25,
    "Roland Goh": 25,
    "Table 1": 1,
    "Table 2": 2,
    "Table 3": 3,
    "Table 5": 5,
    "Table 6": 6,
    "Table 7": 7,
    "Table 8": 8,
    "Table 9": 9,
    "Table 10": 10,
    "Table 11": 11,
    "Table 15": 15,
    "Table 16": 16,
    "Table 17": 17,
    "Table 18": 18,
    "Table 19": 19,
    "Table 20": 20,
    "Table 21": 21,
    "Table 22": 22,
    "Table 23": 23,
    "Table 25": 25,
    "Table 12A": "12a",
    "Table 12B": "12b",
    "Table 15A": "15a",
    "Table 15B": "15b",
    "Table 16A": "16a",
    "Table 16B": "16b",
    "Table 17A": "17a",
    "Table 17B": "17b",

}

table_positions = {
    2: (132, 551),
    20: (455, 403),
    18: (228, 403),
    19: (338, 225),
    21: (565, 225),
    23: (791, 225),
    11: (1019, 1240),
    22: (681, 403),
    25: (910, 403),
    1: (132, 916),
    5: (338, 1240),
    7: (564, 1240),
    9: (791, 1240),
    6: (455, 1062),
    3: (229, 1062),
    8: (682, 1062),
    10: (911, 1062),
}
rectangle_positions ={
    "16a": (410, 569-34/2),
    "17a": (680, 569-34/2),
    "12a": (410, 901-34/2),
    "15a": (680, 901-34/2),
    "16b": (410, 569+32/2),
    "17b": (680, 569+32/2),
    "12b": (410, 901+32/2),
    "15b": (680, 901+32/2),
}

#bg_image = Image.open("Floorplan8.png").convert("RGBA")  
@st.cache_resource
def load_bg_image():
    return Image.open("Floorplan9.png").convert("RGBA")

bg_image = load_bg_image()
# ========== UI ==========
st.title("Andrew and Sheryl 🥂✨🍾")
selected_guest = st.selectbox("Enter your name to find your seat!", [name for name in guest_table_map])

# ========== IMAGE DRAWING ==========
if selected_guest:
    with st.spinner("Checking..."):
        selected_table = guest_table_map[selected_guest]
        
        st.write(f"**Your table is now highlighted in yellow**")
        st.write(f"{selected_guest} is seated at **[Table {selected_table}]** with:")
        #print out all the guests at the selected table
        guests_at_table = [name for name, table in guest_table_map.items() if table == selected_table]
        st.write(" || ".join(guests_at_table))
        
        # Draw over a copy of the image
        img = bg_image.copy()
        draw = ImageDraw.Draw(img)

        # Draw all tables
        for table_num, (x, y) in table_positions.items():
            radius = 55
            fill = "yellow" if table_num == selected_table else None
            draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=fill, outline="red")

        # Draw rectangles for rectangle positions
        for table_num, (x, y) in rectangle_positions.items():
            width, height = 270, 32.5
            fill = "yellow" if table_num == selected_table else None
            draw.rectangle((x - width // 2, y - height // 2, x + width // 2, y + height // 2), fill=fill, outline="red")

        st.image(img)
else:
    st.image(bg_image)
