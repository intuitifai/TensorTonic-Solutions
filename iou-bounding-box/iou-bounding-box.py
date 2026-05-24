def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    # Write code here
    x1, y1, x2, y2 = 0, 1, 2, 3
    # Step 1: Find intersection co-ordinates
    inter_x1 = max(box_a[x1], box_b[x1])
    inter_y1 = max(box_a[y1], box_b[y1])
    inter_x2 = min(box_a[x2], box_b[x2])
    inter_y2 = min(box_a[y2], box_b[y2])
    # Step 2: Compute Intersection area
    inter_width = max(0, inter_x2 - inter_x1)
    inter_height = max(0, inter_y2 - inter_y1)
    intersection = inter_width * inter_height
    # Step 3: Compute union area
    area_a = (box_a[x2] - box_a[x1]) * (box_a[y2] - box_a[y1])
    area_b = (box_b[x2] - box_b[x1]) * (box_b[y2] - box_b[y1])
    union = area_a + area_b - intersection
    # Finally! Compute IoU
    return intersection / union

    