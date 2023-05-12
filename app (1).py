import streamlit as st
import requests
import json
from PIL import Image
import gtts

#styleing
css_style = """
<style>
    .about {
        text-align: justfiy;
        border: 2px solid black;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 20px;
        text-align: justify;
    }

    .about:hover {
        box-shadow: 0px 2px 1px grey;
    }

    .grid-container {
        display: grid;
        grid-template-columns: auto auto auto;
        padding: 15px;
        column-gap: 10px;
        row-gap: 10px;
        border: 2px solid black;
        border-radius: 10px;
    }

    .img {
        width: 200px;
        height: 200px;
        margin-left: 10px;
        transition: transform 2s;
    }

    .label {
        text-align: center;
        font-weight: bold;
        margin: 0px;
        transition: transform 2s;
    }

    .img:hover {
        transform: scale(1.1);
        
    }

    .img:hover + p {
        transform: translateY(10px);
    }

    h5 {
        font-style: italic;
    }

</style>
"""
#set css styles
st.markdown(css_style, unsafe_allow_html=True)

#####subscription key
subscription_key = 'c537b6bc07cd411295298cb315e9ecc2'#prediction key

################################Needful Functions###################################
def get_prediction(image_path):
  
    with open(image_path, 'rb') as img:
            image_data = img.read()
    #setting the headers
    headers = {
                'Prediction-Key': subscription_key,
                'Content-Type': 'application/octet-stream'
            }
           
    #copy the URL
    url = 'https://imaginecupinstance-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/09117061-4ac4-4266-a5c4-6f3722b01216/classify/iterations/Iteration2/image'
    r = requests.post(url,headers = headers, data = image_data)
    response = json.loads(r.content)
    print(response)
    return response


def label_info(main_label, *args):
    st.subheader(f"Proper E-Waste Management - {main_label}")
    sub_header = f"""
        <h5>How to properly Manage  {main_label} as E-Wastes</h5>
        """
    st.markdown(sub_header, unsafe_allow_html=True)

    for content in args:
        st.markdown(f"- {content}")


