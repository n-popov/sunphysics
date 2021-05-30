import experiments_holder
import os
import processor
import visualizer

from cache import Cache

experiment_directories = [os.path.join(os.getcwd(), directory)
                          for directory in os.listdir(os.getcwd())
                          if 'эксперимент' in directory]
print(experiment_directories)
experiments = experiments_holder.ExperimentsHolder(experiment_directories)

first_experiment_images = experiments[0]

cache = Cache()

visualizer.visualize([processor.red_level(image, cache) for image in first_experiment_images], '1')

cache.save_cache()