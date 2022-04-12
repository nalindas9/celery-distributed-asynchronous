from torchvision import transforms as tr
from torchvision.transforms import Compose

def augmentImg(img):
    """
    Augment the image with a random
    rotation, perspective and flip

    Args:
        img: Image to be augmented
    Returns:
        Augmented image
    """
    augment = Compose([tr.RandomRotation(degrees=30),
                       tr.RandomHorizontalFlip(),
                       tr.RandomPerspective(p=0.6)])
    augmented_img = augment(img)
    return augmented_img
    