class Observable:
   
    def __init__(self):
        self.observer_list=[]

    def attach(self, obs):
        self.observer_list.append(obs)

    def detach(self, obs):
         self.observer_list.remove(obs)

    def notify(self):
        for obs in self.observer_list:
            obs.update()



class Observer:
    def __init__(self):
        pass

    def update(self):
        pass
