import tensorflow as tf
import numpy as np
import cv2

model = tf.keras.models.load_model(r'D:\D Drive\harsh\Sound_Control\model_v1.h5')


cap = cv2.VideoCapture(0)

while True:
   
    ret, frame = cap.read()


    resized_frame = tf.image.resize(frame, (256,256))  # Adjust size based on your model input size
    input_data = tf.cast(resized_frame/255. ,tf.float32)
    input_data = tf.expand_dims(resized_frame, axis=0)

    predictions = model.predict(input_data)


    predicted_class = np.argmax(predictions)


    cv2.putText(frame, f'Class: {predicted_class}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the resulting frame

    cv2.imshow('Webcam Classification', frame)
    cv2.waitKey(1)
    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
