"""heater."""
from multiprocessing import Process
from argparse import ArgumentParser

parser = ArgumentParser('heaters.')
parser.add_argument('heaters', type=int, help='heaters?')
args = parser.parse_args()

def heating():
  """heater."""
  while True:
    pass

# heater
heaters = [Process(target=heating) for _ in range(args.heaters)]
[heater.start() for heater in heaters]
[heater.join() for heater in heaters]

