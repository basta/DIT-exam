---
id: mpv_005
course: Methods of Computer Vision
tags: [orientation, dominant-gradient, sift, rotation-invariance]
difficulty: 2
type: open
status: to_learn
---

# Question
Describe **ways of local feature orientation estimation**.

---
# Solution
Orientation estimation turns a similarity- or affine-covariant detection (position + scale + shape) into a fully rotation-invariant frame by assigning a canonical angle. Several approaches exist.

## 1. Dominant Gradient Orientation (SIFT)
1. Take a circular patch around the keypoint at the characteristic scale $\sigma$.
2. Compute gradient magnitude $m(x,y)$ and orientation $\theta(x,y)$ at every pixel.
3. Build a **weighted orientation histogram** with $B$ bins (commonly $B = 36$, 10° each). The vote at $(x, y)$ is weighted by $m(x, y)$ and by a Gaussian centered at the keypoint with $\sigma_w \approx 1.5 \sigma$.
4. Smooth the histogram and find its peak; refine the peak location by quadratic interpolation across neighboring bins.
5. **Multiple orientations:** create a separate keypoint for every secondary peak that is $\ge 80\%$ of the global peak (improves stability).

## 2. Gradient Average Vector
Compute the average gradient vector inside the patch and use its direction. Simple but less stable than histogram-based methods.

## 3. Centroid-Based (BRIEF / ORB)
The orientation is the angle from the patch center $C$ to the intensity centroid
$$
\theta = \arctan\!\left( \frac{m_{01}}{m_{10}} \right), \quad m_{pq} = \sum_{x,y} x^p y^q I(x, y).
$$
Used in **ORB**. Fast but only one orientation per keypoint.

## 4. Major Axis of the Shape
For affine-covariant regions (Harris-Affine, MSER), the eigenvectors of the second moment matrix already give two principal axes. The remaining 1-DOF rotation is resolved by *one* of: the dominant gradient, gradient histogram, or by using e.g. the dark/bright side as a tiebreaker.

## 5. Learned Orientation (LF-Net, AffNet)
A small neural network is trained to predict the orientation that makes the patch most consistent with descriptor matching. The loss is end-to-end (descriptor distance between corresponding patches).

## Properties
- Orientation must be **covariant** with the image: rotating the image by $\alpha$ must add $\alpha$ to the estimate.
- Multiple-orientation outputs increase recall on locally symmetric structures.
- Errors in orientation propagate as errors in the descriptor; in SIFT, descriptor robustness is the main reason small orientation errors are tolerated.

## Related Concepts
- [[SIFT]]
- [[ORB]]
- [[AffNet]]
- [[rotation-invariance]]
