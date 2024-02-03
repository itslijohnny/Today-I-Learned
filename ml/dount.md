# Donut Model

The Donut model was proposed in OCR-free Document Understanding Transformer 
https://huggingface.co/docs/transformers/model_doc/donut

## Overview

![Donut uses Variational Autoencoders (VAEs) and Monte Carlo sampling to detect anomalies in time-series data. It's particularly effective for KPIs (Key Performance Indicators) in business systems.](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/model_doc/donut_architecture.jpg)



## Usage

Usage tips
The quickest way to get started with Donut is by checking the [tutorial notebook](https://github.com/NielsRogge/Transformers-Tutorials/tree/master/Donut), which show how to use the model at inference time as well as fine-tuning on custom data.
Donut is always used within the [VisionEncoderDecoder](https://huggingface.co/docs/transformers/model_doc/vision-encoder-decoder) framework.


## Training
We refer to the [tutorial notebooks](https://github.com/NielsRogge/Transformers-Tutorials/tree/master/Donut).


{% gist d2d9d06dc4338a5e5641ab7fec73dc07 gist}