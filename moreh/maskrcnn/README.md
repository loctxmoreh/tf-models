# Training Mask-RCNN on COCO2017 dataset on Moreh AI Framework

![https://badgen.net/badge/NVIDIA-A100/passed/green]
![https://badgen.net/badge/Moreh-HAC/failed/red]


## Prepare

### Code
Clone and switch to the `maskrcnn` branch
```
git clone https://github.com/loctxmoreh/tf-models
cd tf-models
git checkout -b maskrcnn --track origin/maskrcnn
```

### Environment
#### On A100 machine
Use the file `a100env.yml` to create a `conda` environment:
```
conda env create -f a100env.yml
conda activate tf-models
```

**Note**: on A100 machine, make sure `LD_LIBRARY_PATH` contains the `lib/` of
your `conda` environment, so `tensorflow` can find CUDA libraries

#### On HAC machine
Use the file `hacenv.yml` to create a `conda` environment:
```
conda env create -f hacenv.yml
conda activate tf-models
update-moreh --force --tensorflow 2.9.0 --target 23.5.0
```

### Data
First, download COCO2017 dataset and extract. Then use this script
`official/vision/data/create_coco_tf_record.py` to prepare the dataset in
`tfrecord` format. Files belong to the train set should have the prefix `train`,
`val` for validation set and `test` for test set.

## Run
Move to this project directory:
```
cd moreh/maskrcnn
```

Copy/move/symlink the `tfrecord` COCO2017 dataset to `coco/`
```
# symlink
ln -s /path/to/coco2017/tfrecords coco
```

Then run the training script:
```
./run
```

Checkpoints & training logs will be saved in `output/`
