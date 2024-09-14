# DSRNet-Detector

## 安裝方法
* 請確保有安裝 `git` 以及　`Python >= 3.9`

1. 下載　Repositories　
    ```shell
    git clone https://github.com/IDK-Silver/dsrnet-detector.git
    ```
2. 進到　Repositories
    ```shell
   cd dsrnet-detector
    ```
3. Repositories　初始設定
    ```shell
   python setup_submodule.py
    ```
4. 安裝 Package
    ```shell
   pip install -e .
    ```
## 使用方法
詳細程式請見 [detector_example.py](https://github.com/IDK-Silver/dsrnet-detector/example/detector_example.py)

特別要注意的是 DSRNet 有提供 3 總不同的　model, 分別對應不同的 pt 檔案
* dsrnet_s
* dsrnet_l
* dsrnet_l_nature

在載入 model　要給予一個　DSRNetINetType 的 Enum 像是
* `DSRNetINetType.dsrnet_s`
* `DSRNetINetType.dsrnet_s`
* `dsrnet_l_nature`

```python
# import package
from dsrnet_detector.detector import DSRNetDetector, DSRNetINetType

# 建立 Detector
model = DSRNetDetector()

# 載入模型
model.load_model('path_to_your.pt', DSRNetINetType.your_model_type)

# 進行偵測
output_image = model.detect(input_image)
```