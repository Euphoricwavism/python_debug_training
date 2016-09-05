# -*- coding: utf-8 -*-
import random

# 描画領域を受け持つクラス
# フレームとフィールドから成り、フレームは主に枠を設けるために利用。フィールドは描画対象のクラスを秒がするために利用。
class Field(object):
    FRAME_WIDTH = 100
    FRAME_HEIGHT = 30
    FIELD_PADDING = 1
    FIELD_WIDTH = FRAME_WIDTH - FIELD_PADDING * 2
    FIELD_HEIGHT = FRAME_HEIGHT - FIELD_PADDING * 2
    
    def __init__(self):
        source_str = " " * 90 + "*" * 4 + "." * 3 + "o" * 2 + "@" * 1
        
        # フレームとフィールドの領域あらかじめ用意
        self.frame = [[" "] * self.FRAME_WIDTH] * self.FRAME_HEIGHT
        self.field = [[random.choice(source_str)] * self.FIELD_WIDTH] * self.FIELD_HEIGHT
        
        # フレームの外周に線を描画
        for row_index in range(self.FRAME_HEIGHT):
            for column_index in range(self.FRAME_WIDTH):
                if (row_index == 0 and column_index == 0) or \
                   (row_index == self.FRAME_HEIGHT - 1 and column_index == 0) or \
                   (row_index == 0 and column_index == self.FRAME_WIDTH - 1) or\
                   (row_index == self.FRAME_HEIGHT - 1 and column_index == self.FRAME_WIDTH - 1):
                    self.frame[row_index][column_index] = "+"
                elif row_index == 0 or row_index == self.FRAME_HEIGHT - 1:
                    self.frame[row_index][column_index] = "-"
                elif column_index == 0 or column_index == self.FRAME_WIDTH - 1:
                    self.frame[row_index][column_index] = "|"
        
    # フィールド領域に描画用のオブジェクトを上書きする、paddingによって端から空白を開けて描画する
    def draw_to_field(self, drawing_object, **kargs):
        # 描画領域の内側の空白領域の設定
        if 'padding' in kargs:
            padding_top = padding_left = padding_right = padding_bottom = kargs['padding']
        else:
            padding_top = kargs['padding_top'] if 'padding_top' in kargs else 0
            padding_left = kargs['padding_left'] if 'padding_left' in kargs else 0
            padding_right = kargs['padding_right'] if 'padding_right' in kargs else 0
            padding_bottom = kargs['padding_bottom'] if 'padding_bottom' in kargs else 0
            
        # 実際の上書き処理
        for do_row_index, f_row_index in enumerate(range(padding_top, self.FIELD_HEIGHT - 1 - padding_bottom)):
            if do_row_index > len(drawing_object):
                break
            for do_column_index, f_column_index in enumerate(range(padding_left, self.FIELD_WIDTH - 1 - padding_right)):
                if do_column_index > len(drawing_object[do_row_index]):
                    break
                self.field[f_row_index][f_column_index] = drawing_object[do_row_index][do_column_index]            
        
    # フレームつきのフィールドを返す
    def get_framed_field(self):
        framed_field = self.frame
        for fi_row_index, fr_row_index in enumerate(range(self.FIELD_PADDING, self.FRAME_HEIGHT - 1)):
            if fi_row_index > len(self.field) -1 :
                break
            for fi_column_index, fr_column_index in enumerate(range(self.FIELD_PADDING, self.FRAME_WIDTH - 1)):
                if fi_column_index > len(self.field[fi_row_index]) - 1:
                    break
                framed_field[fr_row_index][fr_column_index] = self.field[fi_row_index][fi_column_index]
        return framed_field

# 描画領域に言葉を挿入するためのクラス
class Word(object):
    
    def __init__(self, word = None):
        if word is None:
            self.word ="""    __    __            __  __                        
   |  \  |  \          |  \|  \                       
   | $$  | $$  ______  | $$| $$  ______               
   | $$__| $$ /      \ | $$| $$ /      \              
   | $$    $$|  $$$$$$\| $$| $$|  $$$$$$\             
   | $$$$$$$$| $$    $$| $$| $$| $$  | $$             
   | $$  | $$| $$$$$$$$| $$| $$| $$__/ $$             
   | $$  | $$ \$$     \| $$| $$ \$$    $$             
    \$$   \$$  \$$$$$$$ \$$ \$$  \$$$$$$              
                                      __        __    
                                     |  \      |  \   
    __   __   __   ______    ______  | $$  ____| $$   
   |  \ |  \ |  \ /      \  /      \ | $$ /      $$   
   | $$ | $$ | $$|  $$$$$$\|  $$$$$$\| $$|  $$$$$$$   
   | $$ | $$ | $$| $$  | $$| $$   \$$| $$| $$  | $$   
   | $$_/ $$_/ $$| $$__/ $$| $$      | $$| $$__| $$   
    \$$   $$   $$ \$$    $$| $$      | $$ \$$    $$   
     \$$$$$\$$$$   \$$$$$$  \$$       \$$  \$$$$$$$   
                                                            """.split('\n')
        else:
            self.word = word

    def get_word(self):
        return self.word

# 描画可能なオブジェクトをコンソール上に描画するためのクラス
class Display(object):
    
    def show(self, showing_object):
        for row in showing_object:
            for cell in row:
                print(cell, end="")
            print("")
        
if __name__ == '__main__':
    field = Field()
    word = Word()
    display = Display()
    field.draw_to_field(word.get_word(), padding_top = 4, padding_left = 25)
    display.show(field.get_framed_field())
    