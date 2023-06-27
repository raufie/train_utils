import numpy as np
class ReplayBuffer:
    def __init__(self, buffer_size):
        self.buffer = []
        self.buffer_size = buffer_size
        self.curr_index = 0
    
    def add(self, experience):
        if len(self.buffer) <self.buffer_size:
            self.buffer.append(experience)
        else:
            self.buffer[self.curr_index%self.buffer_size] = experience
        self.curr_index+=1
    
    def __repr__(self):
        return str(self.buffer)
    
    def get_batch(self, batch_size):
        
        ix = np.random.choice(len(self.buffer), batch_size, p=None)
        
        
        return zip(*[self.buffer[i] for i in ix])
        