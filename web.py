import streamlit as st
import tensorflow as tf
import numpy as np

def model_prediction(test_image):
    model=tf.keras.models.load_model("trained_plant_disease_model.keras")
    image= tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
    input_arr=tf.keras.preprocessing.image.img_to_array(image)
    input_arr=np.array([input_arr])
    predictions=model.predict(input_arr)
    return np.argmax(predictions)
st.sidebar.title("Plant Disease Detection System")
app_mode=st.sidebar.selectbox('select page',['Home','Disease Recognition'])

from PIL import Image

img=Image.open('Diseases.jpg')
st.image(img)

if (app_mode=='HOME'):
    st.markdown("<h1 style='text-align: center;'>Plant Disease Detection System",unsafe_allow_html=True)

elif (app_mode=='Disease Recognition'):
    st.header('Plant Disease Recognition System')

test_image=st.file_uploader('Choose an image:')
if(st.button('Show Image')):
    st.image(test_image,width=4,use_column_width=True)

if(st.button('Predict')):
    st.snow()
    st.write('Our Prediction')
    result_index=model_prediction(test_image)
    class_name=['Potato_Early_blight','Potato_Late_blight','Potato_Healthy']
    st.success('Model is predicting its a {}'.format(class_name[result_index])) 