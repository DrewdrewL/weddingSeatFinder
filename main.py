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
    "Casey Chan": 3,
    "Sandra Chan": 3,
    "Marc Chan": 3,
    "Cheyenne Chan": 3,
    "Mae Chan": 3,
    "Mdm Koh": 3,
    "Colin Chan": 3,
    "Luan Hua Chan": 3,
    "Collette Chan": 3,
    ####################################
    "Elvin Lee": 11,
    "Katherine Heng": 11,
    "Natalie Lee": 11,
    "Nicole Lee": 11,
    "Nellie Lee": 11,
    "Megan Lee": 11,
    "Alwin Lee": 11,
    "Mavis Chan": 11,
    "Serene Lee": 11,
    ####################################
    "Palvin Chan": 10,
    "Melynda Cheng": 10,
    "Oliver Chan": 10,
    "Miles Chan": 10,
    "Tom Cheng": 10,
    "Arlene Cheng": 10,
    "Stephanie Teo": 10,
    "Peter Teo": 10,
    "Tua Kng": 10,
    ####################################
    "Nelson Koh": 5,
    "Noven Koh": 5,
    "AD Chan": 5,
    "Carol Eguaras": 5,
    "Ali Al Kuwari": 5,
    "Marlian GW": 5,
    "Matthew Lee": 5,
    "Nicholas Lee": 5,
    "Han Mian Hwee": 5,
    "Lee Choo": 5,
    ####################################
    "Mr Teh": 9,
    "Mrs Teh": 9,
    "Teh Peijing": 9,
    "Teh Chee Huey": 9,
    "Teh Liming": 9,
    "Nell": 9,
    "Liming Daughter 1": 9,
    "Liming Daughter 2": 9,
    "Diana Pang": 9,
    "Steven Pang": 9,
    ####################################
    "Will Woon": 8,
    "Luna Xiong": 8,
    "Nicole Tan": 8,
    "Markus Yuen": 8,
    "Chermane Goh": 8,
    "Fonzarelli Ong": 8,
    "Joyce Skidell": 8,
    "Min Siang Loy": 8,
    "Jin Hong Ng": 8,
    "Jit Yong Ang": 8,
    ####################################
    "Cassandra Hesler": 7,
    "Bradley Goh": 7,
    "Jin Wei Krishnan": 7,
    "Tim Young": 7,
    "Charmian Koh": 7,
    "Benjamin Ang": 7,
    "Yue Ern Lee": 7,
    "Abhishek Choudhary": 7,
    "Wayne Toh": 7,
    "Jonathan Raharja": 7,
    ####################################
    "Nicholas mum": 6,
    "Nicholas dad": 6,
    "Naresh Vashdev": 6,
    "Deena Loo": 6,
    "Eric Lee": 6,
    "Val Lee": 6,
    "Kenneth Chew": 6,
    "Nicholas Phang": 6,
    "Jarell Ang": 6,
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
    "Trisa Tin": "17A",
    "Rikki Sim": "17A",
    "Brandon Sim": "17A",
    "Glenn Ang": "17A",
    "Julia Sim": "17A",
    "Jamie Ang": "17B",
    "Ryan Ang": "17B",
    "Marcus Tin": "17B",
    "Ivan Tin": "17B",
    "Charlene (Brandon)": "17A",
    "Jan Sim": "17B",
    "Nesh (Jan)": "17B",
    "Faith Lee": "17A",
    "Daryl Ang": "17A",
    ####################################
    "Angela Shenead": "16A",
    "Cheryl Cheong": "16B",
    "Tania Tan": "16A",
    "Kelly Ha": "16A",
    "Vanessa Ghui": "16A",
    "Vera Lim": "16A",
    "Izzah": "16A",
    "Diane Tan": "16A",
    "Jeneen Foo": "16B",
    "Zen Sze": "16B",
    "Anzelle Lee": "16B",
    "Tan Zuu Yuaan @ Victor Tan": "16B",
    "Justin Foo": "16B",
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
    "3rd Uncle (Simon's side)": 25,
    "3rd Uncle's Wife (Simon's side)": 25,
    "4th Uncle (Simon)": 25,
    "Elsie Tan": 25,
    "Cindy Soon": 25,
    "Francis Soon": 25,
    "William Tan": 25,
    "Michelle Tan": 25,
    ####################################
    "Maryam (Sheryl)": 19,
    "Wati (Sheryl)": 19,
    "Annie Leung": 19,
    "Nelson Leung": 19,
    "Yee Joo Poo": 19,
    "Karen Soh": 19,
    "4th Uncle (Josephine)": 19,
    "4th Uncle's Wife (Josephine)": 19,
    "3rd Uncle (Josephine)": 19,
    "3rd Uncle's Wife (Josephine)": 19,
    ####################################
    "James Tan": 23,
    "Sharon Tan": 23,
    "Daniel Kwan": 23,
    "Joe Leng": 23,
    "Shirley Leng": 23,
    "Zach Chua": 23,
    "Sherrie Chua": 23,
    "Karen Tan": 23,
    "Kenneth Tan": 23,
    ####################################
    "Lorraine Tay": 20,
    "Peter Tay": 20,
    "Willie Liam": 20,
    "Jye Chong": 20,
    "Johnson Soh": 20,
    "Linus Terh": 20,
    "Lawrence Chan": 20,
    "Mr Adrian Tee": 20,
    "Mrs Adrian Tee": 20,
    ####################################
    "John Ow": 22,
    "Aloysius Yang": 22,
    "Yelun Yang": 22,
    "Wen Xu Goh": 22,
    "Stephen Cao": 22,
    "Hafiz Alsree": 22,
    "Paul Li": 22,
    "Cassius Kua": 22,
    "Quinn Wong": 22,
    "Ethan Sun": 22,
    ####################################
    "Sean Neighbour": 21,
    "Sean Wife": 21,
    "Opposite Neighbour": 21,
    "Opposite Neighbour Wife": 21,
    "Edgar Tan": 21,
    "Margaret Tan": 21,
    "Molly Goh": 21,
    "Roland Goh": 21,
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
    "Don't click me": 0

}

