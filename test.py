from lightgluestick import LightGlueStick
from lightgluestick import SuperPoint
from lightgluestick import LSD
import torch
from pathlib import Path
from lightgluestick.utils import load_image, batch_to_np
from lightgluestick import TwoViewPipeline
import cv2
from lightgluestick.viz2d import plot_images, plot_keypoints, plot_lines, plot_color_line_matches, plot_matches
from matplotlib import pyplot as plt

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")  # 'mps', 'cpu'
images = Path("resources/images")

conf = {
        'name': 'two_view_pipeline',
        'use_lines': True,
        'extractor': {
            "name": "wireframe",
            "point_extractor": {
                "name": "superpoint",
                "trainable": False,
                "dense_outputs": True,
                "max_num_keypoints": 2048,
                "force_num_keypoints": False,
            },
            "line_extractor": {
                "name": "lsd",
                "trainable": False,
                "max_num_lines": 250,
                "force_num_lines": False,
                "min_length": 15,
            },
            "wireframe_params": {
                "merge_points": True,
                "merge_line_endpoints": True,
                "nms_radius": 3,
            },
        },
        'matcher': {
            'name': 'lightgluestick',
            'weights': 'resources/weights/lightgluestick.tar',
            'trainable': False,
        },
        'ground_truth': {
            'from_pose_depth': False,
        }
    }

pipeline_model = TwoViewPipeline(conf).to(device).eval()

image0 = load_image(images / "3819243606_7acfaf85dd_o.jpg").to(device)[None]
image1 = load_image(images / "3827640857_c93cdfb501_o.jpg").to(device)[None]

x = {'view0': {"image": image0}, 'view1': {"image": image1}}

pred = pipeline_model(x)
pred = batch_to_np(pred)

kp0, kp1 = pred["keypoints0"], pred["keypoints1"]
m0 = pred["matches0"]

line_seg0, line_seg1 = pred["lines0"], pred["lines1"]
line_matches = pred["line_matches0"]

valid_matches = m0 != -1
match_indices = m0[valid_matches]
matched_kps0 = kp0[valid_matches]
matched_kps1 = kp1[match_indices]

valid_matches = line_matches != -1
match_indices = line_matches[valid_matches]
matched_lines0 = line_seg0[valid_matches]
matched_lines1 = line_seg1[match_indices]

# Plot the matches
img0 = image0[0].permute(1, 2, 0).cpu().numpy()
img1 = image1[0].permute(1, 2, 0).cpu().numpy()

plot_images([img0, img1], dpi=200, pad=2.0)
plot_lines([line_seg0, line_seg1], ps=4, lw=2)
plt.gcf().canvas.manager.set_window_title('Detected Lines')
plt.savefig('detected_lines.png')

plot_images([img0, img1], dpi=200, pad=2.0)
plot_keypoints([kp0, kp1], colors='c')
plt.gcf().canvas.manager.set_window_title('Detected Points')
plt.savefig('detected_points.png')

plot_images([img0, img1], dpi=200, pad=2.0)
plot_color_line_matches([matched_lines0, matched_lines1], lw=2)
plt.gcf().canvas.manager.set_window_title('Line Matches')
plt.savefig('line_matches.png')

plot_images([img0, img1], dpi=200, pad=2.0)
plot_matches(matched_kps0, matched_kps1, color="lime", lw=1.0, a=0.4)
plt.gcf().canvas.manager.set_window_title('Point Matches')
plt.savefig('point_matches.png')