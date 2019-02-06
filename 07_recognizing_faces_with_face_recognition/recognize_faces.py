import face_recognition

# Load the known images
image_of_person_1 = face_recognition.load_image_file("known_person_1.jpg")
image_of_person_2 = face_recognition.load_image_file("known_person_2.jpg")

# Get the face encoding of each person. This can fail if no one is found in the photo.
person_1_face_encoding = face_recognition.face_encodings(image_of_person_1)[0]
person_2_face_encoding = face_recognition.face_encodings(image_of_person_2)[0]

# Create a list of all known face encodings
known_face_encodings = [
    person_1_face_encoding,
    person_2_face_encoding,
]

# Load the image we want to check
unknown_image = face_recognition.load_image_file("test_image.jpg")

# Get face encodings for any people in the picture
unknown_face_encodings = face_recognition.face_encodings(unknown_image)

# There might be more than one person in the photo, so we need to loop over each face we found
for unknown_face_encoding in unknown_face_encodings:
    face_distances = face_recognition.face_distance(known_face_encodings, unknown_face_encoding)
    print(f"Distance between unknown image and each known image: {face_distances}")

    # Test if this unknown face encoding matches any of the two people we know
    results = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding, tolerance=0.6)

    if results[0]:
        print(f"Found Person 1 in the photo!")
    if results[1]:
        print(f"Found Person 2 in the photo!")

