import cv2
import os
seconds = {
    # "Vertolyot": 13,
    "Samolyot": 18,
    "Kursi": 26,
    "Odam": 33,
    "Davlat": 40,
    # "Dunyo": 45,
    "Tarix": 52,
    # "Uy": 58,
    # "Razvetka": 64,
    "Bo`luv": 71,
    "Ko`paytiruv": 76,
    "Qo'shuv": 81,
    "Ayiruv": 86,
}

n = 0
DATA_DIR = r'C:\Users\PC\PROJECTS\sign-language-detector-python\data1'
for i in seconds:
    # Open the video file
    video_path = r"C:\Users\PC\PROJECTS\sign-language-detector-python\video_2024-04-20_06-25-45.mp4"  # Replace this with the path to your video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video opened successfully
    if not cap.isOpened():
        print("Error: Unable to open video file")
        exit()

    # Get the frame rate of the video
    fps = cap.get(cv2.CAP_PROP_FPS)
    # print(fps)
    # Define the starting and ending seconds
    start_second = seconds[i]  # Starting second (a)


    # Convert seconds to frames
    start_frame = int(start_second * fps)
    end_frame = int(start_frame + 100)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Define the codec for the output video
    output_video_path = f"{n}_{i}.mp4"  # Path to save the trimmed video
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (int(cap.get(3)),int(cap.get(4))))

    # Set the frame position to the starting frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
    # Read and write frames from the video
    frame_count = 0
    if not os.path.exists(os.path.join(DATA_DIR, str(n))):
        os.makedirs(os.path.join(DATA_DIR, str(n)))

    while cap.isOpened():
        ret, frame = cap.read()
        # print(cap.get(cv2.CAP_PROP_POS_FRAMES))
        # Check if the frame is empty (end of video or reached the end frame)
        if not ret or cap.get(cv2.CAP_PROP_POS_FRAMES) > end_frame:
            n+=1
            break

        # Write the frame to the output video
        out.write(frame)

        cv2.imwrite(os.path.join(DATA_DIR, str(n), '{}.jpg'.format(frame_count)), frame)

        frame_count += 1


        # Display the frame (optional)
        cv2.putText(frame, f"{i}", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('Trimmed Video', frame)

        # Check for the 'q' key to exit the loop
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Release the video capture and video writer objects
    cap.release()
    out.release()

    # Close all windows
    cv2.destroyAllWindows()
    # print(seconds)