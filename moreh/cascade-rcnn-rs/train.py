from absl import app
from absl import flags

from official.common import flags as tfm_flags
from official.vision import train
from official.vision import registry_imports

FLAGS = flags.FLAGS


if __name__ == "__main__":
    tfm_flags.define_flags()
    flags.mark_flags_as_required(['experiment', 'mode', 'model_dir'])
    app.run(train.main)
