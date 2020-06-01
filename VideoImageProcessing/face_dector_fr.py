from PIL import Image
import face_recognition

start_time = time.time()


def extract_faces(img, dir_name):
    image = face_recognition.load_image_file(img)
    print(img)

    # Find all the faces in the image using the default HOG-based model.
    # This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
    # See also: find_faces_in_picture_cnn.py
    face_locations = face_recognition.face_locations(image)

#     print("I found {} face(s) in this photograph.".format(len(face_locations)))
#     face_landmarks_list = face_recognition.face_landmarks(image)
#     print(face_landmarks_list)
    head, tail = os.path.split(img)

    if len(face_locations) == 1:
    

        # Print the location of each face in this image
        top, right, bottom, left = face_locations
        #print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

        # You can access the actual face itself like this:
        face_image = image[top:bottom, left:right]

        pil_image = Image.fromarray(face_image)

        #pil_image.show()
        #os.makedirs('folder/subfolder/')
        
        os.makedirs(head+"/"+dir_name+"/", exist_ok=True)
        

        pil_img_name = head + "/" + dir_name + "/" + tail + "_fd_" + str(n) + ".jpg"
        print(pil_img_name)
        pil_image = pil_image.save(pil_img_name)
        
        n+=1

if __name__ == "__main__":
    directory = sys.argv[1]
    for img in os.listdir(directory):
        img_name  = img
        path_img=os.path.join(directory, img)
        if os.path.isdir(path_img) or (path_img == directory+"/" '.DS_Store'):
            continue
        extract_faces(path_img, sys.argv[2])

print("--- %s seconds ---" % (time.time() - start_time))