import boto3 
import json 
import streamlit as st 
 
st.title('Celebrity details') 
def recognize_celebrities(photo): 
 
     
    client=boto3.client('rekognition') 
    #img_file=st.file_uploader('Upload Face Image',type=['png','jpg','jpeg','jfif']) 
 
    with open('alia.jpg', 'rb') as image: 
        response = client.recognize_celebrities(Image={'Bytes': image.read()}) 
        #image.write(img_file.getbuffer()) 
 
    print('Detected faces for ' + photo)     
    for celebrity in response['CelebrityFaces']: 
        st.write ('Name: ' + str(celebrity['Name'])) 
        st.write ('Id: ' + str(celebrity['Id'])) 
        st.write ('KnownGender: ' + str(celebrity['KnownGender'])) 
        #st.write ('Smile: ' + str(celebrity['Smile'])) 
        st.write ('Position:') 
        st.write ('   Left: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Height'])) 
        st.write ('   Top: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Top'])) 
        st.write ('Info') 
        for url in celebrity['Urls']: 
            st.write ('   ' + url) 
        st.write 
    return len(response['CelebrityFaces']) 
 
def main(): 
    photo='moviestars.jpg' 
 
    celeb_count=recognize_celebrities(photo) 
    print("Celebrities detected: " + str(celeb_count)) 
 
 
if __name__ == "__main__": 
    main()