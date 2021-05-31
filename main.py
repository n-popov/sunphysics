import experiments_holder
import os
import processor
import visualizer

experiment_directories = [os.path.join(os.getcwd(), directory)
                          for directory in os.listdir(os.getcwd())
                          if 'эксперимент' in directory]
experiment_deltas = [os.path.join(os.getcwd(), filename)
                     for filename in os.listdir(os.getcwd())
                     if 'delta' in filename]
experiment_angles = [os.path.join(os.getcwd(), filename)
                     for filename in os.listdir(os.getcwd())
                     if 'angle' in filename]

print(experiment_directories)
experiments = experiments_holder.ExperimentsHolder(experiment_directories, experiment_angles, experiment_deltas)

for name, (images, angles_file, deltas_file) in enumerate(experiments):
    deltas = [float(line) for line in open(deltas_file)]
    angles = [float(line) for line in open(angles_file).readlines()]
    visualizer.visualize(angles, [processor.red_level(image) / delta
                          for image, delta in zip(images, deltas)], str(name + 1))
