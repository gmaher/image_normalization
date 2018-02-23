import os

in_ = './city_small.jpeg'
out = './results/output/'
os.system('python test.py -input {} -output {}'.format(in_,out))

in_ = './results/0082/19.npy'
out = './results/0082_output/'
os.system('python test.py -input {} -output {}'.format(in_,out))

in_ = './results/0110/47.npy'
out = './results/0110_output/'
os.system('python test.py -input {} -output {}'.format(in_,out))

in_ = './results/cabg5/142.npy'
out = './results/cabg5_output/'
os.system('python test.py -input {} -output {}'.format(in_,out))

in_ = './results/0171/78.npy'
out = './results/0171_output/'
os.system('python test.py -input {} -output {}'.format(in_,out))
