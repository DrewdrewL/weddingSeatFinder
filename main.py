import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# ========== CONFIG ==========

guest_table_map = {
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
    "Cheyenne Chan": 5,
    "Mae Chan": 5,
    "Mdm Koh": 5,
    "Colin Chan": 5,
    "Luan Hua Chan": 5,
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
    ####################################
    "Nelson Koh": 7,
    "Noven Koh": 7,
    "AD Chan": 7,
    "Carol Eguaras": 7,
    "Ali Al Kuwari": 7,
    "Marlian GW": 7,
    "Matthew Lee": 7,
    "Nicholas Lee": 7,
    "Han Mian Hwee": 7,
    "Lee Choo": 7,
    ####################################
    "Mr Teh": 8,
    "Mrs Teh": 8,
    "Teh Peijing": 8,
    "Teh Chee Huey": 8,
    "Teh Liming": 8,
    "Nell": 8,
    "Liming Daughter 1": 8,
    "Liming Daughter 2": 8,
    "Diana Pang": 8,
    "Steven Pang": 8,
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
    "Cassandra Hesler": 11,
    "Bradley Goh": 11,
    "Jin Wei Krishnan": 11,
    "Tim Young": 11,
    "Charmian Koh": 11,
    "Benjamin Ang": 11,
    "Yue Ern Lee": 11,
    "Abhishek Choudhary": 11,
    "Wayne Toh": 11,
    "Jonathan Raharja": 11,
    ####################################
    "Nicholas mum": 9,
    "Nicholas dad": 9,
    "Naresh Vashdev": 9,
    "Deena Loo": 9,
    "Eric Lee": 9,
    "Val Lee": 9,
    "Kenneth Chew": 9,
    "Nicholas Phang": 9,
    "Jarell Ang": 9,
    ####################################
    "Travis Tseng": "12B",
    "Christine Teo": "12B",
    "Andrea Chong": "12A",
    "Lim Main Ray": "12B",
    "Ambrose Yew": "12A",
    "Vian See": "12A",
    "Makarios Tang": "12B",
    "Wei Lun Gan": "12A",
    "Marcus Guo": "12A",
    "Janessa Yim": "12B",
    "Alyssa Siow": "12B",
    "Lettitia Quek": "12A",
    "Edna Chah": "12B",
    "Low Xin Yi": "12B",
    ####################################
    "Kelly Thng": "15A",
    "Claudia Lee": "15B",
    "Rachel Ng": "15B",
    "Trevor (Rachel)": "15B",
    "Kai Qing": "15A",
    "Shawn": "15A",
    "Whitney David": "15A",
    "Laurence Sukarti": "15A",
    "Matthew Chia": "15A",
    "Melanie Koh": "15B",
    "Maryam Mohammed": "15B",
    "Lay Shuen Kwek": "15B",
    ####################################
    "Trisa Tin": "16A",
    "Rikki Sim": "16A",
    "Brandon Sim": "16A",
    "Glenn Ang": "16A",
    "Julia Sim": "16A",
    "Jamie Ang": "16B",
    "Ryan Ang": "16B",
    "Marcus Tin": "16B",
    "Ivan Tin": "16B",
    "Charlene (Brandon)": "16A",
    "Jan Sim": "16B",
    "Nesh (Jan)": "16B",
    "Faith Lee": "16A",
    "Daryl Ang": "16A",
    ####################################
    "Angela Shenead": "17A",
    "Cheryl Cheong": "17B",
    "Tania Tan": "17A",
    "Kelly Ha": "17A",
    "Vanessa Ghui": "17A",
    "Vera Lim": "17A",
    "Izzah": "17A",
    "Diane Tan": "17A",
    "Jeneen Foo": "17B",
    "Zen Sze": "17B",
    "Anzelle Lee": "17B",
    "Tan Zuu Yuaan @ Victor Tan": "17B",
    "Justin Foo": "17B",
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
    ####################################
    "VIP 1": 1,
    "VIP 2": 2,
    "Table 3": 3,
    "Table 5": 5,
    "Table 6": 6,
    "Table 7": 7,
    "Table 8": 8,
    "Table 9": 9,
    "Table 10": 10,
    "Table 11": 11,
    "Table 18": 18,
    "Table 19": 19,
    "Table 20": 20,
    "Table 21": 21,
    "Table 22": 22,
    "Table 23": 23,
    "Table 25": 25,
    "Table 12A": "12A",
    "Table 12B": "12B",
    "Table 15A": "15A",
    "Table 15B": "15B",
    "Table 16A": "16A",
    "Table 16B": "16B",
    "Table 17A": "17A",
    "Table 17B": "17B",

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
    "16A": (410, 566-34/2),
    "17A": (680, 566-34/2),
    "12A": (410, 898-34/2),
    "15A": (680, 898-34/2),
    "16B": (410, 566+32/2),
    "17B": (680, 566+32/2),
    "12B": (410, 898+32/2),
    "15B": (680, 898+32/2),
}
font = ImageFont.truetype("ARIALBD.TTF", 50)

#bg_image = Image.open("Floorplan8.png").convert("RGBA")  
@st.cache_resource
def load_bg_image():
    return Image.open("Floorplan12a.png").convert("RGBA")

bg_image = load_bg_image()
# ========== UI ==========
st.title("Andrew and Sheryl 🥂✨🍾")
selected_guest = st.selectbox("Type your name to find your seat!", [name for name in guest_table_map],index=None)
# ========== IMAGE DRAWING ==========
if selected_guest:
    with st.spinner("Loading Seat..."):
        selected_table = guest_table_map[selected_guest]
        if selected_table == 0:
            st.image(bg_image)    
        else:
            st.subheader(f"Please find your table highlighted in yellow")
            st.markdown(f"{selected_guest}, you are seated at <u>**Table {selected_table}**</u> with:", unsafe_allow_html=True)
            #print out all the guests at the selected table
            guests_at_table = [name for name, table in guest_table_map.items() if table == selected_table]
            st.write("|| "+" || ".join(guests_at_table)+" ||")
            
            # Draw over a copy of the image
            img = bg_image.copy()
            draw = ImageDraw.Draw(img)

            for table_num, (x, y) in table_positions.items():
                radius = 55
                fill = "#FFD700" if table_num == selected_table else None
                width = 2 if table_num == selected_table else 0
                draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=fill, outline="black",width=width)
                
                if isinstance(table_num, int) and table_num == selected_table and table_num >= 10:
                    draw.text((x - radius + 25, y - radius + 25), str(table_num), fill="black", font=font) 
                elif isinstance(table_num, int) and table_num == selected_table and table_num < 10:
                    draw.text((x - radius + 40, y - radius + 25), str(table_num), fill="black", font=font)
                else:
                    pass

            # Draw rectangles for rectangle positions
            for table_num, (x, y) in rectangle_positions.items():
                width, height = 270, 34
                fill = "#FFD700" if table_num == selected_table else None
                draw.rectangle((x - width // 2, y - height // 2, x + width // 2, y + height // 2), fill=fill, outline="white")

            st.image(img)

else:
    st.image(bg_image)
