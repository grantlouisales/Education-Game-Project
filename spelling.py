import arcade
from arcade.camera import Camera
from arcade.scene import Scene
from arcade.sprite import Sprite
from arcade.sprite_list.spatial_hash import check_for_collision_with_list

import random
import string
import threading
import time
from constants import *
from MenuView import *
from read_words_file import *


class Spelling():
    
    class Letter(arcade.Sprite):
        def __init__(self, letter, x, y):
            super().__init__(f'resources/letters/letter{str.upper(letter)}.png', center_x=x, center_y=y, scale=.1)
            self.letter = letter
             


    def __init__(self, scene : Scene, player : Sprite, map : string):
        self.letters_collected = []
        self.map_letters = arcade.SpriteList()
        self.scene = scene
        self.curr_word = None
        self.curr_letter = None
        self.player = player
        self.map = map
        self.locations = self.get_locations()
        self.correct_ping = arcade.sound.load_sound("audio/correct_ping.mp3")
        self.error_ping = arcade.sound.load_sound("audio/error_ping.mp3")
        self.get_new_word()
        self.start_word()

    def get_locations(self):
        if self.map == "Map1Hard.json":
            return HARD_LOCATIONS
        elif self.map == "Map1Medium.json":
            return MED_LOCATIONS
        else:
            return EASY_LOCATIONS

    def get_words_list(self):
        if self.map == "Map1Hard.json":
            return get_hard_words()
        elif self.map == "Map1Medium.json":
            return get_medium_words()
        else:
            return get_easy_words()

    def create_letter(self, letter : str, position):
        letter_sprite = self.Letter(letter, position[0], position[1])
        self.map_letters.append(letter_sprite)
        self.scene.add_sprite(f'Letter', letter_sprite)

    def collect_letter(self, letter : Letter):
        # Play sound Accordingly, depending on the letters collected!!!
        # if letter.letter in self.curr_word:
        #     arcade.play_sound(self.correct_ping)
        # else:
        #     arcade.play_sound(self.error_ping)
        self.letters_collected.append(letter)
    
       
        index = self.letters_collected.index(letter) + 1
        self.clear_letters()
        self.next_letter(letter.position)

        letter.center_x, letter.center_y = (index * 50, 50)

    def draw_gui(self):
        for letter in self.letters_collected:
            letter.draw()

    def start_word(self, prev_location=None):
        self.letters_collected = []
        self.curr_letter = (self.curr_word[0], 0)
        self.generate_letters(self.locations, prev_location)

    def get_new_word(self, old_word = None):
        list_words = self.get_words_list()
        test_word = random.choice(list_words)
        if not test_word == old_word:
            self.curr_word = test_word


    def generate_letters(self, pos_list, prev_location):
        while True:
            locations = random.sample(pos_list, 3)
            for location in locations:
                print(location)
            if not prev_location in locations:
                break
            else:
                print("Failed")

        letters = random.sample(string.ascii_lowercase, 2)
        self.create_letter(self.curr_letter[0], locations.pop())
        for place in locations:
            self.create_letter(letters.pop(), place)
        print("--------------------------")

    def clear_letters(self):
        self.scene.remove_sprite_list_by_name('Letter')
        self.map_letters = arcade.SpriteList()

    def next_letter(self, prev_location):
        index = self.curr_letter[1]
        if index == len(self.curr_word) - 1:
            if self.assemble_word() == self.curr_word:
                arcade.play_sound(self.correct_ping)
                self.get_new_word(old_word=self.curr_word) 
            else:
                arcade.play_sound(self.error_ping)
                
            self.start_word(prev_location=prev_location)
            self.draw_word = True
            self.word_timer = 0 
        else:
            self.curr_letter = (self.curr_word[index + 1], index + 1)
            self.generate_letters(self.locations, prev_location)

    def assemble_word(self):
        word = ''
        for letter in self.letters_collected:
            word += letter.letter
        return word
    
    draw_word = True
    word_timer = 0