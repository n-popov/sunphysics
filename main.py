import experiments_holder
import os
import processor
import visualizer

experiment_directories = [os.path.join(os.getcwd(), directory)
                          for directory in os.listdir(os.getcwd())
                          if 'эксперимент' in directory]
print(experiment_directories)
experiments = experiments_holder.ExperimentsHolder(experiment_directories)

first_experiment_images = experiments[0]

visualizer.visualize([processor.red_level(image) for image in first_experiment_images], '1')