table_positions = {
    2: (132, 551),
    19: (455, 403),
    18: (228, 403),
    25: (338, 225),
    23: (565, 225),
    22: (791, 225),
    7: (1019, 1240),
    20: (681, 403),
    21: (910, 403),
    1: (132, 916),
    3: (338, 1240),
    5: (564, 1240),
    6: (791, 1240),
    10: (455, 1062),
    11: (229, 1062),
    9: (682, 1062),
    8: (911, 1062),
}
rectangle_positions ={
    "17A": (410, 566-34/2),
    "16A": (680, 566-34/2),
    "12A": (410, 898-34/2),
    "15A": (680, 898-34/2),
    "17B": (410, 566+32/2),
    "16B": (680, 566+32/2),
    "12B": (410, 898+32/2),
    "15B": (680, 898+32/2),
}
font = ImageFont.truetype("ARIALBD.TTF", 50)

#bg_image = Image.open("Floorplan14.png").convert("RGBA")  
@st.cache_resource
def load_bg_image():
    return Image.open("Floorplan14.png").convert("RGBA")

bg_image = load_bg_image()
# ========== UI ==========
st.title("Andrew and Sheryl 🥂✨🍾")
selected_guest = st.selectbox("Type your name to find your seat!", [name for name in guest_table_map],index=None)
# ========== IMAGE DRAWING ==========
if selected_guest:
    with st.spinner("Loading Seat..."):
        selected_table = guest_table_map[selected_guest]
        if selected_table == 0:
            st.subheader("Do you feel good for clicking?")
            st.image(Image.open("EasterEgg.png").convert("RGBA"))    
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
