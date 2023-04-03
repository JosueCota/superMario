import pygame as pg


class Timer:
  def __init__(self, image_list, start_index=0, delay=100, is_loop=True): 
    self.image_list = image_list
    self.delay = delay 
    self.is_loop = is_loop
    self.last_time_switched = pg.time.get_ticks()
    self.frames = len(image_list)
    self.start_index = start_index
    self.index = start_index if start_index <= len(image_list) - 1 else 0
    
  def next_frame(self): 
    if self.is_expired(): return
    now = pg.time.get_ticks()
    if now - self.last_time_switched > self.delay:
      self.index += 1
      if self.is_loop: self.index %= self.frames
      self.last_time_switched = now

  def reset(self):
    self.index = self.start_index if self.start_index < len(self.image_list) - 1 else 0

  def is_expired(self):
    return not self.is_loop and self.index >= len(self.image_list) - 1

  def image(self): 
    self.next_frame()
    return self.image_list[self.index]
  

class TimerDict(Timer):
  def __init__(self, image_dict, start_key, start_index=0, delay=100, is_loop=True):
   
    super().__init__(image_dict[start_key], start_index=start_index, delay=delay, is_loop=is_loop)
    self.image_dict = image_dict
    self.start_key = start_key

  def reset(self):
    self.image_list = self.image_dict[self.start_key]
    super().reset()

  def keys(self):
    return self.image_dict.keys()

  def has_key(self, key):
    return key in self.image_dict.keys()

  def switch_to_key(self, key):
    if not self.has_key(key):
      raise KeyError(f'Key {key} is not in the TimerDict')
    self.image_list = self.image_dict[key]
    self.start_index = 0
    self.last_time_switched = pg.time.get_ticks()


class TimerDual(Timer):
  def __init__(self, image_list1, image_list2, start_index=0, delay=100, is_loop=True):
    super().__init__(image_list1, start_index=start_index, delay=delay, is_loop=is_loop)
    self.image_list1= image_list1
    self.image_list2= image_list2

    self.start_key = start_index

  def reset(self):
    self.image_list = self.image_dict[self.start_key]
    super().reset()

  def keys(self):
    return self.image_dict.keys()

  def has_key(self, key):
    return key in self.image_dict.keys()

  def switch_to_key(self, key):
    if not self.has_key(key):
      raise KeyError(f'Key {key} is not in the TimerDict')
    self.image_list = self.image_dict[key]
    self.start_index = 0
    self.last_time_switched = pg.time.get_ticks()