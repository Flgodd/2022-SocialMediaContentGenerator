import os

import torch
from ldm.util import instantiate_from_config


class Model:
    def __init__(self):
        self.model = None
        self.current_model_name = ""

    def load_model_from_config(self, config, ckpt, verbose=False):
        print(f"Loading model from {ckpt}")
        pl_sd = torch.load(ckpt, map_location="cpu")
        if "global_step" in pl_sd:
            print(f"Global Step: {pl_sd['global_step']}")
        sd = pl_sd["state_dict"]
        model = instantiate_from_config(config.model)
        m, u = model.load_state_dict(sd, strict=False)
        if len(m) > 0 and verbose:
            print("missing keys:")
            print(m)
        if len(u) > 0 and verbose:
            print("unexpected keys:")
            print(u)

        model.cuda()
        model.eval()
        self.current_model_name = os.path.basename(ckpt)
        self.model = model

    @staticmethod
    def find_model(path):
        result = []
        for file in os.listdir(path):
            if file.endswith(".ckpt"):
                result.append(file)
        return result
