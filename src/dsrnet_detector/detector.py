from .extern.DSRNet.models.dsrnet_model_sirs import DSRNetModel
from .extern.DSRNet.options.net_options.train_options import TrainOptions
import torch.backends.cudnn as cudnn

class DSRNetDetector(DSRNetModel):
    def __init__(self):
        super().__init__()

    def detect(self):
        pass

    def load_model(self, model_weight_path):
        opt = TrainOptions()
        opt.isTrain = False
        cudnn.benchmark = True
        opt.no_log = True
        opt.display_id = 0
        opt.verbose = False
        opt.gpu_ids = 0
        opt.checkpoints_dir = ''
        opt.resume  = None
        opt.model = 'dsrnet_model_sirs'
        opt.dataset = 'sirs_dataset'
        opt.name = 'dsrnet_l_test'
        opt.hyper = True
        opt.if_align = True
        opt.resume = True
        opt.weight_path = model_weight_path
        opt.base_dir = ''
        opt.loss = 'losses'
        opt.inet = 'dsrnet_l'
        opt.init_type = 'edsr'
        opt.no_verbose = False


        self.initialize(opt)