def info_function(label):
    section_break = """
    <hr>
    """
    st.markdown(section_break, unsafe_allow_html=True)
    st.header("Let's Prevent E - Wastes")
    st.image("https://ewrhub.com/wp-content/uploads/2019/05/E-Waste-Eco-Friendly-e1558200601173.jpg", caption = "E-Waste Management")
    if label == "Monitor":
        label_info(
            label,
            "Reduce: The first step in managing monitor e-waste is to reduce the amount of waste produced. Consider purchasing monitors that have a long lifespan and can be easily upgraded or repaired.",
            "Reuse: If your old monitors are still in good working condition, consider donating them to schools or non-profit organizations. You can also sell them or give them away to friends or family.",
            "Recycle: If your monitors are no longer usable, recycle them. Look for certified e-waste recyclers in your area who follow environmentally friendly practices.",
            "Dispose: If you cannot recycle your monitors, dispose of them properly. Do not throw them in the trash or leave them on the curb for the garbage collector. Check with your local government for disposal guidelines.",
            "Data wiping: Before disposing or recycling your monitors, make sure to wipe all the data from them to protect your personal information. Use data wiping software or hire a professional service to do it for you."
        )

    elif label == "Mobile":
        label_info(
            label,
            "Reduce: The first step in managing mobile e-waste is to reduce the amount of waste produced. Consider purchasing mobile devices that have a long lifespan and can be easily upgraded or repaired.",
            "Reuse: If your old mobile devices are still in good working condition, consider donating them to schools, charities, or non-profit organizations. You can also sell them or give them away to friends or family.",
            "Recycle: If your mobile devices are no longer usable, recycle them. Look for certified e-waste recyclers in your area who follow environmentally friendly practices. Some manufacturers and service providers also offer recycling programs for their products.",
            "Dispose: If you cannot recycle your mobile devices, dispose of them properly. Do not throw them in the trash or leave them on the curb for the garbage collector. Check with your local government for disposal guidelines.",
            "Data wiping: Before disposing or recycling your mobile devices, make sure to wipe all the data from them to protect your personal information. Use data wiping software or hire a professional service to do it for you.",
            "Battery management: Mobile devices contain lithium-ion batteries that should be managed properly to prevent fires and explosions. Do not expose them to extreme temperatures, puncture or damage them, or mix them with other types of batteries."
        )
    
    elif label == "Laptop":
        label_info(
            label,
            "Reduce: The first step in managing laptop e-waste is to reduce the amount of waste produced. Consider purchasing laptops that have a long lifespan and can be easily upgraded or repaired.",
            "Reuse: If your old laptop is still in good working condition, consider donating it to schools, charities, or non-profit organizations. You can also sell it or give it away to friends or family.",
            "Recycle: If your laptop is no longer usable, recycle it. Look for certified e-waste recyclers in your area who follow environmentally friendly practices. Some manufacturers and service providers also offer recycling programs for their products.",
            "Dispose: If you cannot recycle your laptop, dispose of it properly. Do not throw it in the trash or leave it on the curb for the garbage collector. Check with your local government for disposal guidelines.",
            "Data wiping: Before disposing or recycling your laptop, make sure to wipe all the data from it to protect your personal information. Use data wiping software or hire a professional service to do it for you.",
            "Battery management: Laptops contain lithium-ion batteries that should be managed properly to prevent fires and explosions. Do not expose them to extreme temperatures, puncture or damage them, or mix them with other types of batteries.",
            "Proper packaging: When shipping your laptop for recycling, use appropriate packaging materials to protect it during transport. Use recyclable or biodegradable packaging materials whenever possible."
        )

    elif label == "Mix":
        label_info(
            label,
            "Reduce: The first step in managing e-waste is to reduce the amount of waste produced. Consider purchasing electronic devices that have a long lifespan and can be easily upgraded or repaired.",
            "Reuse: If your old electronic devices are still in good working condition, consider donating them to schools, charities, or non-profit organizations. You can also sell them or give them away to friends or family.",
            "Recycle: If your electronic devices are no longer usable, recycle them. Look for certified e-waste recyclers in your area who follow environmentally friendly practices. Some manufacturers and service providers also offer recycling programs for their products.",
            "Dispose: If you cannot recycle your electronic devices, dispose of them properly. Do not throw them in the trash or leave them on the curb for the garbage collector. Check with your local government for disposal guidelines.",
            "Data wiping: Before disposing or recycling your electronic devices, make sure to wipe all the data from them to protect your personal information. Use data wiping software or hire a professional service to do it for you.",
            "Battery management: Electronic devices contain batteries that should be managed properly to prevent fires and explosions. Do not expose them to extreme temperatures, puncture or damage them, or mix them with other types of batteries.",
            "Proper packaging: When shipping your electronic devices for recycling, use appropriate packaging materials to protect them during transport. Use recyclable or biodegradable packaging materials whenever possible."
        )

    elif label == "Keyboard":
        label_info(
            label,
            "Reduce: The first step in managing keyboard e-waste is to reduce the amount of waste produced. Consider purchasing keyboards that have a long lifespan and can be easily repaired.",
            "Reuse: If your old keyboard is still in good working condition, consider donating it to schools, charities, or non-profit organizations. You can also sell it or give it away to friends or family.",
            "Recycle: If your keyboard is no longer usable, recycle it. Look for certified e-waste recyclers in your area who follow environmentally friendly practices. Some manufacturers and service providers also offer recycling programs for their products.",
            "Dispose: If you cannot recycle your keyboard, dispose of it properly. Do not throw it in the trash or leave it on the curb for the garbage collector. Check with your local government for disposal guidelines.",
            "Battery management: Keyboards do not contain batteries, but they may contain small quantities of hazardous materials such as lead, mercury, and cadmium. These materials can cause harm to human health and the environment if not disposed of properly. Always handle keyboards with care and avoid breaking or damaging them."
        )
    
    elif label == "Mouse":
        label_info(
            label,
            "Reduce: The first step in managing mouse e-waste is to reduce the amount of waste produced. Consider purchasing mice that have a long lifespan and can be easily repaired.",
            "Reuse: If your old mouse is still in good working condition, consider donating it to schools, charities, or non-profit organizations. You can also sell it or give it away to friends or family.",
            "Recycle: If your mouse is no longer usable, recycle it. Look for certified e-waste recyclers in your area who follow environmentally friendly practices. Some manufacturers and service providers also offer recycling programs for their products.",
            "Dispose: If you cannot recycle your mouse, dispose of it properly. Do not throw it in the trash or leave it on the curb for the garbage collector. Check with your local government for disposal guidelines.",
            "Battery management: Mice do not contain batteries, but they may contain small quantities of hazardous materials such as lead, mercury, and cadmium. These materials can cause harm to human health and the environment if not disposed of properly. Always handle mice with care and avoid breaking or damaging them."
        )
    

def create_sound(label_prompt):
    prompt = f"This is a {label_prompt}"
    
    text_to_audio = gtts.gTTS(prompt)
    text_to_audio.save("prediction.wav")


# def autoplay_audio(file_path: str):
#     with open(file_path, "rb") as f:
#         data = f.read()
#         b64 = base64.b64encode(data).decode()
#         md = f"""
#             <audio id = "audio-wav" controls autoplay="true">
#             <source src="data:audio/wav;base64,{b64}" type="audio/wav">
#             </audio>
#             """
#         st.markdown(
#             md,
#             unsafe_allow_html=True,
#         )

          
#title of the web app
st.title("E Waste Classification")

#main image
st.image("https://cdnsm5-hosted.civiclive.com/UserFiles/Servers/Server_13659739/Image/recycling/banners/ewaste.jpg", caption = "E-Waste")

