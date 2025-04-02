import streamlit as st
from emoji_reaction_component import emoji_reaction_component

st.title("Happy Eid✨")


col1,col2,col3 = st.columns(3)
columns = [col1,col2,col3]

images = [
"WhatsApp Image 2025-03-31 at 20.08.35_fd43b0f1.jpg",
"WhatsApp Image 2025-03-31 at 20.08.36_4f7d1b12.jpg",
"WhatsApp Image 2025-03-31 at 20.08.36_22e463e4.jpg",
"WhatsApp Image 2025-03-31 at 20.08.37_8f58eb84.jpg",
"WhatsApp Image 2025-03-31 at 20.08.37_f75af19a.jpg",
"WhatsApp Image 2025-04-01 at 13.34.33_000214cb.jpg",
"WhatsApp Image 2025-03-31 at 20.08.37_60f8dfd7.jpg",
"WhatsApp Image 2025-03-31 at 20.08.37_d3546fc7.jpg",
"WhatsApp Image 2025-04-01 at 13.34.35_ffcf7335.jpg",
"WhatsApp Image 2025-04-01 at 13.34.33_13650e1d.jpg",
"WhatsApp Image 2025-04-01 at 13.34.34_4eafe2d9.jpg",
"WhatsApp Image 2025-04-01 at 13.34.33_f67ee814.jpg",
"WhatsApp Image 2025-04-01 at 13.34.34_8a868ef1.jpg",
"WhatsApp Image 2025-04-01 at 13.34.34_b6129bd5.jpg",
"WhatsApp Image 2025-04-01 at 13.34.35_11abc98d.jpg"
]

for i,image in enumerate(images):
    col_index = i % 3
    with columns[col_index]:
        st.image(image, caption="")
        emoji_reaction_component(
            key=f"img_{i+1}", 
            emojis=["👍", "❤️", "😮","🥵","🔥"],
            save_to_file=True
        )


