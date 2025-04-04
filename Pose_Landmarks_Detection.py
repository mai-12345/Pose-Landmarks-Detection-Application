
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np
import streamlit as st
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2

st.title("Pose Landmarks Detection ")

image=st.file_uploader(" Please Upload An Image ",type=['png','jpg','jpeg','webp','avif'])


def draw_landmarks_on_image(rgb_image, detection_result):
  pose_landmarks_list = detection_result.pose_landmarks
  annotated_image = np.copy(rgb_image)

  # Loop through the detected poses to visualize.
  for idx in range(len(pose_landmarks_list)):
    pose_landmarks = pose_landmarks_list[idx]

    # Draw the pose landmarks.
    pose_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
    pose_landmarks_proto.landmark.extend([
      landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in pose_landmarks
    ])
    solutions.drawing_utils.draw_landmarks(
      annotated_image,
      pose_landmarks_proto,
      solutions.pose.POSE_CONNECTIONS,
      solutions.drawing_styles.get_default_pose_landmarks_style())
  return annotated_image


if image is not None:
    file_bytes = np.asarray(bytearray(image.read()), dtype = np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    st.image(image, 'Uploaded Image', use_container_width = True)

    mp_image = mp.Image(image_format = mp.ImageFormat.SRGB, data = image)


    # STEP 2: Create an PoseLandmarker object.
    base_options = python.BaseOptions(model_asset_path='C:/Users/H-p/Downloads/pose_landmarker_heavy.task')
    options = vision.PoseLandmarkerOptions(
       base_options=base_options,
       output_segmentation_masks=True)
    detector = vision.PoseLandmarker.create_from_options(options)


    # STEP 4: Detect pose landmarks from the input image.
    detection_result = detector.detect(mp_image)


    # STEP 5: Process the detection result. In this case, visualize it.
    annotated_image = draw_landmarks_on_image(mp_image.numpy_view(), detection_result)
    st.image(annotated_image, ' Image', use_container_width = True)


    # segmentation_mask = detection_result.segmentation_masks[0].numpy_view()
    # visualized_mask = np.repeat(segmentation_mask[:, :, np.newaxis], 3, axis=2) * 255
    # st.image(visualized_mask/255, 'n Image', use_container_width = True)