#sidebar
with st.sidebar:
    #set title for the sidebar
    st.header("E - Waste")
    #set the side bar image
    st.image("https://thumbs.dreamstime.com/b/pile-electronic-waste-gadgets-use-isolated-white-background-reuse-recycle-concept-144517803.jpg", caption = "Types of E-Waste")
    #about e waste
    st.subheader("What are E-Waste?")
    st.markdown("- Electronic waste or e-waste describes discarded electrical or electronic devices. Used electronics which are destined for refurbishment, reuse, resale, salvage recycling through material recovery, or disposal are also considered e-waste.")
    #bad effects of e waste
    st.subheader("Negative Effects of E-waste")
    st.markdown("- Electronic waste contains toxic components that are dangerous to human health, such as mercury, lead, cadmium, polybrominated flame retardants, barium and lithium")
    st.markdown("- The negative health effects of these toxins on humans include brain, heart, liver, kidney and skeletal system damage.")
    st.markdown("- It can also considerably affect the nervous and reproductive systems of the human body, leading to disease and birth defects.")
    st.markdown("- Improper disposal of e-waste is unbelievably dangerous to the global environment, which is why it is so important to spread awareness on this growing problem and the threatening aftermath.")
    st.subheader("How to Avoid?")
    st.markdown("- To avoid these toxic effects of e-waste, it is crucial to properly e-cycle, so that items can be recycled, refurbished, resold, or reused. The growing stream of e-waste will only worsen if not educated on the correct measures of disposal.")

tab1, tab2, tab3 = st.tabs(["About Project ❓", "Predictions 💻", "Camera Upload 📷"])

with tab1:
    st.header("About the project")
    para = """
    <div class = "about">
        <p>
        E-waste, or electronic waste, refers to discarded electronic devices and equipment that are no longer wanted or useful. This can include items such as computers, smartphones, televisions, and other electronic appliances. E-waste is a growing problem, with millions of tons of electronic devices being discarded each year, leading to environmental and health concerns. Recycling and proper disposal of e-waste are important to reduce its negative impact on the environment and human health.
        </p>
        <ul>
            There are mainly three tabs,
            <li>About Project - You can find information and guidance on how to properly interact with the web app</li>
            <li>Predictions - This is the prediction dashboard. You can enter images to make predictions.</li>
            <li>Camera Upload - Take images using the device camera and make predictions</li>
        </ul>
    </div>
    """
    st.markdown(para, unsafe_allow_html=True)

    st.subheader("Categories Classified...")
    #categories classified
    grid_image = """
    <div class="grid-container">
        <div class="grid-item">
            <img class = "img" src = "https://checksammy.com/wp-content/uploads/2021/06/Electronics-Debrand.jpg" alt = "laptop">
            <p class = "label">Laptops</p>
        </div>
        <div class="grid-item">
            <img class = "img" src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWSXVYJ8O1YK287m-6uHZpzdNIvvKgRIrXvuJqkE-VGJ2QzjC8nqnPz96TyDHWoa3cGW8&usqp=CAU" alt = "monitor">
            <p class = "label">Monitors</p>
        </div>
        <div class="grid-item">
            <img class = "img" src = "https://images.nature.com/original/magazine-assets/nindia.2017.57/nindia.2017.57_19308654.jpg" alt = "mouse">
            <p class = "label">Mouse</p>
        </div>  
        <div class="grid-item">
            <img class = "img" src = "https://www.datocms-assets.com/27942/1607440625-pileofoldphones-compareandrecycle.jpg" alt = "mobile">
            <p class = "label">Mobile</p>
        </div>
        <div class="grid-item">
            <img class = "img" src = "https://cdn.shopify.com/s/files/1/0651/6224/8447/articles/keyboard-ewaste_1100x.jpg?v=1671645474" alt = "keyboard">
            <p class = "label">Keyboard</p>
        </div>
        <div class="grid-item">
            <img class = "img" src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-v0LD-zyf2VK5aVofb4gz_orjJw8wCnIj4A&usqp=CAU" alt = "mix">
            <p class = "label">Mix</p>
        </div> 
    </div>
    
    """

    st.markdown(grid_image, unsafe_allow_html=True)

with tab2:
   #predictions by uploading an image
    image_file = st.file_uploader("Please upload an image", accept_multiple_files=False, help="Add a supportive image type", type=['jpeg','jpg','png'])

    if image_file:
        image = Image.open(image_file)
        image.save('input.png')

        #save the image
        st.image(image)

        img_path = "input.png"
        #get predictions
        response = get_prediction(img_path)
        predicted_label = response['predictions'][0]['tagName']
        #audio creation
        create_sound(predicted_label)
        st.subheader("Label is {}".format(predicted_label))

        #play the video
        st.audio("prediction.wav")

        #set the info according to the predictions
        info_function(predicted_label)

with tab3:
    #camera input
    cam_image = st.camera_input("Please take a photo")

    if cam_image:
        #displaying the image
        st.image(cam_image)

        #save the image currently
        cam_input_image = Image.open(cam_image)
        cam_input_image.save("cam_image.png")

        cam_image_path = "cam_image.png"
        #get the predictions
        cam_response = get_prediction(cam_image_path)
        predicted_cam_response = cam_response['predictions'][0]['tagName']
        #audio creation
        create_sound(predicted_cam_response)
        st.subheader("Label is {}".format(predicted_cam_response))
        #play the audio
        st.audio("prediction.wav")
        #set the label according to the predictions
        info_function(predicted_cam_response)
