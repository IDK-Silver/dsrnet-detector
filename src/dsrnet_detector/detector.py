import pathlib
from typing import Union

import numpy
import cv2
import torch
import torch.backends.cudnn as cudnn
import PIL.Image
from enum import Enum
from .extern.DSRNet.data.transforms import to_tensor
from .extern.DSRNet.models.dsrnet_model_sirs import DSRNetModel, tensor2im
from .extern.DSRNet.options.net_options.train_options import TrainOptions
from .extern.DSRNet.data import sirs_dataset as datasets
from .extern.DSRNet.data.image_folder import read_fns
torch.backends.cudnn.benchmark = False

class DSRNetINetType(Enum):
    # dsrnet_s = 'dsrnet_s'
    dsrnet_l = 'dsrnet_l'
    dsrnet_l_nature = 'dsrnet_l_nature'



class DSRNetDetector(DSRNetModel):
    def __init__(self):
        super().__init__()

    @torch.no_grad()
    def detect(self, image: Union[str, numpy.array]):

        # if user given a path then load image from path
        if isinstance(image, str):
            image = cv2.imread(image)
        assert image is not None, 'Image Not Found '

        # BGR to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = PIL.Image.fromarray(image)
        image = self.align(image)
        image = to_tensor(image)
        image = image.expand(1, -1, -1, -1)
        image.float()

        data = {
            "input": image,
            "fn": "test"
        }

        self.set_input(data, 'test')

        # predict
        output_i, output_j, output_rr = self.forward()

        # to BRG format
        output_i = tensor2im(output_i)
        output_i = cv2.cvtColor(output_i, cv2.COLOR_BGR2RGB)

        return output_i

    def load_model(self, model_weight_path, inet: DSRNetINetType):
        opt = TrainOptions()
        opt.isTrain = False
        cudnn.benchmark = False
        opt.no_log = True
        opt.display_id = 0
        opt.verbose = False
        opt.gpu_ids = ["cuda:0"]
        opt.checkpoints_dir = ''
        opt.model = 'dsrnet_model_sirs'
        opt.dataset = 'sirs_dataset'
        opt.name = 'dsrnet_l_test'
        opt.hyper = False
        opt.if_align = True
        opt.resume = True
        opt.weight_path = model_weight_path
        opt.base_dir = ''
        opt.loss = 'losses'
        opt.inet = inet.name
        opt.init_type = 'normal'
        opt.no_verbose = True
        self.initialize(opt)

    def align(self, x):
        h, w = x.height, x.width
        h, w = h // 32 * 32, w // 32 * 32
        x = x.resize((w, h))
        return x

