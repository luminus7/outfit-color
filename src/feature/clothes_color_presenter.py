import cv2



class ClothesColorPresenter:
    def __init__(self, left_margin,
                 total_box_color,
                 total_box_border_color,
                 one_box_border_color,
                 one_color_box_width,
                 one_color_box_height,
                 padding):
        self.__left_margin = left_margin
        self.__total_box_color = total_box_color
        self.__total_box_border_color = total_box_border_color
        self.__one_box_border_color = one_box_border_color
        self.__one_color_box_width = one_color_box_width
        self.__one_color_box_height = one_color_box_height
        self.__padding = padding

    def insert(self, frame, clothes_color_s, pedestrian_coordinates):
        image_draw = frame.copy()
        x, y, w, h = map(int, pedestrian_coordinates)
        x += self.__left_margin
        total_box_st_x = x - self.__padding
        total_box_ed_x = x + self.__one_color_box_width * 3 + self.__padding
        total_box_st_y = y - self.__padding
        total_box_ed_y = y + self.__one_color_box_height + self.__padding
        cv2.rectangle(image_draw, (total_box_st_x, total_box_st_y),
                      (total_box_ed_x, total_box_ed_y), self.__total_box_color, -1, 1)
        cv2.rectangle(image_draw, (total_box_st_x, total_box_st_y),
                      (total_box_ed_x, total_box_ed_y),
                      self.__total_box_border_color, 1, 1)
        one_box_st_x = x
        one_box_st_y = y
        one_box_ed_y = one_box_st_y + self.__one_color_box_height
        for color_idx in range(3):
            one_box_ed_x = one_box_st_x + self.__one_color_box_width
            cv2.rectangle(image_draw, (one_box_st_x, one_box_st_y), (one_box_ed_x, one_box_ed_y),
                          clothes_color_s[color_idx],
                          -1, 1)
            cv2.rectangle(image_draw, (one_box_st_x, one_box_st_y), (one_box_ed_x, one_box_ed_y),
                          self.__one_box_border_color,
                          1, 1)
            one_box_st_x = one_box_ed_x
        return image_draw
