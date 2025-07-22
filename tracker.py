"""
tracker.py
This script lets the user select an object in the first frame of the webcam feed
and then tracks it using either CSRT or KCF tracker.
"""

import cv2
from utils import create_tracker
import argparse
import time

def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--tracker", type=str, default="CSRT", choices=["CSRT", "KCF"],
                        help="Tracker type to use: CSRT or KCF")
    args = parser.parse_args()

    print(f"[INFO] Starting video stream using {args.tracker} tracker...")
    tracker = None
    initBB = None
    fps = None

    # Start video capture from webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("[ERROR] Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        (H, W) = frame.shape[:2]

        # If tracking is active
        if initBB is not None:
            (success, box) = tracker.update(frame)

            if success:
                (x, y, w, h) = [int(v) for v in box]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # FPS information
                fps.stop()
                fps.start()

                info = [
                    ("Tracker", args.tracker),
                    ("Success", "Yes" if success else "No"),
                    ("FPS", f"{1000.0 / fps.getTimeMilli():.2f}")
                ]

                for (i, (k, v)) in enumerate(info):
                    text = f"{k}: {v}"
                    cv2.putText(frame, text, (10, H - ((i * 20) + 20)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        cv2.imshow("Tracking", frame)
        key = cv2.waitKey(1) & 0xFF

        # If user presses "s", select ROI
        if key == ord("s"):
            if frame is not None:
                initBB = cv2.selectROI("Tracking", frame, fromCenter=False, showCrosshair=True)
                cv2.waitKey(1)  

                print(f"[DEBUG] Frame shape: {frame.shape}, dtype: {frame.dtype}")
                print(f"[DEBUG] initBB: {initBB}")

                # Make sure user selected a valid ROI (not cancelled or zero size)
                if initBB[2] > 0 and initBB[3] > 0:
                    tracker = create_tracker(args.tracker)
                    tracker.init(frame, initBB)
                    fps = cv2.TickMeter()
                    fps.start()
                else:
                    print("[WARNING] Invalid ROI selected. Try again.")
            else:
                print("[ERROR] Frame is empty. Cannot select ROI.")
        
        # Quit
        elif key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
