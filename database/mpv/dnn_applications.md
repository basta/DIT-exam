---
id: mpv_044
course: Methods of Computer Vision
tags: [DNN, applications, computer-vision, survey]
difficulty: 2
type: open
status: to_learn
---

# Question
**Deep Neural Nets — applications in computer vision.**

---
# Solution

## Where Deep Nets Are State-of-the-Art

### Image-Level Tasks
- **Image classification:** ImageNet, ResNet, EfficientNet, ViT, ConvNeXt. Single label or multi-label outputs.
- **Image retrieval:** GeM-pooled CNN features, NetVLAD, DELG, SOLAR, CLIP — learned embeddings + ANN search.
- **Place recognition / visual localization:** NetVLAD, Patch-NetVLAD, hloc — recognize where a photo was taken.
- **Few-shot / zero-shot classification:** Prototypical Networks, CLIP — natural-language supervision.
- **Self-supervised pretraining:** SimCLR, MoCo, BYOL, MAE, DINO — learn general-purpose representations without labels.

### Detection & Localization
- **Object detection:** Faster R-CNN, YOLO family, RetinaNet, DETR.
- **Instance segmentation:** Mask R-CNN, Mask2Former, SOLO.
- **Semantic segmentation:** FCN, U-Net, DeepLab, Segformer, Mask2Former.
- **Panoptic segmentation:** combines instance + semantic — Mask2Former, Panoptic FPN.
- **Keypoint detection / pose estimation:** OpenPose, HRNet, ViTPose for human pose; 6-DoF pose for objects.
- **Face detection / recognition / verification:** MTCNN, RetinaFace, ArcFace embeddings.

### Geometry, Depth, Motion
- **Monocular depth estimation:** MiDaS, ZoeDepth, MarigolD.
- **Stereo matching:** RAFT-Stereo, PSMNet.
- **Optical flow:** FlowNet, PWC-Net, RAFT, GMFlow.
- **3-D reconstruction & SfM:** SuperPoint + SuperGlue + COLMAP; Dust3R for end-to-end 3-D from 2 views.
- **NeRF / 3-D Gaussian Splatting:** novel view synthesis, neural 3-D representations.
- **Visual SLAM / VIO:** DROID-SLAM, learned descriptors for ORB-SLAM-style pipelines.

### Generative / Image-to-Image
- **Image generation:** GANs (StyleGAN), diffusion models (Stable Diffusion, DALL·E, Imagen).
- **Conditional generation:** text-to-image, layout-to-image, ControlNet.
- **Image editing & restoration:** super-resolution (SRCNN, ESRGAN, Real-ESRGAN), denoising, deblurring (DnCNN, NAFNet), inpainting, colorization, dehazing.
- **Style transfer:** neural style transfer, AdaIN.
- **Video frame interpolation / extrapolation:** RIFE, Film.

### Tracking
- **Single-object tracking:** SiamFC, KCF (classical), DiMP, SiamRPN++, OSTrack, ARTrack.
- **Multi-object tracking (MOT):** Detection-by-tracking (SORT, ByteTrack), Tracktor, transformer-based MOTR.

### Action / Video Understanding
- **Action recognition:** I3D, SlowFast, TimeSformer, Video Swin, VideoMAE.
- **Temporal action detection / localization, video question answering, captioning.**

### OCR / Document Understanding
- **Scene text detection and recognition:** EAST, CRAFT, TrOCR.
- **Document layout analysis, table extraction, form understanding** (LayoutLM family).

### Medical Imaging
- **Tumor / lesion detection and segmentation** (CT, MRI, histopathology): U-Net and 3-D variants, nnU-Net.
- **Cell segmentation, slide classification, radiology report generation.**

### Autonomous Driving / Robotics
- **Lane detection, road segmentation, traffic-sign recognition.**
- **Bird's-eye-view perception**, **occupancy prediction**, **3-D object detection** from LiDAR (PointPillars, CenterPoint) or cameras (BEVFormer).
- **End-to-end driving** (UniAD, VAD).
- **Visual servoing, grasping, manipulation** policies (Dex-Net, ACT, RT-2).

### Multimodal
- **Vision-language models:** CLIP, BLIP, LLaVA, GPT-4V, Gemini — caption, VQA, grounding.
- **Open-vocabulary detection / segmentation:** GLIP, OWL-ViT, Grounding DINO, SAM.

### Anomaly Detection / Industrial Vision
- **Defect inspection** in manufacturing: PatchCore, PaDiM, EfficientAD.
- **Surface inspection, quality control.**

### AR / VR
- **Hand/body pose, gaze tracking, scene understanding** for AR.
- **6-DoF camera tracking** with learned features for VR/AR.

## Common Thread
All of these tasks share a common pattern: a deep network maps raw pixels (or pixel sequences) to structured outputs (labels, boxes, masks, vectors, 3-D structures, generated pixels). Improvements typically come from:
- Better backbones (CNN → Transformer, hybrid models).
- Better self-supervised pretraining (massively scaled, multi-modal).
- Task-specific heads and losses that directly optimize the evaluation metric (IoU losses, AP loss, etc.).
- Large, diverse training data; sometimes synthetic.

## Related Concepts
- [[ResNet]]
- [[ViT]]
- [[Mask-R-CNN]]
- [[CLIP]]
- [[diffusion-models]]
- [[NeRF]]
