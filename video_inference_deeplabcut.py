from pathlib import Path
from dlclibrary import download_huggingface_model
import deeplabcut

input_video_path = "./videos/monkeys.mp4"

# superanimal_name (pretrained pose model for the target animal/body type):
#   superanimal_bird, superanimal_topviewmouse, superanimal_quadruped, superanimal_humanbody
# model_name (pose estimation architecture):
#   hrnet_w32, resnet_50, rtmpose_s
# detector_name (object detection architecture):
#   fasterrcnn_mobilenet_v3_large_fpn, fasterrcnn_resnet50_fpn_v2, ssdlite

deeplabcut.video_inference_superanimal(
	[str(input_video_path)],
	superanimal_name="superanimal_quadruped",
    model_name="hrnet_w32",
	video_extensions="mp4",
    detector_name="fasterrcnn_resnet50_fpn_v2",
)
