import experiments_holder
import os
import processor
import visualizer

experiment_directories = [os.path.join(os.getcwd(), directory)
                          for directory in os.listdir(os.getcwd())
                          if 'эксперимент' in directory]
print(experiment_directories)
experiments = experiments_holder.ExperimentsHolder(experiment_directories)

for name, images in enumerate(experiments):
    visualizer.visualize([processor.red_level(image) for image in images], str(name + 1))
