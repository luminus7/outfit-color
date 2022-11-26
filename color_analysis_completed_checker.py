class ColorAnalysisCompletedChecker:
    def __init__(self):
        self.__frame_id_s = set()

    def is_color_analysis_completed(self, frame_id):
        return frame_id in self.__frame_id_s

    def inform_color_analysis_is_completed(self, frame_id):
        self.__frame_id_s.add(frame_id)


if __name__ == "__main__":
    checker = ColorAnalysisCompletedChecker()
    print(checker.is_color_analysis_completed(12))
    checker.inform_color_analysis_is_completed(12)
    print(checker.is_color_analysis_completed(12))
