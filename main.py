import streamlit as st
from PIL import Image, ImageDraw, ImageFont


# ========== CONFIG ==========
# Sample guest -> table mapping
guest_table_map = {
    "-" : 0,
    "Aldrin Lee": 1,
    "Audrey Chan": 1,
    "Sheryl (The Bride)": 1,
    "Andrew (The Groom)": 1,
    "Angie Chan": 1,
    "Peter Chan": 1,
    "Rose Chua": 1,
    "Terry Koh": 1,
    "Andrea Lee": 1,
    "Theodore Koh": 1,
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
    "Makarios Tang": 12,
    "Xinyi Low": 12,
    "Edna Chah": 12,
    "Janessa Yim": 12,
    "Alyssa Siow": 12,
    "Travis Tseng": 12,
    "Christine Teo": 12,
    "Andrea Chong": 12,
    "Main Ray Lim": 12,
    "Ambrose Yew": 12,
    "Vian Wee": 12,
    "Marcus Guo": 12,
    "Lettitia Quack": 12,
    "Weilun Gan": 15,
    "Kelly Tng": 15,
    "Whitney David": 15,
    "Laurence Sukarti": 15,
    "Matthew Chia": 15,
    "Rachel Ng": 15,
    "Trevor": 15,
    "Claudia Lee": 15,
    "Kai Qing": 15,
    "Shawn": 15,
    "Melanie": 15,
    "Lay Shuen": 15,
    "Maryam Mohammed": 15,
    "Maryam (Sheryl)": 16,
    "Wati (Sheryl)": 16,
    "Daryl Ang": 16,
    "Faith Lee": 16,
    "Jamie Ang": 16,
    "Ryan Ang": 16,
    "Jan Sim": 16,
    "Nesh (Jan)": 16,
    "Julia Sim": 16,
    "Glenn (Julia)": 16,
    "Brandon Sim": 16,
    "Charlene (Brandon)": 16,
    "Ivan Tin": 16,
    "Marcus Tin": 16,
    "Kelly": 17,
    "Tania": 17,
    "Zen": 17,
    "Jeneen": 17,
    "Cheryl Cheong": 17,
    "Vera": 17,
    "Izzah": 17,
    "Vanessa Ghui": 17,
    "Diane": 17,
    "Angela Shenead": 17,
    "Anzelle Lee": 17,
    "Victor Tan Zuu Yuaan": 17,
    "Justin Foo": 17,
    "Table 3": 3,
    "Table 5": 5,
    "Table 6": 6,
    "Table 7": 7,
    "Table 8": 8,
    "Table 9": 9,
    "Table 10": 10,
    "Table 11": 11,
    "Table 19": 19,
    "Table 20": 20,
    "Table 21": 21,
    "Table 22": 22,
    "Table 23": 23,
    "Table 25": 25,
}
# Table positions (x, y) in image coordinates
table_positions = {
    1: (130, 551),
    6: (454, 403),
    3: (227, 403),
    5: (336, 225),
    7: (564, 225),
    9: (790, 225),
    11: (1018, 225),
    8: (680, 403),
    10: (910, 403),
    2: (130, 919),
    19: (336, 1242),
    21: (564, 1242),
    23: (790, 1242),
    20: (454, 1065),
    18: (227, 1065),
    22: (681, 1065),
    25: (910, 1065),
}
rectangle_positions ={
    12: (410, 569),
    15: (680, 569),
    16: (410, 901),
    17: (680, 901),
}
#st.set_page_config(layout="wide")

# Load background floor plan image
bg_image = Image.open("Floorplan8.png").convert("RGBA")  # Replace with your image

# ========== UI ==========
st.title("Andrew and Sheryl 🥂")
#guest = st.text_input("Search for a guest", "")

# Filter matches
#matches = [name for name in guest_table_map if guest.lower() in name.lower()]

#if matches:
selected_guest = st.selectbox("Search for a guest", [name for name in guest_table_map])
#else:
 #   selected_guest = None

# ========== IMAGE DRAWING ==========
if selected_guest:
    selected_table = guest_table_map[selected_guest]
    st.write(f"**Your table is now highlighted in yellow**")
    st.write(f"**{selected_guest} is seated at Table {selected_table} with:**")
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
        #draw.text((x , y ), f"{table_num}", fill="black", align="center",fontsize=20)

    # Draw rectangles for rectangle positions
    for table_num, (x, y) in rectangle_positions.items():
        width, height = 270, 65
        fill = "yellow" if table_num == selected_table else None
        draw.rectangle((x - width // 2, y - height // 2, x + width // 2, y + height // 2), fill=fill, outline="red")
        #draw.text((x , y ), f"{table_num}", fill="black", align="center",fontsize=20)

    st.image(img)
else:
    st.image(bg_image)
