import cv2

class image:
    def __init__(self,path):
        self.path=path
        # self.image=self.load_image(self.path)
        # self.show=self.show_image(self.image)
    def load_image(self):
        self.image=cv2.imread(self.path)
        return self.image
    def show_image(self,image):
        cv2.imshow('image',self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    path='./test_image.webp'
    test=image(path)


