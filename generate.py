from lottie import objects

class Anim:
    # Animation class

    def __init__(self, frames, size, images_location):
        self._anim = objects.Animation(frames)

        # try to parse the size(wxh)
        try:
            w = size.split('x')[0]
            h = size.split('x')[1]
        except IndexError:
            raise ValueError('Wrong size format. 720x360')

        self._anim.width = w
        self._anim.height = h

        for idx, image in enumerate(images_location):
            img = objects.assets.Image().load(image)
            self._anim.assets.append(img)

            layer = objects.ImageLayer(img.id)

            c = self._anim.add_layer(layer)
            c.start_time = idx
            c.in_point = idx      # type: ignore
            c.out_point = idx + 1 # type: igonre

    def get(self):
        return self._anim
