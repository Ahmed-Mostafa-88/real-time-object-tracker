"""
utils.py
Contains utility functions for selecting OpenCV object trackers.
"""

import cv2

def create_tracker(tracker_type="CSRT"):
    """
    Create an OpenCV object tracker based on the specified type.
    
    Args:
        tracker_type (str): One of ["CSRT", "KCF"]
    
    Returns:
        tracker: OpenCV tracker instance
    """
    tracker_type = tracker_type.upper()
    if tracker_type == "CSRT":
        return cv2.TrackerCSRT_create()
    elif tracker_type == "KCF":
        return cv2.TrackerKCF_create()
    else:
        raise ValueError(f"Unsupported tracker type: {tracker_type}")
