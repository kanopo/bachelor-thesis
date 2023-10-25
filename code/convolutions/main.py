from typing import List
from PIL import Image
import torch
import torchvision.transforms as transforms

import matplotlib.pyplot as plt

conv_layer = torch.nn.Conv2d(in_channels=3, out_channels=1, kernel_size=3)


def conv_image(image: Image.Image, iterations: int = 1) -> list[torch.Tensor]:
    tensors: list[torch.Tensor] = []

    transform = transforms.Compose([transforms.ToTensor()])

    tensor: torch.Tensor = transform(image)
    tensors.append(tensor)

    for i in range(iterations):
        output = conv_layer(tensors[-1].unsqueeze(0))

        tensors.append(output.squeeze(0))

    return tensors


tensors = conv_image(Image.open("dog.jpg"), 1)

# view with matplotlib

plt.figure(figsize=(20, 20))
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(tensors[0].permute(1, 2, 0).numpy())
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Convolution 1")
plt.imshow(tensors[1].squeeze(0).detach().numpy(), cmap="gray")
plt.axis("off")


plt.savefig("original.png")
